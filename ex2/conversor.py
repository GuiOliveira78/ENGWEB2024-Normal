import csv
import json

def read_csv_file(file_path):
    bd = []
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            
            for row in csv_reader:
                new_row = {'id': row.pop('idcontrato')}
                new_row.update(row)
                bd.append(new_row)  # Deve ser new_row, não row
    except FileNotFoundError:
        print(f"O ficheiro {file_path} não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
    return bd

def pertenceContratos(valor, lista):
    return any(reg['id'] == valor for reg in lista)


def calc_contratos(bd):
    contratos = []
    for reg in bd:
        if not pertenceContratos(reg['id'], contratos) and reg['id'] != '':
            contratos.append(reg)
    return contratos


def pertenceEntidades(nipc, lista):
    return any(entidade['nipc'] == nipc for entidade in lista)

def calc_entidades(bd):
    entidades = []
    for reg in bd:
        if not pertenceEntidades(reg['NIPC_entidade_comunicante'], entidades) and reg['NIPC_entidade_comunicante'] != '':
            entidades.append({'nipc': reg['NIPC_entidade_comunicante'],
                              'nome': reg['entidade_comunicante'],
                              'contratos': [reg]})
        elif reg['NIPC_entidade_comunicante'] != '':
            for entidade in entidades:
                if entidade['nipc'] == reg['NIPC_entidade_comunicante']:
                    entidade['contratos'].append(reg)
                    break
            
    return entidades

file_path = 'contratos2024.csv'
myBD = read_csv_file(file_path)
contratos = calc_contratos(myBD)
entidades = calc_entidades(myBD)

novaBD = {
    'Contratos' : contratos,
    'Entidades' : entidades
}

with open("db.json", "w", encoding='utf-8') as f:
    json.dump(novaBD, f, ensure_ascii=False, indent=2)