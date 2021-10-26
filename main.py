import random
import numpy
import math
import json

paises = dict()
provincias = dict()

Coste_desarrollo = {
    0:{
        "Coste_mejora":0,
        "Consumo_alimentos":5,
        "Consumo_alimentos_proc":0,
        "Consumo_alimentos_lux":0,
        "P_inv":25,
        "Ejercito":100
    },

    1:{
        "Coste_mejora":1000,
        "Consumo_alimentos":7.5,
        "Consumo_alimentos_proc":0,
        "Consumo_alimentos_lux":0,
        "P_inv":250,
        "Ejercito":250
    },

    2:{
        "Coste_mejora":2000,
        "Consumo_alimentos":10,
        "Consumo_alimentos_proc":2.5,
        "Consumo_alimentos_lux":0,
        "P_inv":2500,
        "Ejercito":500
    },

    3:{
        "Coste_mejora":4000,
        "Consumo_alimentos":12.5,
        "Consumo_alimentos_proc":3.75,
        "Consumo_alimentos_lux":1,
        "P_inv":25000,
        "Ejercito":1000
    },

    4:{
        "Coste_mejora":8000,
        "Consumo_alimentos":15,
        "Consumo_alimentos_proc":5,
        "Consumo_alimentos_lux":2.5,
        "P_inv":50000,
        "Ejercito":2000
    },

    5:{
        "Coste_mejora":16000,
        "Consumo_alimentos":20,
        "Consumo_alimentos_proc":7.5,
        "Consumo_alimentos_lux":3.5,
        "P_inv":100000,
        "Ejercito":3500
    }
}

coste_stock = {
    1:0.2,
    2:0.15,
    3:0.1,
    4:0.05
}

coste_comer = {
    1:1.5,
    2:1,
    3:0.5,
    4:0.25,
}

coste_infra = {
    2:{
        "Vias":100,
    },
    3:{
        "Vias":150,
        "Radio":100,
    },
    4:{
       "Vias":200,
        "Radio":150,
        "Procesador":75
    },
}

Coste_exp_categoria = {
    1:{
        "Coste_exp_m": 38,
        "Coste_exp_o":23,
        "Coste_apert_m":38,
        "Coste_apert_o":23,
        "Capacidad":50
    },
    2:{
        "Coste_exp_m": 25,
        "Coste_exp_o":15,
        "Coste_apert_m":63,
        "Coste_apert_o":38,
        "Capacidad":100
    },
    3:{
        "Coste_exp_m": 30,
        "Coste_exp_o":18,
        "Coste_apert_m":93,
        "Coste_apert_o":56,
        "Capacidad":150
    },
    4:{
        "Coste_exp_m": 35,
        "Coste_exp_o":21,
        "Coste_apert_m":128,
        "Coste_apert_o":77,
        "Capacidad":200
    },
    5:{
        "Coste_exp_m": 40,
        "Coste_exp_o":24,
        "Coste_apert_m":168,
        "Coste_apert_o":101,
        "Capacidad":250
    },
}


# Almacena todos los elementos del juego con sus propiedades


elementos = {
    "sui":{
        "Inputs":None,
        "Peso":0,
        "Valor":0,
        "Coste":0,
        "Coste_a":0,
        "Provincia":None,
    },
    "Hierro":{
        "Inputs":{},
        "Peso":4,
        "Valor":30,
        "Coste":15,
        "Coste_a":15,
        "Provincia":"Hierro",
    },
    "Hierro_proc":{
        "Inputs":{
            "Hierro":1
        },
        "Peso":4,
        "Valor":50,
        "Coste":15,
        "Coste_a":30,
        "Provincia":None,
    },
    "Acero":{
        "Inputs":{
            "Hierro_proc":4
        },
        "Peso":4,
        "Valor":185,
        "Coste":15,
        "Coste_a":135,
        "Provincia":None,
    },
    "Alimentos":{
        "Inputs":{},
        "Peso":1,
        "Valor":15,
        "Coste":10,
        "Coste_a":10,
        "Provincia":"Alimentos",
    },
    "Alimentos_proc":{
        "Inputs":{
            "Alimentos":2
        },
        "Peso":1,
        "Valor":37.5,
        "Coste":10,
        "Coste_a":30,
        "Provincia":None,
    },
    "Alimentos_lux":{
        "Inputs":{
            "Alimentos_proc":2
        },
        "Peso":1,
        "Valor":80,
        "Coste":10,
        "Coste_a":70,
        "Provincia":None,
    },
    "Carbon":{
        "Inputs":{},
        "Peso":3,
        "Valor":24,
        "Coste":15,
        "Coste_a":15,
        "Provincia":"Carbon",
    },
    "Combustible":{
        "Inputs":{
            "Carbon":1
        },
        "Peso":3,
        "Valor":45,
        "Coste":15,
        "Coste_a":30,
        "Provincia":None,
    },
    "Madera":{
        "Inputs":{},
        "Peso":2,
        "Valor":15,
        "Coste":7,
        "Coste_a":7,
        "Provincia":"Madera",
    },
    "Combustible_veg":{
        "Inputs":{
            "Madera":3
        },
        "Peso":3,
        "Valor":45,
        "Coste":15,
        "Coste_a":30,
        "Provincia":None,
    },
    "Cobre":{
        "Inputs":{},
        "Peso":4,
        "Valor":30,
        "Coste":15,
        "Coste_a":15,
        "Provincia":"Cobre",
    },
    "Bronce":{
        "Inputs":{
            "Cobre":2
        },
        "Peso":4,
        "Valor":65,
        "Coste":15,
        "Coste_a":45,
        "Provincia":None,
    },
    "Muebles_madera":{
        "Inputs":{
            "Madera":1
        },
        "Peso":2,
        "Valor":27,
        "Coste":10,
        "Coste_a":17,
        "Provincia":None,
    },
    "Muebles_hierro":{
        "Inputs":{
            "Hierro":1
        },
        "Peso":2,
        "Valor":35,
        "Coste":10,
        "Coste_a":25,
        "Provincia":None,
    },
    "Muebles_cobre":{
        "Inputs":{
            "Cobre":1
        },
        "Peso":2,
        "Valor":35,
        "Coste":10,
        "Coste_a":25,
        "Provincia":None,
    },
    "TTRR":{
        "Inputs":{},
        "Peso":4,
        "Valor":20,
        "Coste":15,
        "Coste_a":15,
        "Provincia":"TTRR",
    },
    "TTRR_proc":{
        "Inputs":{
            "TTRR":4
        },
        "Peso":3,
        "Valor":100,
        "Coste":20,
        "Coste_a":80,
        "Provincia":None,
    },
    "Vias":{
        "Inputs":{
            "Bronce":1
        },
        "Peso":5,
        "Valor":125,
        "Coste":15,
        "Coste_a":60,
        "Provincia":None,
    },
    "Radio":{
        "Inputs":{
            "TTRR_proc":2
        },
        "Peso":2,
        "Valor":240,
        "Coste":25,
        "Coste_a":185,
        "Provincia":None,
    },
    "Procesador":{
        "Inputs":{
            "Bronce":3,
            "TTRR_proc":2
        },
        "Peso":2,
        "Valor":400,
        "Coste":25,
        "Coste_a":320,
        "Provincia":None,
    },
    "Armas_prim":{
        "Inputs":{
            "Hierro":1
        },
        "Peso":3,
        "Valor":None,
        "Coste":15,
        "Coste_a":30,
        "Provincia":None,
    },
    "Armas_Hierro":{
        "Inputs":{
            "Hierro_proc":1
        },
        "Peso":3,
        "Valor":None,
        "Coste":15,
        "Coste_a":45,
        "Provincia":None,
    },
    "Armas_Acero":{
        "Inputs":{
            "Acero":1
        },
        "Peso":3,
        "Valor":None,
        "Coste":15,
        "Coste_a":150,
        "Provincia":None,
    },
    "Misiles":{
        "Inputs":{
            "Acero":1,
            "Radio":1
        },
        "Peso":5,
        "Valor":None,
        "Coste":20,
        "Coste_a":340,
        "Provincia":None,
    },
    "Guerra_elec":{
        "Inputs":{
            "Acero":1,
            "Procesador":1
        },
        "Peso":5,
        "Valor":None,
        "Coste":20,
        "Coste_a":475,
        "Provincia":None,
    }
}


class Pais:
    def __init__ (self, nombre, recursos,infraestructura,mercado = 0):
        self.lista_unidades = list()
        paises[nombre] = self
        self.nombre = nombre
        self.infraestructura = infraestructura
        self.lista_prov = list()
        self.act_lista_prov()
        self.dic_revueltas = dict()
        self.lista_fabricas = list()
        self.recursos = recursos
        self.productos = dict()
        self.mercado = Mercado(mercado)
        self.act_lista_fabricas()

    #funcion que sirve para asignar unos recursos de partida a los paises
    def update_recursos(self,x):
        self.recursos = x

    def check_rev(self):#genera las revueltas a nivel de pais
        self.dic_revueltas.clear()
        for i in self.lista_prov:
            self.dic_revueltas[i.ID] = i.check_rev()
            if(self.dic_revueltas[i.ID] != None):#las revueltas se expanden a las provincias adyacentes
                for e in self.lista_prov:
                    if e.ID in i.adyacentes:
                        if(e.check_rev() != None and e.pais == self):
                            self.dic_revueltas[e.ID] = self.dic_revueltas[i.ID]

    def act_lista_fabricas(self):
        self.lista_fabricas.clear()
        for i in self.lista_prov:
            self.lista_fabricas = self.lista_fabricas + i.lista_fabricas
        self.lista_fabricas.sort(key = lambda x: x.prioridad, reverse=False)
    def act_lista_prov(self):
        self.lista_prov.sort(key=lambda x:x.prioridad,reverse=False)
    def asignar_recursos(self):
        self.act_lista_fabricas()
        for i in self.lista_fabricas:
            i.calcular_necesidades()
            if(i.necesidades==None):
                continue
            for e in i.necesidades.keys():
                if e in self.recursos.keys():
                    if self.recursos[e] > i.necesidades[e]:
                        i.recursos[e] = i.necesidades[e]
                        self.recursos[e] = self.recursos[e]- i.necesidades[e]
                    else:
                        i.recursos[e] = self.recursos[e]
                        del self.recursos[e]
    def calcular_productos(self):
        self.act_lista_fabricas()
        bucleador = True
        prod = dict()
        while(bucleador == True):
            self.asignar_recursos()
            for i in self.lista_fabricas:
                agregar = i.calcular_productos()
                if(agregar!= 0):
                    if i.tipo in prod.keys():
                        prod[i.tipo] = prod[i.tipo] + agregar
                    else:
                        prod[i.tipo] = agregar
            if(len(prod)==0):
                bucleador = False
            for i in self.lista_fabricas:
                i.devolver_recursos()
            for i in prod.keys():
                if i in self.productos.keys():
                    self.productos[i] = self.productos[i] + prod[i]
                else:
                    self.productos[i] = prod[i]
            prod.clear()
    def agregar(self):
        for i in self.productos.keys():
            if i in self.recursos.keys():
                self.recursos[i] = self.recursos[i] + self.productos[i]
            else:
                self.recursos[i] = self.productos[i]
        self.productos.clear()

    def vender(self,tipo,cantidad,coste_comer=coste_comer,elementos=elementos):#función para vender mercancías (devuelve el coste de comercialización)
        if not tipo in self.recursos.keys():
            return
        if cantidad > self.recursos[tipo]:
            cantidad = self.recursos[tipo]
        coste = cantidad*elementos[tipo]["Peso"]*coste_comer[self.infraestructura]
        if "sui" in self.recursos.keys():
            self.recursos["sui"] += cantidad*self.mercado.precios[tipo]-coste
        else:
            self.recursos["sui"] = cantidad*self.mercado.precios[tipo]-coste
        self.recursos[tipo] = self.recursos[tipo]-cantidad
        if self.recursos[tipo] <= 0:
            self.recursos.pop(tipo)
        return coste
    def mejorar_infraestructa(self,coste_infra=coste_infra):
        for i in coste_infra[self.infraestructura+1].keys():
            if i not in self.recursos.keys():
                return 0
            if coste_infra[self.infraestructura+1][i] < self.recursos.get(i):
                return 0
        for i in coste_infra[self.infraestructura+1].keys():
            self.recursos[i] = self.recursos[i]-coste_infra[self.infraestructura+1][i]
            if self.recursos[i]<=0:
                self.recursos.pop(i)
        self.infraestructura = self.infraestructura+1
    def calcular_stock(self,elementos = elementos):
        coste = 0
        for i in self.recursos.keys():
            coste = coste + self.recursos[i]*coste_stock[self.infraestructura]*elementos[i]["Peso"]
        return coste
    def consumir_alimentos(self):
        for i in self.lista_prov:
            i.consumo_alimentos()

class Provincia:
    def __init__(self, ID, nombre, desarrollo, revueltas, adyacentes, pais,prioridad,clima, recurso = None, control=True):
        self.lista_unidades = list()
        self.clima = clima
        self.ID = ID
        self.prioridad = prioridad
        self.pais_n = pais
        self.pais = paises[pais]
        self.nombre = nombre
        self.desarrollo = desarrollo
        self.revueltas = revueltas
        self.adyacentes = adyacentes
        self.recurso = recurso
        self.control = control
        self.lista_fabricas = list()
        self.pais.lista_prov.append(self)
    def check_conflicto(self):
        if len(self.lista_unidades)>1:
            pass
    def check_rev(self):
        x = random.randint(0, 100)
        r_revueltas = max(self.revueltas.values())
        if x <= r_revueltas:
            self.control = False
            return list(self.revueltas.keys())[list(self.revueltas.values()).index(max(self.revueltas["baja"],self.revueltas["alta"],self.revueltas["media"]))]
        return None

    def consumo_alimentos(self):
        consumo1 = Coste_desarrollo[self.desarrollo]["Consumo_alimentos"]
        consumo2 = Coste_desarrollo[self.desarrollo]["Consumo_alimentos_proc"]
        consumo3 = Coste_desarrollo[self.desarrollo]["Consumo_alimentos_lux"]

        if "Alimentos" in self.pais.recursos.keys() and self.pais.recursos["Alimentos"] >= consumo1:
            self.pais.recursos["Alimentos"] = self.pais.recursos["Alimentos"] - consumo1
        else:
            self.pais.recursos["Alimentos"] = 0
            self.revueltas["baja"] += 10
            if self.revueltas["baja"] > 100:
                self.revueltas["baja"] = 100
            self.pais.recursos.pop("Alimentos")

        if "Alimentos_proc" in self.pais.recursos.keys() and self.pais.recursos["Alimentos_proc"] >= consumo2:
            self.pais.recursos["Alimentos_proc"] = self.pais.recursos["Alimentos_proc"] - consumo2
        else:
            self.pais.recursos["Alimentos_proc"] = 0
            self.revueltas["media"] += 10
            if self.revueltas["media"] > 100:
                self.revueltas["media"] = 100
            self.pais.recursos.pop("Alimentos_proc")

        if "Alimentos_lux" in self.pais.recursos.keys() and self.pais.recursos["Alimentos_lux"] >= consumo3:
            self.pais.recursos["Alimentos_lux"] = self.pais.recursos["Alimentos_lux"] - consumo3
        else:
            self.pais.recursos["Alimentos_lux"] = 0
            self.revueltas["alta"] += 10
            if self.revueltas["alta"] > 100:
                self.revueltas["alta"] = 100
            self.pais.recursos.pop("Alimentos_lux")


    def mejorar_des(self):
        if(self.desarrollo < 5):
            if self.pais.recursos["sui"] >= Coste_desarrollo[self.desarrollo]["Coste_mejora"]:
                self.pais.recursos["sui"] = self.pais.recursos["sui"] - Coste_desarrollo[self.desarrollo+1]["Coste_mejora"]
                self.desarrollo = self.desarrollo + 1
                if self.pais.recursos["sui"] <= 0:
                    self.pais.recursos.pop("sui")


class Mercado:
    def __init__(self,prefab = 0,elementos=elementos):
        self.pais = Pais
        self.precios = dict()
        if prefab == 0:
            for i in elementos.keys():#se incializan los precios a los valores cuando se crea un país
                if elementos[i]["Valor"] != None:
                    self.precios[i] = elementos[i]["Valor"]
        else:
            for i in prefab.keys():
                self.precios[i] = prefab[i]
    def act_precios(self,elementos=elementos):#los precios vienen dados por una distribución normal
        for i in self.precios.keys():
            self.precios[i]  = int(numpy.random.normal(elementos[i]["Valor"],elementos[i]["Valor"]*0.25))

class Unidad:
    def __init__(self, identificador, pais,provincia,numero):
        self.identificador = identificador
        self.pais = pais
        self.provincia_n = provincia
        self.provincia = provincias[provincia]
        self.provincia.lista_unidades.append(self)
        self.numero = numero
        self.pais.lista_unidades.append(self)
    def mover(self,destino):
        if destino.ID in self.provincia.adyacentes:
            if destino.clima == "agua" and self.provincia.clima !="agua":
                coste = self.numero *0.5
                if self.pais.recursos.get("sui") >= coste:
                    self.pais.recursos["sui"] = self.pais.recursos["sui"]-coste
                    if self.pais.recursos["sui"] <= 0:
                        self.pais.recursos.pop("sui")
                else:
                    return False
            for i in destino.lista_unidades:
                if self.pais == i.pais:
                    self.provincia.lista_unidades.remove(self)
                    i.numero = i.numero + self.numero
                    del self
                    return True
            if len(destino.lista_unidades)<=2:
                self.provincia.lista_unidades.remove(self)
                self.provincia = destino
                destino.lista_unidades.append(self)
                return True
        return False

class Fabrica:
    def __init__(self, nombre, tipo, provincia, categoria, prioridad, elementos=elementos, tabla_cat=Coste_exp_categoria):
        self.nombre = nombre
        self.tipo = tipo
        self.provincia = provincias[provincia]
        self.provincia_n =provincia
        self.categoria = categoria
        self.prioridad = prioridad
        self.inputs = dict()
        self.inputs = elementos[tipo]["Inputs"]
        self.inputs["sui"] = elementos[tipo]["Coste"]
        self.recurso = elementos[tipo]["Provincia"]
        self.provincia.lista_fabricas.append(self)
        self.capacidad = Coste_exp_categoria[self.categoria]["Capacidad"]
        self.necesidades = dict()
        self.recursos = dict()
        self.calcular_necesidades()

    def calcular_necesidades(self):
        if self.inputs == None:
            self.necesidades = 1
            return
        for i in self.inputs.keys():
            self.necesidades[i] = self.inputs[i]*self.capacidad
    def calcular_productos(self):
        if len(self.recursos) == 0:
            self.produccion = 0
            return 0
        limites = dict()
        for i in self.necesidades.keys():#se busca el factor limitante de la producción
            if i in self.recursos.keys():
                limites[i] = self.recursos[i]/self.inputs[i]
            else:
                self.produccion = 0
                return 0
        limite = list(limites.keys())[list(limites.values()).index(min(limites.values()))]
        self.produccion = limites[limite]
        self.consumir_productos()
        self.produccion = int(self.produccion)
        self.capacidad = self.capacidad - self.produccion
        return self.produccion
    def consumir_productos(self):#una vez asignada la producción los recursos utilizados se consumen
        for i in self.recursos.keys():
            self.recursos[i] = int(self.recursos[i] - self.produccion*self.inputs[i])
    def mejorar(self,Coste_exp_categoria = Coste_exp_categoria): #aumento la categoría de una fábrica   ESTO HAY QUE CAMBIARLO DE TAL MODO QUE NO HAYA QUE ELEGIR QUE TIPO DE MUEBLE USAR
        if self.categoria < 5:
            cantidad = Coste_exp_categoria[self.categoria+1]["Coste_exp_m"]
            if "Muebles_cobre" in self.provincia.pais.recursos.keys():
                if self.provincia.pais.recursos["Muebles_cobre"]<cantidad/1.66:
                    cantidad = math.ceil(cantidad -self.provincia.pais.recursos["Muebles_cobre"]*1.66)
                    self.provincia.pais.recursos.pop("Muebles_cobre")
                else:
                    self.provincia.pais.recursos["Muebles_cobre"] = int(self.provincia.pais.recursos["Muebles_cobre"]-(cantidad/1.66))
                    if self.provincia.pais.recursos["Muebles_cobre"] <= 0:
                        self.provincia.pais.recursos.pop("Muebles_cobre")
                    self.categoria = self.categoria+1
                    return 1
            if "Muebles_hierro" in self.provincia.pais.recursos.keys():
                if self.provincia.pais.recursos["Muebles_hierro"]<cantidad/1.66:
                    cantidad = math.ceil(cantidad -self.provincia.pais.recursos["Muebles_hierro"]*1.66)
                    self.provincia.pais.recursos.pop("Muebles_hierro")
                else:
                    self.provincia.pais.recursos["Muebles_hierro"] = int(self.provincia.pais.recursos["Muebles_hierro"]-(cantidad/1.66))
                    if self.provincia.pais.recursos["Muebles_hierro"] <= 0:
                        self.provincia.pais.recursos.pop("Muebles_hierro")
                    self.categoria = self.categoria+1
                    return 1
            if "Muebles_madera" in self.provincia.pais.recursos.keys():
                if self.provincia.pais.recursos["Muebles_madera"]<cantidad/1.66:
                    cantidad = math.ceil(cantidad -self.provincia.pais.recursos["Muebles_madera"])
                    self.provincia.pais.recursos.pop("Muebles_madera")
                else:
                    self.provincia.pais.recursos["Muebles_madera"] = int(self.provincia.pais.recursos["Muebles_madera"]-cantidad)
                    if self.provincia.pais.recursos["Muebles_madera"] <= 0:
                        self.provincia.pais.recursos.pop("Muebles_madera")
                    self.categoria = self.categoria+1
                    return 1
        return 0
    def devolver_recursos(self):#los recursos asigandos a la fábrica que no se han consumido se devuelven a la pool
        for e in self.recursos.keys():
            if self.recursos[e]>0:
                if e in self.provincia.pais.recursos:
                    self.provincia.pais.recursos[e] = self.provincia.pais.recursos[e]+self.recursos[e]
                else:
                    self.provincia.pais.recursos[e] = self.recursos[e]
        self.recursos.clear()

def intercambio(pais1,pais2,elemento1,elemento2,cantidad1,cantidad2):
    if not elemento1 in pais1.recursos.keys() or not elemento2 in pais2.recursos.keys():
        return
    if cantidad1 < pais1.recursos[elemento1] or cantidad2 < pais2.recursos[elemento2]:
        return
    pais1.recursos[elemento1] = pais1.recursos[elemento1] - cantidad1
    pais2.recursos[elemento2] = pais2.recursos[elemento2] - cantidad2
    if pais1.recursos[elemento1] <= 0:
        pais1.recursos.pop(elemento1)
    if pais2.recursos[elemento2] <= 0:
        pais2.recursos.pop(elemento2)
    if elemento2 in pais1.recursos.keys():
        pais1.recursos[elemento2] = pais1.recursos[elemento2] + cantidad2
    else:
        pais1.recursos[elemento2] = cantidad2
    if elemento1 in pais2.recursos.keys():
        pais2.recursos[elemento1] = pais1.recursos[elemento1] + cantidad1
    else:
        pais2.recursos[elemento1] = cantidad1

def Construir_fabrica(nombre, tipo, provincia, categoria, prioridad, elementos=elementos,coste_exp_categoria = Coste_exp_categoria):
    recurso = elementos[tipo]["Provincia"]
    if recurso == provincia.recurso and provincia.clima != "agua":
        cantidad = coste_exp_categoria[categoria]["Coste_apert_m"]
        if "Muebles_cobre" in provincia.pais.recursos.keys():
            if provincia.pais.recursos["Muebles_cobre"]<cantidad/1.66:
                cantidad = math.ceil(cantidad -provincia.pais.recursos["Muebles_cobre"]*1.66)
                provincia.pais.recursos.pop("Muebles_cobre")
            else:
                provincia.pais.recursos["Muebles_cobre"] = int(provincia.pais.recursos["Muebles_cobre"]-(cantidad/1.66))
                if provincia.pais.recursos["Muebles_cobre"] <= 0:
                    provincia.pais.recursos.pop("Muebles_cobre")
                return Fabrica(nombre, tipo, provincia, categoria, prioridad)
        if "Muebles_hierro" in provincia.pais.recursos.keys():
            if provincia.pais.recursos["Muebles_hierro"]<cantidad/1.66:
                cantidad = math.ceil(cantidad -provincia.pais.recursos["Muebles_hierro"]*1.66)
                provincia.pais.recursos.pop("Muebles_hierro")
            else:
                provincia.pais.recursos["Muebles_hierro"] = int(provincia.pais.recursos["Muebles_hierro"]-(cantidad/1.66))
                if provincia.pais.recursos["Muebles_hierro"] <= 0:
                    provincia.pais.recursos.pop("Muebles_hierro")
                return Fabrica(nombre, tipo, provincia, categoria, prioridad)
        if "Muebles_madera" in provincia.pais.recursos.keys():
            if provincia.pais.recursos["Muebles_madera"]<cantidad/1.66:
                cantidad = math.ceil(cantidad -provincia.pais.recursos["Muebles_madera"])
                provincia.pais.recursos.pop("Muebles_madera")
            else:
                provincia.pais.recursos["Muebles_madera"] = int(provincia.pais.recursos["Muebles_madera"]-cantidad)
                if provincia.pais.recursos["Muebles_madera"] <= 0:
                    provincia.pais.recursos.pop("Muebles_madera")
                return Fabrica(nombre, tipo, provincia, categoria, prioridad)
        return 0
    else:
        return 0

""" Formato para las revueltas {"baja":X,"media":Y,"alta":Z} """
rebeldes = Pais("rebeldes",{},1,0)
paises.pop("rebeldes")
def lectura_datos():
    #leemos los datos del json de paises
    doc_paises = open("paises.json","r")
    dic_paises = json.load(doc_paises)
    doc_paises.close()
    for i in dic_paises.keys():
        i = Pais(i,dic_paises[i]["recursos"],dic_paises[i]["infra"],dic_paises[i]["mercado"])

    #leemos los datos del json de provincias
    doc_prov = open("provincias_t.json","r")
    dic_prov = json.load(doc_prov)
    doc_prov.close()
    for i in dic_prov.keys():
        provincias[i] = Provincia(i,dic_prov[i]["nombre"],dic_prov[i]["desarrollo"],dic_prov[i]["revueltas"],dic_prov[i]["adyacentes"],dic_prov[i]["pais"],dic_prov[i]["prioridad"],dic_prov[i]["clima"],dic_prov[i]["recurso"],dic_prov[i]["control"])
    #leemos los datos de las fabricas
    for i in paises.keys():
        for e in dic_paises[i]["fabricas"]:
            e = Fabrica(e["nombre"],e["tipo"],e["provincia"],e["categoria"],e["prioridad"])
    for i in paises.keys():
        paises[i].act_lista_fabricas()
    #leemos los datos de las unidades
    for i in paises.keys():
        for e in dic_paises[i]["unidades"]:
            e = Unidad(e["ID"],paises[i],e["provincia"],e["numero"])
    #leemos los datos de las unidades rebeldes
    doc_revueltas = open("rev.json")
    dic_revueltas = json.load(doc_revueltas)
    doc_revueltas.close()
    for i in dic_revueltas:
        x = Unidad(i["ID"],rebeldes,i["provincia"],i["numero"])
def guardar_datos():
    #actualizamos los datos del json de paises
    dic_paises_f = dict()
    dic_provincias_f = dict()
    for i in paises.keys():
        dic_paises_f[i] = {"infra":paises[i].infraestructura,"recursos":paises[i].recursos,"nombre":i,"mercado":paises[i].mercado.precios}
    #actualizamos las fabricas
    for i in paises.keys():
        dic_paises_f[i]["fabricas"] = list()
        for e in range(len(paises[i].lista_fabricas)):
            dic_paises_f[i]["fabricas"].append(dict())
            dic_paises_f[i]["fabricas"][e] = {"nombre":paises[i].lista_fabricas[e].nombre,"tipo":paises[i].lista_fabricas[e].tipo,"categoria":paises[i].lista_fabricas[e].categoria,"provincia":paises[i].lista_fabricas[e].provincia_n,"prioridad":paises[i].lista_fabricas[e].prioridad}
    #actualizamos las unidades
    for i in paises.keys():
        dic_paises_f[i]["unidades"] = list()
        for e in range(len(paises[i].lista_unidades)):
            dic_paises_f[i]["unidades"].append(dict())
            dic_paises_f[i]["unidades"][e] = {"ID":paises[i].lista_unidades[e].identificador,"numero":paises[i].lista_unidades[e].numero,"provincia":paises[i].lista_unidades[e].provincia_n} 
    #actualizamos las unidades rebeldes
    dic_revueltas_f = list()
    for i in rebeldes.lista_unidades:
        dic_revueltas_f.append({"ID":i.identificador,"numero":i.numero,"provinicia":i.provincia_n})
    #actualizamos los datos del json de paises
    json_paises_f = json.dumps(dic_paises_f,indent=4,sort_keys=True)
    doc_paises = open("paises.json","w")
    doc_paises.write(json_paises_f)
    doc_paises.close()
    for i in provincias.keys():
        dic_provincias_f[i] = {"nombre":provincias[i].nombre,"desarrollo":provincias[i].desarrollo,"clima":provincias[i].clima,"control":provincias[i].control,"prioridad":provincias[i].prioridad,"adyacentes":provincias[i].adyacentes,"recurso":provincias[i].recurso,"pais":provincias[i].pais_n,"revueltas":provincias[i].revueltas}
    doc_provincias = open("provincias_t.json","w")
    doc_provincias.write(json.dumps(dic_provincias_f,indent=4,sort_keys=True))
    doc_provincias.close()
#ORDEN DEL JUEGO
#1 SE LEEN LOS DATOS DE LOS JSONS
#2 SE LEEN LAS ORDENES Y SE EJECUTAN
#3 SE REALIZAN TODOS LOS CONSUMOS
#4 SE ALMACENAN DE NUEVO TODOS LOS DATOS EN LOS JSONS
lectura_datos()

#actualizamos los precios para el próximo turno
for i in paises.keys():
    paises[i].mercado.act_precios()
guardar_datos()

print("fin")