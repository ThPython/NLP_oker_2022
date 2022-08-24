# This file iterate through our files and then iterate through each line and then iterate through the list
# inside the "contents" column. The date inside an object inside this list is then written inside a new "date" column.
import pandas as pd
import json
import os

# define directory paths and filenames
directory_name_general = "./data/general_content_files/"
directory_name_with_dates = "./data/general_content_files_with_dates/"
document_counter = 1

# Create a list of all files inside the directory.
filenames = os.listdir(directory_name_general)

# Sort filenames starting from first file
filenames.sort()


# This function reads the csv files, extracts the date from the contents, and writes the json files with the date column
# :param file: the name of the file that you want to read from
def read_and_write_files(file):
    list_of_article_objects = []
    df = pd.read_csv(directory_name_general + file)

    for e in df["0"]:
        article_object = json.loads(e)
        for content in article_object["contents"]:
            if content:
                content_value = content.get("content", "")
                type_of_contents = content.get("type", "")
                if type_of_contents == "date":
                    article_object['date'] = content_value
                    break

        list_of_article_objects.append(article_object)

    with open(directory_name_with_dates + "with_dates" + str(document_counter) + '.json', "w") as final:
        json.dump(list_of_article_objects, final)

    # First we tried to create csv-files with pandas, but we had some issues with too long lines and because of this
    # we have chosen the json method.
    # df_with_dates = pd.DataFrame(list_of_article_objects, index=None)
    # df_with_dates.to_csv(directory_name_with_dates + "with_dates" + str(document_counter) + '.csv')


# Iterating through the list of files in the directory and calling the read_and_write_files function on each file.
for file in filenames:
    read_and_write_files(file)
    document_counter += 1

