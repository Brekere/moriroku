import pandas as pd
import numpy as np
import json

filepath = "data/modelos.csv"
filepathjson_models = "./../data_structs/models.json"
filepathjson_color_model = "./../data_structs/color_model.json"
data = pd.read_csv(filepath)

list_ids = data['id'].unique()
list_no_parts = data['no_parte'].unique()
list_description = data['description'].unique()
list_id_color = data['id_color'].unique()
list_color_codes = data['color_code'].unique()

print("######################################  Ids: ")
print(list_ids)
print( len(list_ids) )

print("######################################  No. Parts: ")
print(list_no_parts)
print( len(list_no_parts) )

print("######################################  Descriptions: ")
print(list_description)
print( len(list_description) )

print("######################################  Ids_Color: ")
print(list_id_color)
print( len(list_id_color) )

print("######################################  Color codes: ")
print(list_color_codes)
print( len(list_color_codes) )

### Generando un registro de la información ... por ahora no se guarda .. 
list_color_model = {"list": []}
for i in range(len(data)):
    #print(" ------ Especificion de modelo_pintado #{} \n {} ".format(i, data.iloc[i]))
    try:
        id_ = int(data.iloc[i]['id'])
    except:
        id_ = 0
    color_model = {"id": i, "id_": id_, "part_number": data.iloc[i]['no_parte'], "id_color": int(data.iloc[i]['id_color']), "color_code": data.iloc[i]['color_code']}
    list_color_model["list"].append(color_model)

#with open(filepathjson, 'w') as json_file:
#    json.dump(list_color_model, json_file)

print("Listar descripción y color por No. Parts")

for e in list_no_parts:
    rest = data[ data['no_parte'] == e ]
    print(">>>>>>>>>>>>>>> No. de parte: {}  --- tot: {}".format(e , rest.shape[0]))
    print(rest[["id", "description", "id_color", "color_code"]])

## Guardar los modelos solamente ... por número de parte
print("--------------- Guardando Modelos")
models = {"list": []}
ids_l = []
part_number_l = []
for i in range(list_no_parts.shape[0]):
    rest = data[ data['no_parte'] == list_no_parts[i] ]
    model = {"id": i, "part_number": list_no_parts[i], "description": rest.iloc[0]['description']}
    ids_l.append(i)
    part_number_l.append(list_no_parts[i])
    models["list"].append(model)
print(models)
with open(filepathjson_models, 'w') as json_file:
    json.dump(models, json_file)


## Guardar relación modelo y color 
print("--------------- Guardando Color-Modelo")
list_color_model = {"list": []}
for i in range(len(data)):
    try:
        id_ = int(data.iloc[i]['id'])
    except:
        id_ = 0
    part_number = data.iloc[i]["no_parte"]
    idx_rest = part_number_l.index(part_number)
    color_model = { "id": i ,"id_": id_, "id_model": ids_l[idx_rest],"id_color": int(data.iloc[i]['id_color']), "color_code": data.iloc[i]['color_code'] }
    list_color_model["list"].append(color_model)
print(list_color_model)

with open(filepathjson_color_model, 'w') as json_file:
    json.dump(list_color_model, json_file)