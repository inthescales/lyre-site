import calendar

# Preprocessing for blog article bodies
def preprocess_post(title, body):
    # Append the title to the top of the post
    output = "<h1>" + title + "</h1>"

    output += body

    # Replace separators with a custom divider object
    output = output.replace("---", "<div class=\"divider\"></div>")

    return output

# Generates the body for the blog index page
def make_blog_index(metas):
    output = """
    <div>
    <h1 style=\"display: inline-block; vertical-align: middle;\">Blog Articles</h1>   &#183;  
    <a class=\"blog-rss\" style=\"display: inline-block; vertical-align: middle;\" href=\"http://www.lyresdictionary.com/blog/feed.xml\">RSS</a>
    </div>
    """

    output += "<ul class=\"blog-index\">"
    output += "<div style=\"height: 8px;\"></div>"

    metas = sorted(metas, key=lambda x: (x["date"][0], x["date"][1], x["date"][2]), reverse=True)
    for i in range(0, len(metas)):

        if i > 0:
            output += "<div class=\"blog-index-divider\"></div>"

        meta = metas[i]
        output += "<li>"
        output += "<a href=\"" + meta["slug"] + ".html\">" + meta["title"] + "</a>" + "  &#183;  <i>" + calendar.month_name[meta["date"][1]] + " " + str(meta["date"][0]) + "</i>"
        output += "<br>"
        output += meta["description"]
        output += "</li>"

    output += "</ul>"

    return output
