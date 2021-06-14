import mysql.connector
from mysql.connector import errorcode
import os
import smtplib
import variaveis 

# Conf email
server = smtplib.SMTP(variaveis.hostemail)
FROM = variaveis.mailfrom
TO = variaveis.mailto

if not os.path.isfile(variaveis.home + '/' + variaveis.conffile):
  MSG = '[GLPI RELATORIO] Erro ao abrir arquivo conf \n\n Script não encontrou o arquivo {} em {}\n Verifique o local e o nome dentro de variaveis.py'.format(variaveis.conffile, variaveis.home)
  server.sendmail(variaveis.mailfrom, variaveis.mailto, MSG.encode('utf-8'))
  os._exit(os.EX_OSFILE)

# CONEXAO COM BANCO
try:
  cnx = mysql.connector.connect(database=variaveis.database,
                                host=variaveis.hostglpi,
                                option_files=variaveis.home + '/' + variaveis.conffile
                                )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print(variaveis.msgerrodbconect)
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print(variaveis.msgerrodbnaoexiste)
  else:
    print(err)


cursor = cnx.cursor()


dados = (str("GOINFRA"), int(5), int(2021))




busca="""SELECT SUM(TIMESTAMPDIFF(MINUTE,gt.internal_time_to_own,gt.internal_time_to_resolve)) AS MINUTOS 
            FROM glpi.glpi_tickets gt 
            INNER JOIN glpi.glpi_plugin_fields_ticketcontratos        gpft ON gpft.items_id = gt.id 
            INNER JOIN glpi.glpi_plugin_fields_contratofielddropdowns gpfc ON gpfc.id = gpft.plugin_fields_contratofielddropdowns_id 
            WHERE gpft.servioindisponvelfield = '1' 
            AND	gpfc.name LIKE %s
            AND DATE_FORMAT(gt.internal_time_to_own, '%m') IN (%s) 
            AND DATE_FORMAT(gt.internal_time_to_own, '%Y') IN (%s)"""

cursor.execute(busca, (dados))




for MINUTOS in cursor:
    print("Tempo fora {}".format(MINUTOS[0]))

cursor.close()
cnx.close()