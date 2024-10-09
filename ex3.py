import csv

import csv


try:
    with open('dados.csv', 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        

        for linha in leitor_csv:
            print(linha)

        
except:
    print('Erro paizao')