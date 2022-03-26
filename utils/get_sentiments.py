

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
"""
def lexicon_sentiment(lexicon_dt, text_str):
  '''
  Given a lexicon dict[word]=sentiment and a string
  Return a sentiment ('pos'|'neg') and a polarity (-1.0 to 1.0)
  '''

  word_ls = text_str.split()
  text_polarity = 0

  for aword in word_ls:
    word_sentiment = lexicon_dt.get(aword)
    if word_sentiment != None: #lexicon_dt.get(aword) != None:
      # print(f'Word: {aword} Polarity: {word_sentiment}')
      text_polarity += word_sentiment # lexicon_dt[aword]

  if text_polarity > 0.0:
    text_sentiment = 'pos'
  else:
    text_sentiment = 'neg'
  
  # Return tuple of polarity ('positive'|'negative') and sentiment float value (-1.0 to 1.0)
  return text_sentiment, round(text_polarity, 4)

# Test
test_str = "I love enjoying the great outdoors!"
test_tp = lexicon_sentiment(lexicon_jockersrinker_dt, test_str)
print(f'The Sentence: {test_str}\n\n  Sentiment: {test_tp[0]}\n\n  Polarity:  {test_tp[1]}')

""";

# --------------------------------------------------
"""
def pattern_discrete2continous_sentiment(text):
  '''
  Given a plain text string, give it to
    Stanford Stanza (OpenNLP) to calculate sentiment for each word on a 3 point scale 0-2
  Return a sentiment value for the entire sentence (sum of word sentiments/log(len of sentence)) 
    that approximates a normal distribution for all values
    In order to get more fine grained measure of overall Sentence sentiment
    Sentiment values will be Normalized/Standardized so absolute precision is not required
  '''
  text_sentiment_total = 0.
  text_ls = text.split()
  text_len = len(text_ls)
  for aword in text_ls:
    text_sentiment_total += pattern_sa(str(aword))[0]
  text_sentiment_norm = text_sentiment_total/(np.log(text_len)+0.01)

  return text_sentiment_norm
""";

# --------------------------------------------------
def sent2vader_comp(asent_str):
  '''
  Given a Sentence as a text string
  Return a Sentiment = sum(VADER sentiments for each word)
  '''

  words_ls = asent_str.split()
  sent_sentiment_fl = 0.0

  for j, atest_word in enumerate(words_ls):
    sent_sentiment_fl += vader_analyzer.polarity_scores(atest_word.lower())['compound']

  return sent_sentiment_fl

# --------------------------------------------------
def sent2textblob(asent_str):
  '''
  Given a Sentence as a text string
  Return a Sentiment = sum(TextBlob sentiments for each word)
  '''

  words_ls = asent_str.split()
  sent_sentiment_fl = 0.0

  for j, atest_word in enumerate(words_ls):
    sent_sentiment_fl += TextBlob(atest_word.lower()).sentiment.polarity

  return sent_sentiment_fl

# --------------------------------------------------
def flair_sentiment(asent_str):
  '''
  Given a text string, get sentiment str using Flair (e.g. 'NEGATIVE (0.9243)') 
  Return a floating point -1.0 to 1.0
  '''
  sentence = Sentence(asent_str)
  classifier.predict(sentence)

  # print(f'   Sentence: {atest_str}')
  sentiment_str = str(sentence.labels[0])

  polarity_str, polarity_val_str = sentiment_str.split()

  pol_str = polarity_str.strip()
  if pol_str.strip() == "POSITIVE":
    sign_val = 1.0
  elif pol_str.strip() == "NEGATIVE":
    sign_val = -1.0
  else:
    print(f'ERROR: Illegal value for polarity_str: {pol_str}')

  pol_val_str = polarity_val_str.strip()
  pol_val_str = pol_val_str[1:-1]
  pol_fl = sign_val * float(pol_val_str)

  return pol_fl

# --------------------------------------------------
def stanza_discrete2continous_sentiment(text):
  '''
  Given a plain text string, give it to
    Stanford Stanza (OpenNLP) to calculate sentiment for each word on a 3 point scale 0-2
  Return a sentiment value for the entire sentence (sum of word sentiments/log(len of sentence)) 
    that approximates a normal distribution for all values
    In order to get more fine grained measure of overall Sentence sentiment
    Sentiment values will be Normalized/Standardized so absolute precision is not required
  '''
  text_sentiment_tot = 0.
  text_ls = text.split()
  text_len = len(text_ls)
  for aword in text_ls:
    adoc = nlp(aword)
    for i, sentence in enumerate(adoc.sentences):
      text_sentiment_tot += float(sentence.sentiment)
  text_sentiment_norm = text_sentiment_tot/(np.log(text_len)+0.1)

  return text_sentiment_norm

# --------------------------------------------------
def ml_metrics(model,x,y):
  # https://www.kaggle.com/aditya6040/7-models-on-imdb-dataset-best-score-88-2/notebook
  y_pred = model.predict(x)
  acc = accuracy_score(y, y_pred)
  f1=f1_score(y, y_pred)
  cm=confusion_matrix(y, y_pred)
  report=classification_report(y,y_pred)
  plt.figure(figsize=(4,4))
  sns.heatmap(cm,annot=True,cmap='Blues',xticklabels=[0,1],fmt='d',annot_kws={"fontsize":19})
  plt.xlabel("Predicted",fontsize=16)
  plt.ylabel("Actual",fontsize=16)
  plt.show()
  print("\nAccuracy: ",round(acc,2))
  print("\nF1 Score: ",round(f1,2))
  print("\nConfusion Matrix: \n",cm) # Comment out?
  print("\nReport:",report)

# --------------------------------------------------
def lexicon_metrics(y, y_pred):
  acc = accuracy_score(y, y_pred)
  f1=f1_score(y, y_pred)
  cm=confusion_matrix(y, y_pred)
  report=classification_report(y, y_pred)
  plt.figure(figsize=(4,4))
  sns.heatmap(cm,annot=True,cmap='Blues',xticklabels=[0,1],fmt='d',annot_kws={"fontsize":19})
  plt.xlabel("Predicted",fontsize=16)
  plt.ylabel("Actual",fontsize=16)
  plt.show()
  print("\nAccuracy: ",round(acc,2))
  print("\nF1 Score: ",round(f1,2))
  print("\nConfusion Matrix: \n",cm) # Comment out?
  print("\nReport:",report)

# --------------------------------------------------
def labelscore2fl(labelscore_sentiment_ls, sa_model):
  '''
  Given the list of dict returned by RoBERTa15lg
  Return a floating point value for sentiment
  '''
  sentiment_fl = -99.99

  label_str = labelscore_sentiment_ls[0]['label'].strip().lower()
  score_fl = float(labelscore_sentiment_ls[0]['score'])

  # For lablels POSTIVE/POS, NEGATIVE/NEG
  if label_str in ['positive','pos']:
    sentiment_fl = score_fl
  elif label_str in ['negative','neg']:
    sentiment_fl = -1.0 * (score_fl)
  elif label_str in ['neutral','neu']:
    sentiment_fl = 0

  # For Labels 'n Stars' where n=[1..5]
  elif label_str == '1 star':
    sentiment_fl = score_fl
  elif label_str == '2 stars':
    sentiment_fl = 1.0 + score_fl
  elif label_str == '3 stars':
    sentiment_fl = 2.0 + score_fl
  elif label_str == '4 stars':
    sentiment_fl = 3.0 + score_fl
  elif label_str == '5 stars':
    sentiment_fl = 4.0 + score_fl

  # Else ERROR on illegal Label value
  else:
    print(f'ERROR: Illegal value for RoBERTa Label: {label_str}')

  return sentiment_fl

# --------------------------------------------------
def logitstensor2sentiment(hugseqclass_output):
  '''
  Given a Huggingface SequenceClassifierOutput logits tensor
  Return Sentiment and assoc softmax probability values
  '''

  text_smax_ls_ls = hugseqclass_output.logits.softmax(dim=-1).tolist()
  text_smax_ls = text_smax_ls_ls[0]
  # print(type(text_smax_ls[0]))
  # print(f'  sMAX: {text_smax_ls}')
  max_val = max(text_smax_ls)            # Probability based upon logits %
  max_indx = text_smax_ls.index(max_val) # Sentiment (starting from 0 up)
  val_scale = len(text_smax_ls)
  # print(f'   MAX: {max_val} at indx={max_indx}')

  return max_indx, val_scale, max_val



# --------------------------------------------------