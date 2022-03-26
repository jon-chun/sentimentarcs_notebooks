# Corpus Details
Corpus_Genre = ""
Corpus_Type = ""
Corpus_Number = ""

# Main Dictionary[Model_abbr] = Model_Full_Info
model_titles_dt = {}
corpus_titles_ls = []
    
# Main Dictionary[Title_abbr] = Text_Full_Title_by_Author
corpus_titles_dt = {}
corpus_texts_dt = {}

# Main Dictionary[Family] = [List of Models]
models_ensemble_dt = {}

# Currently Running Notebook
NotebookModels = ""

# Dictionary of Python Sentiment Lexicons
lexicons_dt = {}

# SentimentArcs Filenames and Directory Structure
FNAME_SENTIMENT_RAW = ""
SUBDIR_SENTIMENTARCS = ""

SUBDIR_TEXT_RAW = ""
PATH_TEXT_RAW_CORPUS = ""
SUBDIR_TEXT_CLEAN = ""
SUBDIR_SENTIMENT_RAW = ""
SUBDIR_SENTIMENT_CLEAN = ""
SUBDIR_TIMESERIES_RAW = ""
SUBDIR_TIMESERIES_CLEAN = ""
SUBDIR_GRAPHS = ""
SUBDIR_CRUXES = ""
SUBDIR_DATA = ""
SUBDIR_UTILS = ""

# NLP Processing
MIN_PARAG_LEN = 0
MIN_SENT_LEN = 0
STOPWORDS_ADD_EN = []
STOPWORDS_DEL_EN = []

# Testing Sets
TEST_WORDS_LS = []
TEST_SENTENCES_LS  = []

# Dictionary[Slang] = Standard English (to help lexicons)
SLANG_DT = {}