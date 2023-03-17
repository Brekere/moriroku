import pandas as pd
import numpy as np
import json

def cvs2json(filepath = None, filepathjson = None, path_ = None):
    if filepath is None or filepathjson is None or path_ is None:
        print("No hay archivos que cargar o guardar")
        return

    data01 = pd.read_csv(filepath)
    df_formula = data01[ data01['Formula'].notnull() ]
    idx_formula = np.where(data01['Formula'].notnull())
    formulas_name = list(df_formula['Formula'].unique())
    print("******************************* Nombre de las formulas: ")
    print( df_formula['Formula'] )
    print(formulas_name)

    # Obtener los nombres de las bases
    df_bases = data01[ data01['Tipo'] == "Base" ]
    bases_name = list(df_bases['Nombres'].unique())
    print("******************************* Nombre de las Bases: ")
    print(df_bases)
    print(bases_name)

    # Obtener los nombres de los solventes
    df_solventes = data01[ data01['Tipo'] == "Solvente" ]
    solventes_name = list(df_solventes['Nombres'].unique())
    print("******************************* Nombre de los Solventes: ")
    print(df_solventes)
    print(solventes_name)

    # Obtener los nombres de los catalizadores
    df_catalizadores = data01[ data01['Tipo'] == "Catalizador" ]
    catalizadores_name = list(df_catalizadores['Nombres'].unique())
    print("******************************* Nombre de los Catalizadores: ")
    print(df_catalizadores)
    print(catalizadores_name)

    # Obtener los nombres de los aditivos (Crater y Anti Crater)
    idx_result = np.where( (data01['Tipo'] != "Catalizador") & (data01['Tipo'] != "Base") & (data01['Tipo'] != "Solvente"))
    #print(idx_result)
    df_aditivos = data01.loc[idx_result]
    aditivos_name = list(df_aditivos['Nombres'].unique())
    print("******************************* Nombre de las Aditivos: ")
    print(df_aditivos)
    print(aditivos_name)

    ### Guardar bases de color en un archivo ...
    idxs_bases = saveBases(bases_name, path_)
    ### Guardar solventes de color en un archivo ...
    idxs_solvents = saveSolvents(solventes_name, path_)
    ### Guardar aditivos de color en un archivo ...
    idxs_aditives = saveAdditives(aditivos_name, path_)
    ### Guardar aditivos de color en un archivo ...
    idxs_catalyst = saveCatalysts(catalizadores_name, path_)

    print(">>>>>>>>>> index formulas: {}".format(idx_formula))

    idx_formula = np.array(idx_formula[0])
    formulas = {"list": []}
    for i in range( idx_formula.shape[0] ):
        k = idx_formula[i]
        if i == idx_formula.shape[0] -1:
            idx_last_componet = data01.shape[0]-1
        else:
            idx_last_componet = idx_formula[i+1]-1
        print("######## Formula {} -> indices de componentes: {} {}".format(i+1, idx_formula[i], idx_last_componet) )
        try:
            id_formula = int(data01.iloc[k]['id'])
        except:
            id_formula = data01.iloc[k]['id']
        formula = {"name": data01.iloc[k]['Formula'], "id": id_formula, "list_componets": []}
        print(formula)
        for j in range(k,idx_last_componet+1):
            print(" Component {}>> type: {}  name: {}  percentage {}   tolerance: {} ".format (j, data01.iloc[j]['Tipo'], data01.iloc[j]['Nombres'], data01.iloc[j]['Porcentajes'], data01.iloc[j]['Tolerancia']  )  )
            percentage = data01.iloc[j]['Porcentajes']
            percentage = float(percentage.replace('%', '') )
            tolerance = data01.iloc[j]['Tolerancia']
            tolerance = float( tolerance.replace('%', '').replace('-', '').replace('+', '') )
            component_name = data01.iloc[j]['Nombres']
            type_component = 0
            if data01.iloc[j]['Tipo'] == "Base":
                id_componente = getIdFromName(idxs_bases, bases_name, component_name)
                #id_componente = bases_name.index(data01.iloc[j]['Nombres']) # id de solventes
            if data01.iloc[j]['Tipo'] == "Solvente":
                id_componente = getIdFromName(idxs_solvents, solventes_name, component_name)
                #id_componente = solventes_name.index(data01.iloc[j]['Nombres']) # id de solventes
                type_component = 1
            if data01.iloc[j]['Tipo'] == "Aditivo":
                id_componente = getIdFromName(idxs_aditives, aditivos_name, component_name)
                #id_componente = aditivos_name.index(data01.iloc[j]['Nombres']) # id de solventes
                type_component = 2
            if data01.iloc[j]['Tipo'] == "Catalizador":
                id_componente = getIdFromName(idxs_catalyst, catalizadores_name, component_name)
                #id_componente = catalizadores_name.index(data01.iloc[j]['Nombres']) # id de solventes
                type_component = 3
            print("id_componente : {}".format(id_componente))
            component = {"id_component": id_componente, "name": component_name, "type": type_component, "percentage": percentage, "tolerance": tolerance}
            formula['list_componets'].append(component)
        formulas['list'].append(formula)

    #data_json = json.dumps(formulas)

    with open(filepathjson, 'w') as json_file:
        json.dump(formulas, json_file)


def saveBases(listBases, path_):
    bases = {"type": 0, "name": "Base(color)", "list": []}
    idxs = []
    for i in range(len(listBases)):
        base = {"id": i, "name": listBases[i], "description": ""}
        idxs.append(i)
        bases['list'].append(base)
    # Guardar ..... 
    pathfile = path_ + "bases.json"
    with open(pathfile, 'w') as json_file:
        json.dump(bases, json_file)
    return idxs 

def saveSolvents(listSolvents, path_):
    solvents = {"type": 1, "name": "Solvente","list": []}
    idxs = []
    for i in range(len(listSolvents)):
        solvent = {"id": i, "name": listSolvents[i], "description": ""}
        idxs.append(i)
        solvents['list'].append(solvent)
    # Guardar ..... 
    pathfile = path_ + "solvents.json"
    with open(pathfile, 'w') as json_file:
        json.dump(solvents, json_file)
    return idxs

def saveAdditives(listAdditive, path_):
    additives = {"type": 2, "name": "Aditivo", "list": []}
    idxs = []
    for i in range(len(listAdditive)):
        additive = {"id": i, "name": listAdditive[i], "description": ""}
        idxs.append(i)
        additives['list'].append(additive)
    # Guardar ..... 
    pathfile = path_ + "additives.json"
    with open(pathfile, 'w') as json_file:
        json.dump(additives, json_file)
    return idxs

def saveCatalysts(listCatalyst, path_):
    catalysts = {"type": 3, "name": "Catalizador", "list": []}
    idxs = []
    for i in range(len(listCatalyst)):
        catalyst = {"id": i, "name": listCatalyst[i], "description": ""}
        idxs.append(i)
        catalysts['list'].append(catalyst)
    # Guardar ..... 
    pathfile = path_ + "catalysts.json"
    with open(pathfile, 'w') as json_file:
        json.dump(catalysts, json_file)
    return idxs

def getIdFromName(idxs, listE, name):
    try:
        idx_ = listE.index(name)
        id = idxs[idx_]
    except:
        id = -1
    return id 