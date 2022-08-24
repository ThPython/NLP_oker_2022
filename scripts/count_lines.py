# Counting the total number of lines in the .jl file.
# We need the total number of lines for our retrieve_lines.py file.
with open(r"./TREC_Washington_Post_collection.v4.jl", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)  # Total Lines 728626
