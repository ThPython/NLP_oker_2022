# This file retrieve lines from our general .jl file and writes 8 new smaller files.
import pandas as pd

# define document range (max lines to write inside new file) and counter
document_range = 100000
document_counter = 1
# total lines variable with value which we get from our count_lines.py file
total_lines_of_file = 728626

# The following code is reading the file line by line and storing the lines in a list.
# The list is then converted to a dataframe and stored as a csv file.
# The csv file is stored in the data folder.
# The csv file is named as 100000_lines_1.csv, 100000_lines_2.csv, 100000_lines_3.csv, 100000_lines_4.csv,
# 100000_lines_5.csv, 100000_lines_6.csv, 100000_lines_7.csv, 100000_lines_8.csv
with open("./TREC_Washington_Post_collection.v4.jl") as f1:
    head = []
    counter = 0

    while True:
        next_line = next(f1)
        head.append(next_line)
        counter += 1

        if counter % document_range == 0:
            df = pd.DataFrame(head)
            df.to_csv('./data/general_content_files/100000_lines_' + str(document_counter) + '.csv', index=False)
            head = []
            document_counter += 1

        if counter % total_lines_of_file == 0:
            df = pd.DataFrame(head)
            df.to_csv('./data/general_content_files/100000_lines_' + str(document_counter) + '.csv', index=False)
            head = []
            document_counter += 1
