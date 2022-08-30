import json
import os

# define directory path
directory_name = "./data/only_chosen_year/"

# Create a list of all files inside the directory.
filenames = os.listdir(directory_name)

# sort filenames
filenames.sort()

# Iterating through the list of files in the directory and calling the read_and_write_files function on each file.
for file in filenames:
    with open(directory_name + file, "r") as fp:
        data = json.load(fp)
        print("Anzahl Artikel: ", file, len(data))

# total articles in 2016: 101212
# total articles in 2017: 54279
