
def config_seaborn():
  '''
  Set configurations params for Seaborn
  '''

  global sns
  # View previous seaborn configuration
  # print('\n Old Seaborn Configurtion Settings:\n')
  sns.axes_style()
  print('\n\n')

  # Update and View new seaborn configuration
  # print('\n New Seaborn Configurtion Settings:\n')

  # Change defaults
  # sns.set(style='white', context='talk', palette='tab10')

  sns.set_theme('paper') # paper, notebook, talk, poster
  sns.set_context('paper')
  sns.set_style('white')    # darkgrid, whitegrid, dark, white, and ticks
  sns.set_palette('tab10')  # High-Contrast Palette, Vision Impaired Friendly

  return