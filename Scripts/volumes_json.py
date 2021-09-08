import json
import sys, getopt
import csv


# Pegando o nome do arquivo por getopts
def main(argv):
    helpmsg = 'Use volumes_json.py -i arquivo.json'
    jsonfile = ''
    #resultdict = []
    #titulos = ['ID', 'Tipo', 'Nome', 'Discos']
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print(helpmsg)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpmsg)
            sys.exit()
        elif opt == '-i':
            jsonfile = arg
            if jsonfile == "":
                sys.exit(helpmsg)
    print('Arquivo json: {}'.format(jsonfile))

    #Abrindo o arquivo
    with open(jsonfile,'r') as f:
        arq = json.load(f)

    for campos in arq['Volumes']:

        # zerar o dict disks a cada iteração do for acima pois só quero para cada instância
        # disks = {'unidade':[]}
        #print("ID: {}\n".format(campos['VolumeId']))
        for key in campos:
            #print('Chave: {}\nValor: {}\nTipo de valor: {}'.format(key, campos[key], type(campos[key])))
            validalista = isinstance(campos[key], (list, dict))

            if validalista is True:
                for subkey in campos[key]:
                    dicttexto = []
                    # print('Subchave: {}'.format(subkey))
                    for dict_chave in subkey:
                        addedtexto = "'" + str(dict_chave) + "': '" + str(subkey[dict_chave])+"'"
                        #print(addedtexto)
                        dicttexto.append(addedtexto)
            print (key, '--',campos[key], '++', dicttexto)

        #print('FORAIF ',key, ': ', campos[key], dicttexto)


        #for discos in campos['Instances'][0]['BlockDeviceMappings']:
        #                disks['unidade'].append(discos['Ebs']['VolumeId'])
        #print(type(discos))
        #print(disks)
"""         lista = campos['Instances'][0]['Tags']
        for tags in lista:
            if tags['Key'] == 'Name':
                # print("Nome: {}".format(tags['Value']))
                resultdict.append({"ID": campos['Instances'][0]['InstanceId'],"Tipo": campos['Instances'][0]['InstanceType'],"Nome": tags['Value'],"Discos": disks['unidade']})
        

    #print(resultdict)

    with open('saidacsv.csv', 'w') as arquivocsv: 
        escreve = csv.DictWriter(arquivocsv, fieldnames=titulos)
        escreve.writeheader()
        escreve.writerows(resultdict)
        
     """




if __name__ == "__main__":
   main(sys.argv[1:])




