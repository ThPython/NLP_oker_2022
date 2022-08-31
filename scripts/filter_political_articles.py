# This file iterates through all files in our new directory with articles from 2016 and 2017 and create a new file with
# only political articles.
import json
import os

# define directory paths and filenames
directory_name_only_chosen_years = "./data/only_chosen_year/"
directory_name_only_politic_file = "./data/only_politic_file/"
document_counter = 1

# Create a list of all files inside the directory.
filenames = os.listdir(directory_name_only_chosen_years)

# Sort filenames starting from first file
filenames.sort()

# list of the filtered articles
list_with_political_articles = []


# Iterating through all files in the directory and then iterating through all articles in the file.
# Then it is iterating through all contents of the article and if the content is "Politics" it is appending it to the
# list. Change the string "Politics" to another if you are searching for another content type.
def read_and_write_files(file):
    with open(directory_name_only_chosen_years + file, "r") as final:
        data = json.load(final)

    for line in data:
        for content in line["contents"]:
            if content:
                content_value = content.get("content", "")
                if content_value == "Politics":
                    list_with_political_articles.append(line)
                    break


# Creating a JSON file with the list of political articles.
def create_file_with_filtered_articles(list_with_articles):
    with open(directory_name_only_politic_file + "only_political_articles" + '.json', "w") as final:
        json.dump(list_with_articles, final)


# Iterating through the list of files in the directory and calling the read_and_write_files function on each file.
for file in filenames:
    read_and_write_files(file)
    document_counter += 1

# Creating a JSON file with the list of political articles.
create_file_with_filtered_articles(list_with_political_articles)

