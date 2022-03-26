
def config_matplotlib():
  '''
  Set configurations params for Matplotlib
  '''

  global plt

  from cycler import cycler

  colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']   
  linestyles = ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--']

  cycle = plt.cycler("color", colors) + plt.cycler("linestyle", linestyles)

  # View previous matplotlib configuration
  # print('\n Old Matplotlib Configurtion Settings:\n')
  # plt.rc.show
  print('\n\n')

  # Update and view new matplotlib configuration
  # print('\n New Matplotlib Configurtion Settings:\n')
  myparams = {'axes.prop_cycle': cycle}
  plt.rcParams.update(myparams)

  plt.rcParams["axes.titlesize"] = 16
  plt.rcParams['figure.figsize'] = 20,10
  plt.rcParams["legend.fontsize"] = 10
  plt.rcParams["xtick.labelsize"] = 12
  plt.rcParams["ytick.labelsize"] = 12
  plt.rcParams["axes.labelsize"] = 12
  plt.rcParams["figure.titlesize"] = 32

  # View matplotlib options
  # plt.rcParams.keys()

  # Set matplotlib plot figure.figsize
  new_plt_size = plt.rcParams["figure.figsize"]=(20,10)
  print(" New figure size: ",new_plt_size)

  return