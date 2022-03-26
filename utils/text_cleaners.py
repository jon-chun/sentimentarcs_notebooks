import global_vars

def text2lemmas(comment, lowercase, remove_stopwords):
    if lowercase:
        comment = comment.lower()
    comment = nlp(comment)
    lemmatized = list()
    for word in comment:
        lemma = word.lemma_.strip()
        if lemma:
            if not remove_stopwords or (remove_stopwords and lemma not in stopwords_ls):
                lemmatized.append(lemma)
    return " ".join(lemmatized)

# --------------------------------------------------
def text_str2sents(text_str, pysbd_only=False):
  '''
  Given a long text string (e.g. a novel) and pysbd_only flag
  Return a list of every Sentence defined by (a) 2+ newlines as paragraph separators, 
                                            (b) SpaCy+PySBD Pipeline, and 
                                            (c) Optionally, NLTK sentence tokenizer
  '''

  parags_ls = []
  sents_ls = []

  from pysbd.utils import PySBDFactory
  nlp = spacy.blank('en')
  nlp.add_pipe(PySBDFactory(nlp))

  print(f'BEFORE stripping out headings len: {len(text_str)}')

  parags_ls = re.split(r'[\n]{2,}', text_str)

  parags_ls = [x.strip() for x in parags_ls]

  # Strip out non-printing characters
  parags_ls = [re.sub(f'[^{re.escape(string.printable)}]', '', x) for x in parags_ls]

  # Filter out empty lines Paragraphs
  parags_ls = [x for x in parags_ls if (len(x.strip()) >= global_vars.MIN_PARAG_LEN)]

  print(f'   Parag count before processing sents: {len(parags_ls)}')
  # FIRST PASS at Sentence Tokenization with PySBD

  for i, aparag in enumerate(parags_ls):
  

    aparag_nonl = re.sub('[\n]{1,}', ' ', aparag)
    doc = nlp(aparag_nonl)
    aparag_sents_pysbd_ls = list(doc.sents)
    print(f'pysbd found {len(aparag_sents_pysbd_ls)} Sentences in Paragraph #{i}')

    # Strip ofaparag_sents_pysbd_lsf whitespace from Sentences
    aparag_sents_pysbd_ls = [str(x).strip() for x in aparag_sents_pysbd_ls]

    # Filter out empty line Sentences
    aparag_sents_pysbd_ls = [x for x in aparag_sents_pysbd_ls if (len(x.strip()) > global_vars.MIN_SENT_LEN)]

    print(f'      {len(aparag_sents_pysbd_ls)} Sentences remain after cleaning')

    sents_ls += aparag_sents_pysbd_ls

  # (OPTIONAL) SECOND PASS as Sentence Tokenization with NLTK
  if pysbd_only == True:
    # Only do one pass of SpaCy/PySBD Sentence tokenizer
    # sents_ls += aparag_sents_pysbd_ls
    pass
  else:
    # Do second NLTK pass at Sentence tokenization if pysbd_only == False
    # Do second pass, tokenize again with NLTK to catch any Sentence tokenization missed by PySBD
    # corpus_sents_all_nltk_ls = []
    # sents_ls = []
    # aparag_sents_nltk_ls = []
    aparag_sents_pysbd_ls = deepcopy(sents_ls)
    sents_ls = []
    for asent in aparag_sents_pysbd_ls:
      print(f'Processing asent: {asent}')
      aparag_sents_nltk_ls = []
      aparag_sents_nltk_ls = sent_tokenize(asent)

      # Strip off whitespace from Sentences
      aparag_sents_nltk_ls = [str(x).strip() for x in aparag_sents_nltk_ls]

      # Filter out empty line Sentences
      aparag_sents_nltk_ls = [x for x in aparag_sents_nltk_ls if (len(x.strip()) > global_vars.MIN_SENT_LEN)]

      # corpus_sents_all_second_ls += aparag_sents_nltk_ls

      sents_ls += aparag_sents_nltk_ls

  print(f'About to return sents_ls with len = {len(sents_ls)}')
  
  return sents_ls

# --------------------------------------------------
def textfile2df(fullpath_str):
  '''
  Given a full path to a *.txt file
  Return a DataFrame with one Sentence per row
  '''

  import pandas as pd
  
  textfile_df = pd.DataFrame()

  with open(fullpath_str,'r') as fp:
    content_str = fp.read() # .replace('\n',' ')

  sents_ls = text_str2sents(content_str)

  textfile_df['text_raw'] = pd.Series(sents_ls)

  return textfile_df

# --------------------------------------------------
def emojis2text(atext):
  for emot, text_desc in UNICODE_EMOJI.items():
    atext = atext.replace(emot, ' '.join(text_desc.replace(",", "").split()))

  atext = atext.replace('_', ' ').replace(':','')

  return atext

# --------------------------------------------------
def all_emos2text(atext):
  '''
  Given a text string with embedded emojis and/or emoticons
  Return a expanded text string with all emojis/emoticons translated into text
  '''

  # First, convert emoticons to text
  for emot, text_desc in EMOTICONS_EMO.items():
    atext = atext.replace(emot, ' ' + ' '.join(text_desc.replace(",", " ").split()))

  # Second, convert emojis to text
  for emot, text_desc in UNICODE_EMOJI.items():
    atext = atext.replace(emot, ' ' + ' '.join(text_desc.replace(",", " ").split()))

  atext = re.sub(r':([A-Za-z_]*):',r'\1',atext)
  # atext = re.sub(r'([\w]+)([_])([\w]+)',r'\1 \3',atext)
  atext = re.sub(r'_', ' ', atext)
  atext = ' '.join(atext.split())

  return atext

# --------------------------------------------------
def expand_slang(astring):
  words_ls = []
  words_expanded_ls = []
  slang_words = global_vars.SLANG_DT.keys()

  words_ls = astring.split()
  for aword in words_ls:
    if aword.lower() in slang_words:
      words_expanded_ls.append(global_vars.SLANG_DT[aword.lower()])
    else:
      words_expanded_ls.append(aword.lower())

  # abbreviations[word.lower()] if word.lower() in abbreviations.keys() else word

  astring_expanded = ' '.join(words_expanded_ls)

  return astring_expanded 

# --------------------------------------------------
def clean_text(text_df, text_col, text_type='normal'): 
  '''
  Given a DataFrame with a Text Column of raw text of type (formal, informal, tweet)
  Return a Series of clean texts
  '''

  text_clean_ser = pd.Series()

  # Extra processing steps for 'informal' and 'tweet' types of text
  if text_type in ['email', 'tweet']:

    # Remove URLs
    text_clean_ser = hero.remove_urls(text_df[text_col])

    # Emoticons and then Emojis to Text
    text_clean_ser = text_clean_ser.apply(lambda x : all_emos2text(x))

    # Expand Slang/Abbr
    text_clean_ser = text_clean_ser.apply(lambda x : expand_slang(x))

  else:

    text_clean_ser = text_df[text_col]


  # Expand Contractions
  text_clean_ser = text_clean_ser.apply(lambda x : contractions.fix(x))

  # Clean text: lowercase, remove punctuation/numbers, etc
  # text_clean_ser = text_clean_ser.pipe(hero.clean, hero_pre_pipeline)
  text_clean_ser = hero.clean(text_clean_ser, pipeline = def_pipeline)

  return text_clean_ser

# --------------------------------------------------
def lemma_pipe(texts):
  '''
  Given a text string
  Return a text string with all tokens lemmatized using SpaCy pipe for speed
  Called by clean_text() with SpaCy Lemmatizer
  '''
  # https://prrao87.github.io/blog/spacy/nlp/performance/2020/05/02/spacy-multiprocess.html

  lemma_tokens = []
  # for doc in nlp.pipe(docs, batch_size=32, n_process=3, disable=["tagger", "parser", "ner"]):
  for doc in nlp.pipe(texts, batch_size=200, n_process=3, disable=["tagger", "parser", "ner"]):
    # lemma_tokens.append([str(tok.lemma_).lower() if tok.lemma_ != '-PRON-' else str(tok.orth_).lower() for tok in doc])
    temp_ls = [str(tok.lemma_).lower() if tok.lemma_ != '-PRON-' else str(tok.orth_).lower() for tok in doc]
    lemma_tokens.append(' '.join(temp_ls))

  return lemma_tokens