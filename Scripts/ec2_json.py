import json
import sys, getopt
import csv


# Pegando o nome do arquivo por getopts
def main(argv):
    jsonfile = ''
    csvfile = ''
    resultdict = []
    titulos = ['ID', 'Tipo', 'Nome', 'Discos']
    try:
        opts, args = getopt.getopt(argv,"hi:o:")
    except getopt.GetoptError:
        print('Use ec2_json.py -i arquivo.json')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Use ec2_json.py -i arquivo.json')
            sys.exit()
        elif opt == '-i':
            jsonfile = arg
        elif opt == '-o':
            csvfile = arg
    print('Arquivo json: {}'.format(jsonfile))
    #Abrindo o arquivo
    with open(jsonfile,'r') as f:
        arq = json.load(f)

    for campos in arq['Reservations']:
        # zerar o dict disks a cada iteração do for acima pois só quero para cada instância
        disks = {'unidade':[]}
        #print("ID: {}".format(campos['Instances'][0]['InstanceId']))
        for discos in campos['Instances'][0]['BlockDeviceMappings']:
                        disks['unidade'].append(discos['Ebs']['VolumeId'])
        #print(type(discos))
        #print(disks)
        lista = campos['Instances'][0]['Tags']
        for tags in lista:
            if tags['Key'] == 'Name':
                # print("Nome: {}".format(tags['Value']))
                resultdict.append({"ID": campos['Instances'][0]['InstanceId'],"Tipo": campos['Instances'][0]['InstanceType'],"Nome": tags['Value'],"Discos": disks['unidade']})
        

    #print(resultdict)

    with open(csvfile, 'w') as arquivocsv: 
        escreve = csv.DictWriter(arquivocsv, fieldnames=titulos)
        escreve.writeheader()
        escreve.writerows(resultdict)
        
    




if __name__ == "__main__":
   main(sys.argv[1:])




