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
  
  