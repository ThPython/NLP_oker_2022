# This file iterate through our files and then iterate through each line. Every article which was published in 2016
# or 2017 (year variable) is written in a new file.
import json
import os

# define the year you want to extract, for our research 2016 or 2017
year = "2016"

# define directory paths and filenames
directory_name_with_dates = "./data/general_content_files_with_dates/"
directory_name_only_chosen_year = "./data/only_chosen_year/"
document_counter = 1

# Create a list of all files inside the directory.
filenames = os.listdir(directory_name_with_dates)

# Sort filenames starting from first file
filenames.sort()


# This function reads the json files, iterates through the lines and if our chosen year is inside the date column
# it will be appended to our list. At the end we get files with articles which were published on our chosen year.
# :param file: the name of the file that you want to read from
def read_and_write_files(file):
    list_of_article_objects = []

    with open(directory_name_with_dates + file, "r") as final:
        data = json.load(final)

    for line in data:
        if "date" in line.keys():
            if year in line["date"]:
                list_of_article_objects.append(line)

    with open(directory_name_only_chosen_year + "only_chosen_date" + str(document_counter) + "_" + year + '.json', "w") as final:
        json.dump(list_of_article_objects, final)


# Iterating through the list of files in the directory and calling the read_and_write_files function on each file.
for file in filenames:
    read_and_write_files(file)
    document_counter += 1

