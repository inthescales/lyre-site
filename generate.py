import json
import os
import shutil

import markdown

import src.blog as blog
import src.meta as metadata
import src.rss as rss

print("> Generating site")

output_path = "./output"

if os.path.exists(output_path) and os.path.isdir(output_path):
    shutil.rmtree(output_path)

os.mkdir(output_path)

# Helpers ======================

# Substitude codes in page bodies
def process(data, title):
    if title != None:
        data = data.replace("%TITLE%", title + " - Lyre’s Dictionary")
    else:
        data = data.replace("%TITLE%", "Lyre’s Dictionary")
    return data

# MAIN =========================

print("> Reading templates")

header = None
footer = None
with open("./templates/header.html") as header_data, \
     open("./templates/footer.html") as footer_data:
     header = header_data.read()
     footer = footer_data.read()

if header == None:
    print("ERROR: Unable to read header template")
if footer == None:
    print("ERROR: Unable to read footer template")
if header == None or footer == None:
    exit(0)

print("> Generating pages")

page_files = os.listdir("./pages/")
for file in page_files:
    name = file.split(".")[0]

    with open("./pages/" + file, encoding='utf-8') as page_data:
        # Assemble data
        page_string = page_data.read()
        filename = file.split(".")[0]
        meta, body = metadata.parse_meta(filename, page_string)
        page_content = header + body + footer

        # Fill in templates
        title = None
        if "title" in meta:
            title = meta["title"]
        page_content = process(page_content, title=title)

        # Write

        if filename == "index":
            f = open(output_path + "/" + filename + ".html", "w")
        else:
            os.mkdir(output_path + "/" + filename)
            f = open(output_path + "/" + filename + "/index.html", "w")
        f.write(page_content)
        f.close()

print("> Generating blog posts")

post_metas = []

post_files = os.listdir("./blog/")
os.mkdir(output_path + "/blog/")
for file in post_files:
    if not file.endswith(".md"):
        continue

    name = file.split(".")[0]

    with open("./blog/" + file, encoding='utf-8') as post_data:
        # Assemble data
        post_string = post_data.read()
        filename = file.split(".")[0]
        meta, body = metadata.parse_meta(filename, post_string)
        body = blog.preprocess_post(meta["title"], body)
        body = markdown.markdown(body)
        meta["slug"] = filename
        meta["date"] = metadata.parse_post_date(filename)
        post_content = header + body + footer

        # Fill in templates
        post_content = process(post_content, title=meta["title"])

        # Write
        f = open(output_path + "/blog/" + filename + ".html", "w")
        f.write(post_content)
        f.close()

        # Add metadata to list
        post_metas.append(meta)

print("> Generating blog index")

# Generate page HTML
blog_index_content = header + blog.make_blog_index(post_metas) + footer
blog_index_content = process(blog_index_content, title="Blog")

# Write
f = open(output_path + "/blog/index.html", "w")
f.write(blog_index_content)
f.close()

print("> Copying assets")

shutil.copytree("./assets", output_path + "/assets")

# Move out favicons and WOTD RSS
shutil.copy(output_path + "/assets/images/favicon.ico", "./output/blog/")
shutil.move(output_path + "/assets/images/favicon.ico", "./output/")
shutil.move(output_path + "/assets/wotd-feed-base.xml", "./output/wotd-feed.xml")

print("> Generating blog rss")

rss_data = rss.generate_blog_rss(post_metas)
f = open(output_path + "/blog/feed.xml", "w")
f.write(rss_data)
f.close()


print("> Done generating")
