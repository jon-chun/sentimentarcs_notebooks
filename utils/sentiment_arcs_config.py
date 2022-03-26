
def get_subdirs(Corpus_Genre, Corpus_Type, Corpus_Number, NotebookModels):
    '''
    Given a two strings: Corpus, Text_type
    Set all global SUB/DIR constants
    '''

    global FNAME_SENTIMENT_RAW
    global SUBDIR_SENTIMENTARCS
    global SUBDIR_TEXT_RAW
    global SUBDIR_TEXT_CLEAN
    global SUBDIR_SENTIMENT_RAW
    global SUBDIR_SENTIMENT_CLEAN
    global SUBDIR_TIMESERIES_RAW
    global SUBDIR_TIMESERIES_CLEAN
    global SUBDIR_PLOTS
    global SUBDIR_DATA
    global SUBDIR_UTILS

    # NotebookModels indicates which notebook is currently running that imported this get_subdirs() function
    if NotebookModels == 'syuzhetr2sentimentr':
        FNAME_SENTIMENT_RAW = f'sentiment_raw_{Corpus_Genre}_{Corpus_Type}_syuzhetr2sentimentr.json'
    elif NotebookModels == 'lex2ml':
        FNAME_SENTIMENT_RAW = f'sentiment_raw_{Corpus_Genre}_{Corpus_Type}_lex2ml.json'
    elif NotebookModels == 'dnn2transformers':
        FNAME_SENTIMENT_RAW = f'sentiment_raw_{Corpus_Genre}_{Corpus_Type}_dnn2transformers.json'
    elif NotebookModels == 'none':
        FNAME_SENTIMENT_RAW = f'[NONE]'
    else:
        print(f'ERROR: Illegal value for NotebookModels: {NotebookModels}')
        return

    # Define a universal syntax for a common directory structure across all notebooks
    SUBDIR_SENTIMENTARCS = '/gdrive/MyDrive/cdh/sentiment_arcs'
    if Corpus_Type == 'new':
        SUBDIR_TEXT_RAW = f"./text_raw/text_raw_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}/"
        SUBDIR_TEXT_CLEAN = f"./text_clean/text_clean_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}/"
        SUBDIR_SENTIMENT_RAW = f"./sentiment_raw/sentiment_raw_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}/"
        SUBDIR_SENTIMENT_CLEAN = f"./sentiment_clean/sentiemnt_clean_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}/"
        SUBDIR_TIMESERIES_RAW = f"./timeseries_raw/timeseries_raw_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}/"
        SUBDIR_TIMESERIES_CLEAN = f"./timeseries_clean/timeseries_clean_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}/"
    elif Corpus_Type == 'ref':
        SUBDIR_TEXT_RAW = f"./text_raw/text_raw_{Corpus_Genre}_{Corpus_Type}/"
        SUBDIR_TEXT_CLEAN = f"./text_clean/text_clean_{Corpus_Genre}_{Corpus_Type}/"
        SUBDIR_SENTIMENT_RAW = f"./sentiment_raw/sentiment_raw_{Corpus_Genre}_{Corpus_Type}/"
        SUBDIR_SENTIMENT_CLEAN = f"./sentiment_clean/sentiemnt_clean_{Corpus_Genre}_{Corpus_Type}/"
        SUBDIR_TIMESERIES_RAW = f"./timeseries_raw/timeseries_raw_{Corpus_Genre}_{Corpus_Type}/"
        SUBDIR_TIMESERIES_CLEAN = f"./timeseries_clean/timeseries_clean_{Corpus_Genre}_{Corpus_Type}/"
    else:
        print(f'ERROR: Illegal value for Corpus_Type: {Corpus_Type}')

    SUBDIR_GRAPHS = f"./graphs/graphs_{Corpus_Genre}/"
    SUBDIR_DATA = f"./data/data_{Corpus_Genre}"
    SUBDIR_UTILS = f"./utils/"

    # Provide user feedback to verify Directory Structure
    print('Verify the Directory Structure:\n')
    print('-------------------------------\n')

    print(f'           [Corpus Genre]: {Corpus_Genre}\n')
    print(f'            [Corpus Type]: {Corpus_Type}\n\n')

    print(f'    [FNAME_SENTIMENT_RAW]: {FNAME_SENTIMENT_RAW}\n\n')
    print('\n\nINPUTS:')
    print('-------------------------------\n')
    print(f'   [SUBDIR_SENTIMENTARCS]: {SUBDIR_SENTIMENTARCS}\n')
    print('\nSTEP 1: Clean Text')
    print('--------------------\n')
    print(f'        [SUBDIR_TEXT_RAW]: {SUBDIR_TEXT_RAW}\n')
    print(f'      [SUBDIR_TEXT_CLEAN]: {SUBDIR_TEXT_CLEAN}\n')
    print('\nSTEP 2: Get Sentiments')
    print('--------------------\n')
    print(f'   [SUBDIR_SENTIMENT_RAW]: {SUBDIR_SENTIMENT_RAW}\n')
    print(f' [SUBDIR_SENTIMENT_CLEAN]: {SUBDIR_SENTIMENT_CLEAN}\n')
    print('\nSTEP 3: Smooth Time Series and Get Crux Points')
    print('--------------------\n')
    print(f'  [SUBDIR_TIMESERIES_RAW]: {SUBDIR_SENTIMENT_RAW}\n')
    print(f'[SUBDIR_TIMESERIES_CLEAN]: {SUBDIR_SENTIMENT_CLEAN}\n')
    print('\n\nOUTPUTS:')
    print('-------------------------------\n')
    print(f'           [SUBDIR_PLOTS]: {SUBDIR_GRAPHS}\n')
    print(f'            [SUBDIR_DATA]: {SUBDIR_DATA}\n')
    print(f'           [SUBDIR_UTILS]: {SUBDIR_UTILS}\n')

    return

def get_globals():
    '''
    When called from any notebook, use this routine to set all global values in this one centralized file
    '''

    # Define minimum paragraph and sentence lengths for data cleaning
    #   any parag/sent less than these mins will be ignored/blanked
    global MIN_PARAG_LEN
    global MIN_SENT_LEN
    MIN_PARAG_LEN = 10
    MIN_SENT_LEN = 3

    # Stopwords to add and delete from default English stopword list
    global STOPWORDS_ADD_EN
    global STOPWORDS_DEL_EN
    STOPWORDS_ADD_EN = ['a', 'the', 'an']
    STOPWORDS_DEL_EN = ['jimmy', 'dean']

    # Main Dictionary holding all Lexicon by Name/Key
    global lexicons_dt
    lexicons_dt = {}

    # Test WORDS of Sentiment Analysis
    global test_words_ls
    test_words_ls =["Love",
    "Hate",
    "bizarre",
    "strange",
    "furious",
    "elated",
    "curious",
    "beserk",
    "gambaro"]
                    
    # Test SENTENCES of Sentiment Analysis
    global test_sentences_ls
    test_sentences_ls = ["I hate bad evil worthless Mondays.",
    "I love Paris in the springtime",
    "It was Wednesday.",
    "You are a disgusting pig - I hate you.",
    "What a delightfully funny and beautiful good man.",
    "That was it"]


    # Abbreviation / Slang
    # https://www.kaggle.com/nmaguette/up-to-date-list-of-slangs-for-text-preprocessing/notebook

    global SLANG_DT
    SLANG_DT = {
        "$" : " dollar ",
        "€" : " euro ",
        "4ao" : "for adults only",
        "a.m" : "before midday",
        "a3" : "anytime anywhere anyplace",
        "aamof" : "as a matter of fact",
        "acct" : "account",
        "adih" : "another day in hell",
        "afaic" : "as far as i am concerned",
        "afaict" : "as far as i can tell",
        "afaik" : "as far as i know",
        "afair" : "as far as i remember",
        "afk" : "away from keyboard",
        "app" : "application",
        "approx" : "approximately",
        "apps" : "applications",
        "asap" : "as soon as possible",
        "asl" : "age, sex, location",
        "atk" : "at the keyboard",
        "ave." : "avenue",
        "aymm" : "are you my mother",
        "ayor" : "at your own risk", 
        "b&b" : "bed and breakfast",
        "b+b" : "bed and breakfast",
        "b.c" : "before christ",
        "b2b" : "business to business",
        "b2c" : "business to customer",
        "b4" : "before",
        "b4n" : "bye for now",
        "b@u" : "back at you",
        "bae" : "before anyone else",
        "bak" : "back at keyboard",
        "bbbg" : "bye bye be good",
        "bbc" : "british broadcasting corporation",
        "bbias" : "be back in a second",
        "bbl" : "be back later",
        "bbs" : "be back soon",
        "be4" : "before",
        "bfn" : "bye for now",
        "blvd" : "boulevard",
        "bout" : "about",
        "brb" : "be right back",
        "bros" : "brothers",
        "brt" : "be right there",
        "bsaaw" : "big smile and a wink",
        "btw" : "by the way",
        "bwl" : "bursting with laughter",
        "c/o" : "care of",
        "cet" : "central european time",
        "cf" : "compare",
        "cia" : "central intelligence agency",
        "csl" : "can not stop laughing",
        "cu" : "see you",
        "cul8r" : "see you later",
        "cv" : "curriculum vitae",
        "cwot" : "complete waste of time",
        "cya" : "see you",
        "cyt" : "see you tomorrow",
        "dae" : "does anyone else",
        "dbmib" : "do not bother me i am busy",
        "diy" : "do it yourself",
        "dm" : "direct message",
        "dwh" : "during work hours",
        "e123" : "easy as one two three",
        "eet" : "eastern european time",
        "eg" : "example",
        "embm" : "early morning business meeting",
        "encl" : "enclosed",
        "encl." : "enclosed",
        "etc" : "and so on",
        "faq" : "frequently asked questions",
        "fawc" : "for anyone who cares",
        "fb" : "facebook",
        "fc" : "fingers crossed",
        "fig" : "figure",
        "fimh" : "forever in my heart", 
        "ft." : "feet",
        "ft" : "featuring",
        "ftl" : "for the loss",
        "ftw" : "for the win",
        "fwiw" : "for what it is worth",
        "fyi" : "for your information",
        "g9" : "genius",
        "gahoy" : "get a hold of yourself",
        "gal" : "get a life",
        "gcse" : "general certificate of secondary education",
        "gfn" : "gone for now",
        "gg" : "good game",
        "gl" : "good luck",
        "glhf" : "good luck have fun",
        "gmt" : "greenwich mean time",
        "gmta" : "great minds think alike",
        "gn" : "good night",
        "g.o.a.t" : "greatest of all time",
        "goat" : "greatest of all time",
        "goi" : "get over it",
        "gps" : "global positioning system",
        "gr8" : "great",
        "gratz" : "congratulations",
        "gyal" : "girl",
        "h&c" : "hot and cold",
        "hp" : "horsepower",
        "hr" : "hour",
        "hrh" : "his royal highness",
        "ht" : "height",
        "ibrb" : "i will be right back",
        "ic" : "i see",
        "icq" : "i seek you",
        "icymi" : "in case you missed it",
        "idc" : "i do not care",
        "idgadf" : "i do not give a damn fuck",
        "idgaf" : "i do not give a fuck",
        "idk" : "i do not know",
        "ie" : "that is",
        "i.e" : "that is",
        "ifyp" : "i feel your pain",
        "IG" : "instagram",
        "iirc" : "if i remember correctly",
        "ilu" : "i love you",
        "ily" : "i love you",
        "imho" : "in my humble opinion",
        "imo" : "in my opinion",
        "imu" : "i miss you",
        "iow" : "in other words",
        "irl" : "in real life",
        "j4f" : "just for fun",
        "jic" : "just in case",
        "jk" : "just kidding",
        "jsyk" : "just so you know",
        "l8r" : "later",
        "lb" : "pound",
        "lbs" : "pounds",
        "ldr" : "long distance relationship",
        "lmao" : "laugh my ass off",
        "lmfao" : "laugh my fucking ass off",
        "lol" : "laughing out loud",
        "ltd" : "limited",
        "ltns" : "long time no see",
        "m8" : "mate",
        "mf" : "motherfucker",
        "mfs" : "motherfuckers",
        "mfw" : "my face when",
        "mofo" : "motherfucker",
        "mph" : "miles per hour",
        "mr" : "mister",
        "mrw" : "my reaction when",
        "ms" : "miss",
        "mte" : "my thoughts exactly",
        "nagi" : "not a good idea",
        "nbc" : "national broadcasting company",
        "nbd" : "not big deal",
        "nfs" : "not for sale",
        "ngl" : "not going to lie",
        "nhs" : "national health service",
        "nrn" : "no reply necessary",
        "nsfl" : "not safe for life",
        "nsfw" : "not safe for work",
        "nth" : "nice to have",
        "nvr" : "never",
        "nyc" : "new york city",
        "oc" : "original content",
        "og" : "original",
        "ohp" : "overhead projector",
        "oic" : "oh i see",
        "omdb" : "over my dead body",
        "omg" : "oh my god",
        "omw" : "on my way",
        "p.a" : "per annum",
        "p.m" : "after midday",
        "pm" : "prime minister",
        "poc" : "people of color",
        "pov" : "point of view",
        "pp" : "pages",
        "ppl" : "people",
        "prw" : "parents are watching",
        "ps" : "postscript",
        "pt" : "point",
        "ptb" : "please text back",
        "pto" : "please turn over",
        "qpsa" : "what happens", #"que pasa",
        "ratchet" : "rude",
        "rbtl" : "read between the lines",
        "rlrt" : "real life retweet", 
        "rofl" : "rolling on the floor laughing",
        "roflol" : "rolling on the floor laughing out loud",
        "rotflmao" : "rolling on the floor laughing my ass off",
        "rt" : "retweet",
        "ruok" : "are you ok",
        "sfw" : "safe for work",
        "sk8" : "skate",
        "smh" : "shake my head",
        "sq" : "square",
        "srsly" : "seriously", 
        "ssdd" : "same stuff different day",
        "tbh" : "to be honest",
        "tbs" : "tablespooful",
        "tbsp" : "tablespooful",
        "tfw" : "that feeling when",
        "thks" : "thank you",
        "tho" : "though",
        "thx" : "thank you",
        "tia" : "thanks in advance",
        "til" : "today i learned",
        "tl;dr" : "too long i did not read",
        "tldr" : "too long i did not read",
        "tmb" : "tweet me back",
        "tntl" : "trying not to laugh",
        "ttyl" : "talk to you later",
        "u" : "you",
        "u2" : "you too",
        "u4e" : "yours for ever",
        "utc" : "coordinated universal time",
        "w/" : "with",
        "w/o" : "without",
        "w8" : "wait",
        "wassup" : "what is up",
        "wb" : "welcome back",
        "wtf" : "what the fuck",
        "wtg" : "way to go",
        "wtpa" : "where the party at",
        "wuf" : "where are you from",
        "wuzup" : "what is up",
        "wywh" : "wish you were here",
        "yd" : "yard",
        "ygtr" : "you got that right",
        "ynk" : "you never know",
        "zzz" : "sleeping bored and tired"
    }

    return

