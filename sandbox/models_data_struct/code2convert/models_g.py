import json
import pandas as pd
import numpy as np

from utilities_formulas import getIdFromName

def getIdFormulaByName(list_f, name):
    for f in list_f:
        if name == f["name"]:
            return f["id"]
    return -1

def getPartNumberModelByName(list_m, no_parte):
    for m in list_m:
        if no_parte == m["part_number"]:
            return m["id"]
    return -1

filepath_model_g_1 = 'data/modelos_g_capa1.csv'
filepath_model_g_2 = 'data/modelos_g_capa2.csv'

df = pd.read_csv(filepath_model_g_1)

print(df)

columns_shared = ["Pintado", "EA", "color", "description"]
columns_no_parte = "no_parte-"
columns_1 = [ ["Base", "g-base"], ["Tiner 1", "g-T1"], ["Tiner 2", "g-T2"], ["Tiner 3", "g-T3"], ["Catalizador", "g-C"] ]
columns_2 = [ ["Barniz","g-B"], ["Tiner","g-T"], ["Catalizador","g-C"] ]

print(" Valores únicos de las columnas: ")
pintado = df["Pintado"].unique()
print("Numero de lementos: {}".format( len(pintado) ))
print(pintado)
no_parte = df["full_no_parte"].unique()
print("Numero de lementos: {}".format( len(no_parte) ))
print(no_parte)
bases = df["Base"].unique()
print("Numero de lementos: {}".format( len(bases) ))
print(bases)
tiners_1 = df["Tiner 1"].unique()
print("Numero de lementos: {}".format( len(tiners_1) ))
print(tiners_1)
tiners_2 = df["Tiner 2"].unique()
print("Numero de lementos: {}".format( len(tiners_2) ))
print(tiners_2)
tiners_3 = df["Tiner 3"].unique()
print("Numero de lementos: {}".format( len(tiners_3) ))
print(tiners_3)
catalizador = df["Catalizador"].unique()
print("Numero de lementos: {}".format( len(catalizador) ))
print(catalizador)

########## Save new json models ... 
dict_modles = {"list": []}
for i in range(len(no_parte)):
    dict_modles["list"].append({ "id": i, "part_number": no_parte[i], "description": ""}) # por ahora descripción estará vacía
list_mod = dict_modles["list"]
path_ = "./../data_structs/"
pathfile = path_ + "models.json"
with open(pathfile, 'w') as json_file:
    json.dump(dict_modles, json_file)



df_color = df.groupby('Base')

filepathjson = "./../data_structs/formulas.json"
with open(filepathjson, 'r') as json_file:
    formulas = json.load(json_file)

print("***************** Formulas: ")
list_f = formulas["list"]

for formula in list_f:
    print(formula["name"])
dict_color_model = {"list": []}
id_l_mod = 0
print("----------- Agrupado: ")
factor_weight = 1000
for group_name, df_group in df_color:
    selected_formula = None
    for formula in list_f:
        if formula["name"] == group_name:
            selected_formula = formula
            break
    if selected_formula is None:
        print("No se pudo encontrar {}".format(group_name))
        continue
    else:
        print("{} ---> {}".format(group_name, selected_formula["name"]))
    columns_important = ["Pintado", "full_no_parte", "Base", "g-base", "Tiner 1", "g-T1", "Tiner 2", "g-T2", "Tiner 3", "g-T3", "Catalizador", "g-C"]
    df_g = df_group[ columns_important ]
    #print(df_group[columns_important])
    list_c = selected_formula["list_componets"]
    text_ = ""
    for comp in list_c:
        text_ += "{} ({} %) \t".format(comp["name"], comp["percentage"])
    print(text_)
    print(df_g)
    unique_base = df_g["Base"].unique()
    unique_comp_1 = df_g["Tiner 1"].unique()
    unique_comp_2 = df_g["Tiner 2"].unique()
    unique_comp_3 = df_g["Tiner 3"].unique()
    unique_catal = df_g["Catalizador"].unique()
    print(unique_base)
    percentages_dict = ({ unique_base[0]: [0],  unique_comp_1[0]: [0], unique_comp_2[0]: [0], unique_comp_3[0]: [0], unique_catal[0]: [0], "tot_weight": [0], "tot_percentage": [0]})
    #print(percentages_dict)
    df_percentages = pd.DataFrame( percentages_dict )
    for index,record in df_g.iterrows():
        base_name = record[columns_1[0][0]]
        weight_base = float(record[columns_1[0][1]]) *factor_weight
        text_ = "Base: {}g -- 100%  ".format(weight_base)
        percentage_component_weight = []
        tot_weight = weight_base
        new_row = {base_name: [100]}
        id_formula = getIdFormulaByName(list_f, base_name)
        model_name = record["full_no_parte"]
        id_model = getPartNumberModelByName(list_mod, model_name)
        dict_color_model["list"].append( {"id": id_l_mod, "id_": record["Pintado"], "id_model":  id_model, "id_color": id_formula } )
        id_l_mod += 1
        for i in range(4):
            name_comp = record[ columns_1[i+1][0] ]
            if not pd.isna(name_comp):
                weight_comp = float(record[ columns_1[i+1][1] ])*factor_weight
                percentage_ = (weight_comp/weight_base)*100
                tot_weight += weight_comp
                percentage_component_weight.append( percentage_ )
                text_ += "* {} -> {:.7}g -- {:.5}% ".format(name_comp,weight_comp, percentage_)
                new_row[name_comp] = [percentage_]
            else:
                new_row[name_comp] = [0]
        tot_percentage = 100 + sum(percentage_component_weight)
        new_row["tot_weight"] = [tot_weight]
        new_row["tot_percentage"] = [tot_percentage]
        new_df = pd.DataFrame((new_row))
        #print(new_row)
        #df_percentages.append(new_row, ignore_index=True)
        df_percentages = pd.concat([ new_df, df_percentages.loc[:] ]).reset_index(drop=True)
        #text_ += " :::: Totales (g,%) ({}g, {}%)".format(tot_weight, tot_percentage)
        #print(text_)
    print(df_percentages)

pathfile = path_ + "color_model.json"
with open(pathfile, 'w') as json_file:
    json.dump(dict_color_model, json_file)

##### Calcular los pesos finales y guardarlos ... 
dict_pintado_peso_pieza = {"list": []}
print("Pesos totales y porcentajes: ")
factor_weight = 1000
for index, record in df.iterrows():
    #print("{}-> {}".format(index, record))
    data = {"pintado": record["Pintado"], "color": record["Base"], "no_parte": record["full_no_parte"], "description": record["description"]}
    print(" ******************************************************************** ")
    base_name = record[columns_1[0][0]]
    #id_formula = getIdFormulaByName(list_f, base_name)
    weight_base = float(record[columns_1[0][1]]) *factor_weight
    text_ = "Peso Base: {}  ".format(weight_base)
    percentage_component_weight = []
    tot_weight = weight_base
    for i in range(4):
        name_comp = record[ columns_1[i+1][0] ]
        if not pd.isna(name_comp):
            weight_comp = float(record[ columns_1[i+1][1] ])*factor_weight
            percentage_ = (weight_comp/weight_base)*100
            tot_weight += weight_comp
            percentage_component_weight.append( percentage_ )
            text_ += "* {} -> {:.7} gr --- {:.5} % ".format(name_comp,weight_comp, percentage_)
    tot_percentage = 100 + sum(percentage_component_weight)
    text_ += " :::: Total W: {} and tot %: {}".format(tot_weight, tot_percentage)
    #data["peso"] = tot_weight
    data["peso_base"] = round(weight_base,6)
    dict_pintado_peso_pieza["list"].append(data)
    print(text_)
print(dict_pintado_peso_pieza)

pathfile = path_ + "pintado_pesos.json"
with open(pathfile, 'w') as json_file:
    json.dump(dict_pintado_peso_pieza, json_file)




