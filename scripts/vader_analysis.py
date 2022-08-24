# import nltk # you need this import only if you want to download the vader lexicon
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

# run this only once. if you already have the vader_lexicon you do not need to run this.
# nltk.download('vader_lexicon')

# the sentiment intensity analyzer of vader
sid = SentimentIntensityAnalyzer()

# define directory paths and filename
directory_name_only_politic_file = "./data/only_politic_file/"
file = "only_political_articles.csv"
new_file = "only_political_articles_with_scores.csv"

# read csv file
df = pd.read_csv(directory_name_only_politic_file + file)

# adding scores and labels to dataframe
df['scores'] = df['new_content'].apply(lambda content: sid.polarity_scores(content))

# adding compound to dataframe
df['compound'] = df['scores'].apply(lambda score_dict: score_dict['compound'])

# adding the compound score to dataframe
df['comp_score'] = df['compound'].apply(lambda c: 'pos' if c >= 0 else 'neg')

# saving dataframe as csv file
df.to_csv(directory_name_only_politic_file + new_file, index=False)
