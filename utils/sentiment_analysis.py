

def get_lexsent_sentiment(asent_str, lexicon_dt):
  '''
  Given a Sentence in string form and a Lexicon Dictionary
  Return the Sentiment of the Sentence = Sum(Sentiment(all words))
  '''

  sent_sentiment = 0
  asent_str = str(asent_str)
  word_ls = asent_str.split()
  for aword in word_ls:
    word_sentiment = lexicon_dt.get(aword)
    if word_sentiment != None:
      sent_sentiment += float(word_sentiment)

  return sent_sentiment

# --------------------------------------------------

# --------------------------------------------------

# --------------------------------------------------

# --------------------------------------------------