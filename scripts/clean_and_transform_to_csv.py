# This file is for cleaning the columns which we don't need for our analysis.
# At the end our data will be transformed to a csv file.
import pandas as pd
import json

# define directory paths and filenames
directory_name_only_politic_file = "./data/only_politic_file/"
file = "only_political_articles_new_content.json"
new_file = "only_political_articles.csv"

# Reading the json file and removing the columns that we don't need.
with open(directory_name_only_politic_file + file, "r") as final:
    data = json.load(final)
    for line in data:
        line.pop('published_date')
        line.pop('article_url')
        line.pop('title')
        line.pop('author')
        line.pop('contents')
        line.pop('type')
        line.pop('source')
        line.pop('content')

# Converting the data into a dataframe and then saving it as a csv file.
df = pd.DataFrame(data)
df.to_csv(directory_name_only_politic_file + new_file)
