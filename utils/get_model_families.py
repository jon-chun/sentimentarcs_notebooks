
import global_vars

def get_ensemble_model_famalies(models_titles_dt):
  '''
  Given a Dict of Model Titles
  Return a list of lists (one for each family populated with corresponding models)
  '''

  # Convenience lists for each type of model

  # Lexicon Models
  models_lexicon_ls = [x[0] for x in models_titles_dt.values() if x[1] == 'lexicon']
  print(f'\nThere are {len(models_lexicon_ls)} Lexicon Models')
  for i,amodel in enumerate(models_lexicon_ls):
    print(f'  Lexicon Model #{i}: {amodel}')

  # Heuristic Models
  models_heuristic_ls = [x[0] for x in models_titles_dt.values() if x[1] == 'heuristic']
  print(f'\nThere are {len(models_heuristic_ls)} Heuristic Models')
  for i,amodel in enumerate(models_heuristic_ls):
    print(f'  Heuristic Model #{i}: {amodel}')

  # Traditional ML Models
  models_tradml_ls = [x[0] for x in models_titles_dt.values() if x[1] == 'tradml']
  print(f'\nThere are {len(models_tradml_ls)} Traditional ML Models')
  for i,amodel in enumerate(models_tradml_ls):
    print(f'  Traditional ML Model #{i}: {amodel}')

  # DNN Models
  models_dnn_ls = [x[0] for x in models_titles_dt.values() if x[1] == 'dnn']
  print(f'\nThere are {len(models_dnn_ls)} DNN Models')
  for i,amodel in enumerate(models_dnn_ls):
    print(f'  DNN Model #{i}: {amodel}')

  # Transformer Models
  models_transformer_ls = [x[0] for x in models_titles_dt.values() if x[1] == 'transformer']
  print(f'\nThere are {len(models_transformer_ls)} Transformer Models')
  for i,amodel in enumerate(models_transformer_ls):
    print(f'  Transformer Model #{i}: {amodel}')

  # All Models

  models_ensemble_dt = {}
  models_ensemble_dt['lexicon'] = models_lexicon_ls
  models_ensemble_dt['heuristic'] = models_heuristic_ls
  models_ensemble_dt['ml'] = models_tradml_ls
  models_ensemble_dt['dnn'] = models_dnn_ls
  models_ensemble_dt['transformer'] = models_transformer_ls

  print(f'\nThere are {len(models_ensemble_dt.keys())} Total Models:')
  for i,amodel in enumerate(models_ensemble_dt.keys()):
    print(f'  Model #{i:>2}: {amodel}')

  print(f'\nThere are {len(models_ensemble_dt.keys())} Total Models (+1 for Ensemble Mean)')

  return models_ensemble_dt