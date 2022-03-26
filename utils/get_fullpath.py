
def get_fullpath(text_title_str, ftype='data_clean', fig_no='', first_note = '',last_note='', plot_ext='png', no_date=False):
  '''
  Given a required file_type(ftype:['data_clean','data_raw','plot']) and
    optional first_note: str inserted after Title and before (optional) SMA/Standardization info
            last_note: str insterted after (optional) SMA/Standardization info and before (optional) timedate stamp
            plot_ext: change default *.png extension of plot file
            no_date: don't add trailing datetime stamp to filename
  Generate and return a fullpath (/subdir/filename.ext) to save file to
  '''

  # String with full path/filename.ext to return
  fname = ''

  # Get current datetime stamp as a string
  if no_date:
    date_dt = ''
  else:
    date_dt = f'_{datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")}'

  # Clean optional file notation if passed in
  if first_note:
    fnote_str = first_note.replace(' ', '_')
    fnote_str = '_'.join(fnote_str.split())
    fnote_str = '_'.join(fnote_str.split('.'))
    fnote_str = '_'.join(fnote_str.split('__'))
    fnote_str = fnote_str.lower()

  if first_note:
    text_title_str = f'{text_title_str}_{first_note}'

  # Option (a): Cleaned Model Data (Smoothed then Standardized)
  if ftype == 'data_clean':
    fprefix = 'sa_clean_'
    fname_str = f'{SUBDIR_SENTIMENT_CLEAN}{fprefix}{text_title_str}_{Model_Standardization_Method.lower()}_sma{Window_Percent}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.csv'
    else:
      fname = f'{fname_str}{date_dt}.csv'

  # Option (b): Raw Model Data
  elif ftype == 'data_raw':
    fprefix = 'sa_raw_'
    fname_str = f'{SUBDIR_SENTIMENT_RAW}{fprefix}{text_title_str}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.csv'
    else:
      fname = f'{fname_str}{date_dt}.csv'

  # Option (c): Plot Figure
  elif ftype == 'plot':
    if fig_no:
      fprefix = f'plot_{fig_no}_'
    else:
      fprefix = 'plot_'
    fname_str = f'{SUBDIR_SENTIMENT_PLOTS}{fprefix}{text_title_str}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.{plot_ext}'
    else:
      fname = f'{fname_str}{date_dt}.{plot_ext}'

  # Option (d): Crux Text
  elif ftype == 'crux_text':
    fprefix = 'crux_'
    fname_str = f'{SUBDIR_SENTIMENT_CRUXES}{fprefix}{text_title_str}'
    if last_note:
      fname = f'{fname_str}_{last_note}{date_dt}.txt'
    else:
      fname = f'{fname_str}{date_dt}.txt'

  else:
    print(f'ERROR: In get_fullpath() with illegal arg ftype:[{ftype}]')
    return f'ERROR: ftype:[{ftype}]'

  return fname