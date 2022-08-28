# polit_sent.py nimmt die von politSplitToYear.py erzeugten 2 Dateien als Eingabe und gibt verdichtete Daten aus:
.
.
.
c758046b36cbea162f559fff1ab39f18 2017-02-24T20:17:56Z -0.9998 2017
7d2a0432-ea4a-11e6-bf6f-301b6b443624 2017-02-04T00:28:20Z -0.9998 2017
2016: von 1908 Artikeln waren 1392 (72%) positiv und 516 (28%) negativ
2017: von 1368 Artikeln waren 999 (73%) positiv und 369 (27%) negativ
  
#  Alle benötigten Dateien liegen auf Sciebo, aufgrund der bereits unterschriebenen "Individual Application".
###

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd

# header = ['id', 'date', 'new_content', 'scores', 'compound', 'comp_score']
key_woerter = ['Trump', 'Biden']

def do_article(datei):

  positiv, negativ = (0,0)
  df = pd.read_csv(datei)
  # print(df)
  for index, row in df.iterrows():
    compound = row['compound']
    if compound > 0: positiv += 1
    else: negativ +=1
    print(row['id'], row['date'], row['compound'], row['date'][:4])
  return(positiv, negativ)
  

if __name__ == "__main__":
  print("hier ist", str(sys.argv))
  
  pos_2016, neg_2016 = do_article('./df_2016_descend.csv')
  pos_2017, neg_2017 = do_article('./df_2017_descend.csv')
  sum_2016 = pos_2016 + neg_2016; pos_proz_2016 = int((pos_2016*100)/sum_2016)
  sum_2017 = pos_2017 + neg_2017; pos_proz_2017 = int((pos_2017*100)/sum_2017)
  print("2016: von {:d} Artikeln waren {:d} ({:d}%) positiv und {:d} ({:d}%) negativ". \
       format(sum_2016, pos_2016, pos_proz_2016, neg_2016, 100-pos_proz_2016))
  print("2017: von {:d} Artikeln waren {:d} ({:d}%) positiv und {:d} ({:d}%) negativ". \
       format(sum_2017, pos_2017, pos_proz_2017, neg_2017, 100-pos_proz_2017))
  
  
