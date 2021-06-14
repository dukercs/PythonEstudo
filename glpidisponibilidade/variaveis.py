from pathlib import Path


home = str(Path.home())
hostemail = "openrelay.datatraffic.com.br"
mailfrom = "infra@datatraffic.com.br"
mailto = "rodolpho.stach@datatraffic.com.br"

conffile = "my.cnf"
hostglpi = "10.0.1.39"
database = "glpi"




msgerrofile = str('Não encontrei o arquivo {}/.my.cnf\n Necessário para conectar no banco\n Consulte https://dev.mysql.com/doc/refman/5.7/en/option-files.html'.format(home))
msgerrodbnaoexiste = "O banco especificado {} não existe".format(database)
msgerrodbconect = "Acesso negado para a combinação de usuario e senha ou não é possível acessar com este usuário a partir deste host"