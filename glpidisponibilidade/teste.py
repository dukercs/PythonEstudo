from pathlib import Path
import os
import variaveis

print (variaveis.host)

home = str(Path.home())


if not os.path.isfile(str(home) + '/.my2.cnf'):
  print('Não')
  os._exit(os.EX_OSFILE)
else:
  print('Sim')



print('Resto')