# Parses the header metadata from a page or post file into a dictionary
# Returns a two-element list containing the metadata and body
def parse_meta(name, text):
    sections = text.split("---")

    if len(sections) < 2:
        print("ERROR: Unexpected format in file '" + name + "'")
        exit(0)

    meta = {}
    for line in sections[1].split("\n"):
        if line == "":
            continue

        expression = line.split(": ")
        if not len(expression) == 2:
            exit(0)

        treated_value = expression[1]
        if treated_value[0] in ["\"", "'"] and treated_value[-1] in ["\"", "'"]:
            treated_value = treated_value[1:-1]
        meta[expression[0]] = treated_value

    body = "---".join(sections[2:])

    return [meta, body]

# Parse the date of a post from its filename
# Format is YYYY-M(M)-D(D)
def parse_post_date(name):
    split = name.split("-")
    if len(split) < 4:
        print("ERROR: post name '" + name + "' is misformatted")

    year = int(split[0])
    month = int(split[1])
    day = int(split[2])

    return [year, month, day]
