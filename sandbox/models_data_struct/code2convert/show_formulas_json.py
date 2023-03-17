import json

filepathjson = "./../data_structs/formulas01.json"
with open(filepathjson, 'r') as json_file:
    data = json.load(json_file)

print("***************** Formulas 01")
print(data)


filepathjson = "./../data_structs/formulas02.json"
with open(filepathjson, 'r') as json_file:
    data = json.load(json_file)

print("***************** Formulas 02")
print(data)