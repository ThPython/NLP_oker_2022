# This file is for extracting contents from our final only_political_articles.json file.
# For our analysis with VADER we need the contents as a string inside a new key (column).
import json

# define directory paths and filenames
directory_name_only_politic_file = "./data/only_politic_file/"
file = "only_political_articles.json"
new_file = "only_political_articles_new_content.json"

# The above code is taking the contents of the json file and creating a new key called "new_content" and the value of
# that key is the contents of the json file.
with open(directory_name_only_politic_file + file, "r") as final:
    data = json.load(final)

    for line in data:
        new_content_list = []
        for content in line.get("contents", {}):
            if content:
                if content.get("type", "") == "sanitized_html":
                    content_value = content.get("content", "")
                    new_content_list.append(content_value)
        line["new_content"] = " ".join(new_content_list)

# Writing the new data to a new file.
with open(directory_name_only_politic_file + new_file, "w") as final:
    json.dump(data, final)
