#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd

# header = ['id', 'date', 'new_content', 'scores', 'compound', 'comp_score']

dic_word_comp = {}

'''
Liste an Wörtern für ein dictionary:
Groß- und Kleinschreibung und Singular und Plural
Donald
Barack
Trump
Obama
President (gross oder klein) Plural/Singular
Republican/s
Democratic/s
'''

key_woerter = [' donald ', ' trump', ' barack ', ' obama ', ' president ', 
  ' republican ', ' republicans ', ' democratic ', ' democratics ']


def do_content(content):
  found = []
  content = content.lower()
  for wort in key_woerter:
    if wort in content:
      found.append(wort)
  return(found)
  
  
def do_article(datei):
  global dic_word_comp
  dic_word_comp.clear()
  to_skip = []
  # count = 0
  positiv, negativ = (0,0)
  df = pd.read_csv(datei)
  for index, row in df.iterrows():
    # count += 1
    # if count > 3: break
    found = do_content(row['new_content'])
    if len(found) == 0:
       to_skip.append(index)
       continue
    compound = row['compound']
    if compound > 0: positiv += 1
    else: negativ +=1
    str1 = "{:s}, {:s}, {:s}, {:s}".format(row['id'], row['date'], str(row['compound']), row['date'][:4])
    print(str1)
    str2 = "  {:02d} key_woerter gefunden: {:s}".format(len(found), str(found))
    print(str2)
    compound = row['compound']
    praefix = 'P' if compound >= 0 else 'N' 
    sort_key = "  {:02d}_{:s}{:+f}".format(len(found), praefix, compound)
    dic_word_comp[sort_key] = str1
  return(positiv, negativ, len(to_skip))
  
  
def do_reorder(jahr):
  print('\nArtikel aus {:s}, sortiert nach Anzahl Key-Woerten absteigend, compound absteigend:'.format(jahr))  
  keys = dic_word_comp.keys()
  sorted_keys = sorted(keys, reverse=True)
  sorted_dic_word_comp = {}
  for key in sorted_keys:
    sorted_dic_word_comp[key] = dic_word_comp[key]
  for key, data in sorted_dic_word_comp.items():
    print(key, ":", data)
  

if __name__ == "__main__":
  print("hier ist", str(sys.argv))
  print('\n--------------- f u e r   2 0 1 6 ---------------')
  pos_2016, neg_2016, skipped_2016 = do_article('./df_2016_descend.csv')
  do_reorder('2016')
  print('\n--------------- f u e r   2 0 1 7 ---------------')
  pos_2017, neg_2017, skipped_2017 = do_article('./df_2017_descend.csv')
  do_reorder('2017')
  print('\n--------------- E n d e   2 0 1 7 ---------------')  
  sum_2016 = pos_2016 + neg_2016; pos_proz_2016 = int((pos_2016*100)/sum_2016)
  sum_2016_total = sum_2016 + skipped_2016
  sum_2017 = pos_2017 + neg_2017; pos_proz_2017 = int((pos_2017*100)/sum_2017)
  sum_2017_total = sum_2017 + skipped_2017
  print("2016: von {:d} Artikeln waren {:d} ({:d}%) positiv und {:d} ({:d}%) negativ ({:d} skipped, total: {:d})". \
       format(sum_2016, pos_2016, pos_proz_2016, neg_2016, 100-pos_proz_2016, skipped_2016, sum_2016_total))
  print("2017: von {:d} Artikeln waren {:d} ({:d}%) positiv und {:d} ({:d}%) negativ ({:d} skipped, total: {:d}))". \
       format(sum_2017, pos_2017, pos_proz_2017, neg_2017, 100-pos_proz_2017, skipped_2017, sum_2017_total))
  
  