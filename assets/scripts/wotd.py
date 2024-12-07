import getopt
import os
import random
import re
import sys

from datetime import date, datetime, timedelta
from email import utils as email_utils

from mastodon import Mastodon

instance_url = "https://mastodon.social"
account_id = 113590173980484259

separator_head = "<!-- WOTD START -->"
separator_tail = "<!-- WOTD END -->"

# Getting the WotD ==================================

def fetch_posts(days):
	posts_per_day = 12
	quantity = posts_per_day * days + 1

	if quantity > 40:
		print("ERROR: Mastodon API has maximum post fetch size of 40 (you asked for {quantity}).")
		exit(0)

	mastodon = Mastodon( api_base_url=instance_url)
	posts = mastodon.account_statuses(id=account_id, limit=quantity)
	posts = sorted(posts, key=lambda x: x["created_at"])

	today = date.today()
	target_date = today - timedelta(days=days)

	return [post for post in posts if post["created_at"].date() == target_date]

def choose_post(posts):
	def get_score(post):
		return post["favourites_count"] + post["reblogs_count"] + post["replies_count"]

	score_map = {}
	for post in posts:
		score = get_score(post)
		if not score in score_map:
			score_map[score] = []

		score_map[score].append(post)

	high_score = max(score_map.keys())
	chosen = random.choice(score_map[high_score])

	return chosen

def parse_post(post):
	content = post["content"]
	exp = re.compile("<p>(\\S*) \\(([^\\)]*)\\)<br \\/>([^<]*)<\\/p>")
	m = exp.match(content)

	form = m.group(1)
	type = m.group(2)
	gloss = m.group(3)

	return [form, type, gloss]

def get_wotd():
	print("> FETCHING")
	posts = fetch_posts(3)
	print("> CHOOSING")
	wotd = choose_post(posts)
	print("> PARSING")
	parsed = parse_post(wotd)

	return parsed

# Updating the site ==================================

def format_wotd(wotd):
	form = wotd[0]

	type_dict = {"adj": "adjective", "n": "noun", "v": "verb"}
	type = wotd[1]
	if wotd[1] in type_dict:
		type = type_dict[wotd[1]]

	gloss = wotd[2]

	return f"<b>{form}</b> &#183; <i>{type}</i><br>{gloss}"

def update_site(root_path, wotd):
	def process_file(file):
		with open(file, encoding='utf-8') as file_data:
			original_content = file_data.read()
			new_content = re.sub(f"{separator_head}(\\s*).*(\\s*){separator_tail}", f"{separator_head}\\1{format_wotd(wotd)}\\2{separator_tail}", original_content, flags=re.MULTILINE)

			# Write
			f = open(file, "w")
			f.write(new_content)
			f.close()

	def update_dir(path):
		files = [path + "/" + file for file in os.listdir(path)]

		for file in files:
			if os.path.isdir(file):
				update_dir(file)
			elif file.endswith(".html"):
				process_file(file)

	print("> UPDATING SITE")
	update_dir(root_path)

# Generate RSS ===============================

def format_wotd_rss(wotd):
	title = wotd[0]
	description = f"<b>{wotd[0]}</b> &#183; <i>{wotd[1]}</i><br>" + wotd[2]
	timestamp = email_utils.format_datetime(datetime.now())
	return f"""		<item>
			<title>{title}</title>
			<description><![CDATA[{description}]]></description>
			<pubDate>{timestamp}</pubDate>
		</item>
"""

def get_wotd_rss(wotd_content):
	head = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
	<channel>
		<title>Lyre's Dictionary Word of the Day</title>
		<link>http://www.lyresdictionary.com</link>
		<description>Selections from the Lyre's Dictionary word feeds</description>

"""

	tail = """	</channel>
</rss>
"""

	return head + "".join(wotd_content) + tail

# Generate Base RSS --------------------------

def generate_base_wotd_content():
	wotds = [
		["bibible", "adjective", "able to be drunk"],
		["gymnasis", "noun", "the act or state of training"],
		["smeeker", "noun", "one who fumigates"],
		["futurarium", "noun", "a place for the future"],
		["aristophile", "noun", "one who has a love of the best things"],
		["kimen", "verb", "to make fine, beautiful"],
		["rephrame", "noun", "that which is told again"]
	]

	wotd_content = []
	for wotd in wotds:
		wotd_content.append(format_wotd_rss(wotd))

	return get_wotd_rss(wotd_content)

def make_base_wotd_rss(root_path):
	content = generate_base_wotd_content()
	wotd_path = root_path + "wotd-feed-base.xml"

	f = open(wotd_path, "w")
	f.write(content)
	f.close()

# Update the RSS ----------------------------

def update_wotd_rss(root_path, wotd):
	print("> Updating RSS")
	wotd_path = root_path + "/wotd-feed.xml"

	with open(wotd_path) as wotd_data:
		wotd_string = wotd_data.read()
		matches = re.findall("<item>.*?<\\/item>", wotd_string, re.DOTALL)

	if len(matches) >= 7:
		matches = matches[:6]

	title = f"<b>{wotd[0]}</b> &#183; <i>{wotd[1]}</i>"
	description = wotd[2]
	formatted = format_wotd_rss(wotd)

	wotd_content = [formatted] + matches

	content = get_wotd_rss(wotd_content)

	f = open(wotd_path, "w")
	f.write(content)
	f.close()

# Interface ==================================

if __name__ == '__main__' and len(sys.argv) > 0:

	root_path = "./"
	mode = "update"

    # Get args
	try:
		opts, params = getopt.getopt(sys.argv[1:], "bp:", ["base", "path"])
	except getopt.GetoptError:
		sys.exit(2)

	for opt, arg in opts:
		if opt in ["-b", "--base"]:
			mode = "base"
		elif opt in ["-p", "--path"]:
			root_path = arg

# Clean path
if root_path.endswith("/"):
	root_path = root_path[:-1]

# Update the WOTD
if mode == "update":
	wotd = get_wotd()
	update_site(root_path, wotd)
	update_wotd_rss(root_path, wotd)

# Generate a base WOTD RSS file
elif mode == "base":
	make_base_wotd_rss(root_path)
