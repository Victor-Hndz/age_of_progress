import json

doc = open("Provincias.json")

dic = json.load(doc)
doc.close()
for i in dic.keys():
    dic[i]["desarrollo"] = 1
    dic[i]["revueltas"] = {"baja":1,"media":1,"alta":1}
    dic[i]["prioridad"] = 1
    dic[i]["recurso"] = 0
    dic[i]["control"] = True

doc = open("Provincias.json","w")
doc.write(json.dumps(dic,indent=4,sort_keys=True))
