### politSplitToYear.py


Ad 1.) politSplitToYear.py
nimmt die Datei 'only_political_articles_with_scores.csv' als Eingabe und erzeugt daraus 2 Dateien:
a) df_2016_descend.csv    # Artikel für das Jahr 2016, absteigend nach 'compound' sortiert (1 bis -1)
b) df_2017_descend.csv    # Artikel für das Jahr 2017, absteigend nach 'compound' sortiert (1 bis -1)

Ad 2.) polit_sent.py
nimmt die von politSplitToYear.py erzeugten 2 Dateien als Eingabe und gibt verdichtete Daten aus:
.
.
.
c758046b36cbea162f559fff1ab39f18 2017-02-24T20:17:56Z -0.9998 2017
7d2a0432-ea4a-11e6-bf6f-301b6b443624 2017-02-04T00:28:20Z -0.9998 2017
2016: von 1908 Artikeln waren 1392 (72%) positiv und 516 (28%) negativ
2017: von 1368 Artikeln waren 999 (73%) positiv und 369 (27%) negativ
###

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
