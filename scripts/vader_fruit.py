# conda install -c conda-forge vadersentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

texte1 = [
  'This apple is very good.',
  'This apple is bullshit.',
  'This pear is bullshit.',
  'This apple is very good. This apple is bullshit.',
  'This apple is very good. This pear is bullshit.' 
]

texte2 = [
  'Gentleman.',
  'No Gentleman.',
  'Real Gentleman.',
  'No real Gentleman.',
  'Dumbass.',
  'No Dumbass.',
  'John is a Dumbass.',
  'John is not a Dumbass.',
  'John is no Dumbass.',
  'It is not the case that John is a Dumbass',
  'John is not really a dumbass',
  'John not really is a dumbass',
  'Nobody is a dumbass.',
  'Nobody dumbass',
  'Nobody no dumbass',
  'No Nobody dumbass',
  'No this Nobody dumbass',
  'Jim believes that John is a dumbass',
  'Jim does not believe that John is a dumbass',
  'Jim does not believe that John is no dumbass',
  'Jim does not believe that John is not a dumbass',
  'It is not true that john is no dumbass',
  'It is not true that john is not a dumbass',
  'It is false that john is no dumbass',
  'It is wrong that john is no dumbass',
  'John is never a dumbass',
  'John is perhaps a dumbass'
]

all_texte = [texte1, texte2]

  
for texte in all_texte:
  for text in texte:
    print('vader:', text, analyser.polarity_scores(text))
  print()
  
  
''' Output:
vader: This apple is very good. {'neg': 0.0, 'neu': 0.556, 'pos': 0.444, 'compound': 0.4927}
vader: This apple is bullshit. {'neg': 0.559, 'neu': 0.441, 'pos': 0.0, 'compound': -0.5859}
vader: This pear is bullshit. {'neg': 0.559, 'neu': 0.441, 'pos': 0.0, 'compound': -0.5859}
vader: This apple is very good. This apple is bullshit. {'neg': 0.272, 'neu': 0.5, 'pos': 0.228, 'compound': -0.1548}
vader: This apple is very good. This pear is bullshit. {'neg': 0.272, 'neu': 0.5, 'pos': 0.228, 'compound': -0.1548}

vader: Gentleman. {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
vader: No Gentleman. {'neg': 0.688, 'neu': 0.312, 'pos': 0.0, 'compound': -0.296}
vader: Real Gentleman. {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}
vader: No real Gentleman. {'neg': 0.524, 'neu': 0.476, 'pos': 0.0, 'compound': -0.296}
vader: Dumbass. {'neg': 1.0, 'neu': 0.0, 'pos': 0.0, 'compound': -0.5574}
vader: No Dumbass. {'neg': 0.0, 'neu': 0.255, 'pos': 0.745, 'compound': 0.4449}
vader: John is a Dumbass. {'neg': 0.545, 'neu': 0.455, 'pos': 0.0, 'compound': -0.5574}
vader: John is not a Dumbass. {'neg': 0.0, 'neu': 0.578, 'pos': 0.422, 'compound': 0.4449}
vader: John is no Dumbass. {'neg': 0.0, 'neu': 0.506, 'pos': 0.494, 'compound': 0.4449}
vader: It is not the case that John is a Dumbass {'neg': 0.286, 'neu': 0.714, 'pos': 0.0, 'compound': -0.5574}
vader: John is not really a dumbass {'neg': 0.0, 'neu': 0.615, 'pos': 0.385, 'compound': 0.4819}
vader: John not really is a dumbass {'neg': 0.436, 'neu': 0.564, 'pos': 0.0, 'compound': -0.5945}
vader: Nobody is a dumbass. {'neg': 0.545, 'neu': 0.455, 'pos': 0.0, 'compound': -0.5574}
vader: Nobody dumbass {'neg': 0.783, 'neu': 0.217, 'pos': 0.0, 'compound': -0.5574}
vader: Nobody no dumbass {'neg': 0.0, 'neu': 0.406, 'pos': 0.594, 'compound': 0.4449}
vader: No Nobody dumbass {'neg': 0.359, 'neu': 0.163, 'pos': 0.477, 'compound': 0.1838}
vader: No this Nobody dumbass {'neg': 0.744, 'neu': 0.256, 'pos': 0.0, 'compound': -0.7003}
vader: Jim believes that John is a dumbass {'neg': 0.375, 'neu': 0.625, 'pos': 0.0, 'compound': -0.5574}
vader: Jim does not believe that John is a dumbass {'neg': 0.31, 'neu': 0.69, 'pos': 0.0, 'compound': -0.5574}
vader: Jim does not believe that John is no dumbass {'neg': 0.0, 'neu': 0.732, 'pos': 0.268, 'compound': 0.4449}
vader: Jim does not believe that John is not a dumbass {'neg': 0.0, 'neu': 0.755, 'pos': 0.245, 'compound': 0.4449}
vader: It is not true that john is no dumbass {'neg': 0.19, 'neu': 0.571, 'pos': 0.239, 'compound': 0.1511}
vader: It is not true that john is not a dumbass {'neg': 0.176, 'neu': 0.604, 'pos': 0.221, 'compound': 0.1511}
vader: It is false that john is no dumbass {'neg': 0.0, 'neu': 0.705, 'pos': 0.295, 'compound': 0.4449}
vader: It is wrong that john is no dumbass {'neg': 0.258, 'neu': 0.499, 'pos': 0.243, 'compound': -0.0454}
vader: John is never a dumbass {'neg': 0.0, 'neu': 0.578, 'pos': 0.422, 'compound': 0.4449}
vader: John is perhaps a dumbass {'neg': 0.474, 'neu': 0.526, 'pos': 0.0, 'compound': -0.5574}
'''