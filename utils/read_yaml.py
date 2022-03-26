import global_vars

import yaml

def read_corpus_yaml(Corpus_Genre, Corpus_Type, Corpus_Number):
  '''
  Given a Corpus_Genre (e.g. novels), Corpus_Type (new or reference) and Corpus_Number (for new)
  Read and return the long-form titles for both Models and Corpus Texts
  '''

  if Corpus_Type == 'new':
    path_info_yaml = f'text_raw/text_raw_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}'
    file_yaml = f'text_raw_{Corpus_Genre}_{Corpus_Type}_corpus{Corpus_Number}_info.yaml'
  elif Corpus_Type == 'reference':
    path_info_yaml = f'text_raw/text_raw_{Corpus_Genre}_{Corpus_Type}'
    file_yaml = f'text_raw_{Corpus_Genre}_{Corpus_Type}_info.yaml'
  else:
    print(f'ERROR: Illegal value for Corpus_Type = {Corpus_Type}')
    return

  # Read Models Ensemble YAML Config Files 
  with open("./config/models_ref_info.yaml", "r") as stream:
    try:
      global_vars.models_titles_dt = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  # Read Corpus Texts YAML Config File
  print(f'YAML Directory: {path_info_yaml}')
  print(f'YAML File: {file_yaml}')
  with open(f"{path_info_yaml}/{file_yaml}", "r") as stream:
    try:
      global_vars.corpus_titles_dt = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      print(exc)

  return