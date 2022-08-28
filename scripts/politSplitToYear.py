import pandas as pd

header = ['id', 'date', 'new_content', 'scores', 'compound', 'comp_score']

list_2016 = []
list_2017 = []
list_false = []

df_polit_sent = pd.read_csv('./only_political_articles_with_scores.csv')
df_polit_sent = df_polit_sent.reset_index()  # index zuruecksetzen
for index, row in df_polit_sent.iterrows():
  print(row['id'], row['date'], row['compound'], row['date'][:4])
  if (row['date'][:4]=='2016'):
    list_2016.append(row)
  elif (row['date'][:4]=='2017'):
    list_2017.append(row)
  else:
    list_false.append(row)
    
print("Anzahl rows:", len(df_polit_sent.index))
print("2016: {:d}, 2017: {:d}, andere: {:d}".format(len(list_2016), len(list_2017), len(list_false)))

df_2016 = pd.DataFrame(list_2016, columns=header)
df_2017 = pd.DataFrame(list_2017, columns=header)

df_2016.sort_values(by=['compound'], ignore_index=True, inplace=True, ascending=0)
df_2017.sort_values(by=['compound'], ignore_index=True, inplace=True, ascending=0)

df_2016.to_csv('./df_2016_descend.csv', index=False)
df_2017.to_csv('./df_2017_descend.csv', index=False)