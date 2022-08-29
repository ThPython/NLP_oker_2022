# conda install -c conda-forge vadersentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

texte = [
  'This apple is very good.',
  'This apple is bullshit.',
  'This pear is bullshit.',
]

apple_apple = \
'''
  This apple is very good. This apple is bullshit. 
'''

apple_pear = \
'''
  This apple is very good. This pear is bullshit. 
'''

for text in texte:
  print('vader.analyser:', text, analyser.polarity_scores(text))

print('vader.analyser:', apple_apple, analyser.polarity_scores(apple_apple))
print('vader.analyser:', apple_pear, analyser.polarity_scores(apple_pear))


''' Output:
vader.analyser: This apple is very good. {'neg': 0.0, 'neu': 0.556, 'pos': 0.444, 'compound': 0.4927}
vader.analyser: This apple is bullshit. {'neg': 0.559, 'neu': 0.441, 'pos': 0.0, 'compound': -0.5859}
vader.analyser: This pear is bullshit. {'neg': 0.559, 'neu': 0.441, 'pos': 0.0, 'compound': -0.5859}
vader.analyser: 
  This apple is very good. This apple is bullshit. 
 {'neg': 0.272, 'neu': 0.5, 'pos': 0.228, 'compound': -0.1548}
vader.analyser: 
  This apple is very good. This pear is bullshit. 
 {'neg': 0.272, 'neu': 0.5, 'pos': 0.228, 'compound': -0.1548}
'''