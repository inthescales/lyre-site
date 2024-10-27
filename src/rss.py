import datetime

from email import utils as email_utils

def generate_blog_rss(metas):
	output = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
	<channel>
		<title>Lyre's Dictionary</title>
		<link>http://www.lyresdictionary.com</link>
		<description>Lyre's Dictionary Blog</description>

"""

	metas = sorted(metas, key=lambda x: (x["date"][0], x["date"][1], x["date"][2]), reverse=True)
	for meta in metas:
		title = meta["title"]
		link = "http://www.lyresdictionary.com/blog/" + meta["slug"]
		description = meta["description"]
		date = datetime.datetime(meta["date"][0], meta["date"][1], meta["date"][2])
		timestamp = email_utils.format_datetime(date)
		output += f"""		<item>
			<title>{title}</title>
			<link>{link}</link>
			<description>{description}</description>
			<pubDate>{timestamp}</pubDate>
		</item>
"""

	output += """	</channel>
</rss>
"""

	return output
