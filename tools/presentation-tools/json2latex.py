#!/usr/bin/python

import json

def json_to_latex_table(json_path,caption='Resumo da base de dados',label='tab:dataset_summary'):
    # Lê o arquivo JSON
    with open(json_path, 'r') as file:
        data = json.load(file)
    TOTAL=sum(data.values());
    
    # Cria o cabeçalho da tabela
    latex_table  = "\\begin{table}[h!]\n"
    latex_table += "\\centering\n"
    latex_table += "\\begin{tabular}{r|l|l}\n"
    latex_table += "\\hline\n"
    latex_table += "Categoria & Quantidade & Porcentagem \\\\\n"
    latex_table += "\\hline\n"
    latex_table += "\\hline\n"
    
    # Adiciona as linhas da tabela
    for category, count in data.items():
        percent= 100*float(count)/TOTAL;
        str_p=f"{percent:.2f}\\%";
        latex_table += category+" & "+str(count)+" & "+str_p+" \\\\\n"
        latex_table += "\\hline\n"
    latex_table += "\\hline\n"
    latex_table += "Total & "+str(TOTAL)+" & 100\\% \\\\\n"
    
    # Finaliza a tabela
    latex_table += "\\end{tabular}\n"
    latex_table += "\\caption{"+caption+"}\n"
    latex_table += "\\label{"+label+"}\n"
    latex_table += "\\end{table}"
    
    return latex_table

################################################################################

# Source
json_path = '../../archive/train/train.emotion4.csv.json'
latex_table = json_to_latex_table(  json_path,
                                    caption='Resumo da base de dados MCFER com 4 categorias - treinamento',
                                    label='tab:MCFER4:train')
print('\n')
print(latex_table)
print('\n')


# Source
json_path = '../../archive/test/test.emotion4.csv.json'
latex_table = json_to_latex_table(  json_path,
                                    caption='Resumo da base de dados MCFER com 4 categorias - teste',
                                    label='tab:MCFER4:test')
print('\n')
print(latex_table)
print('\n')
