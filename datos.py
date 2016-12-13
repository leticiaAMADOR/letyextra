import json

class data:  
    data = []

    def read(self):
        with open('clientes.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

    def getClientes(self): 
        clientes = []
        for row in self.data:
            data = row['nom']
            if cliente not in datas:
                data.append(data)
        return data

    
                
class data1:  
    peli = []

    def read(self):
        with open('peliculas.json','r') as file:
            peli = json.load(file)
            self.data1 = peli['results'] 

    def getPeliculas(self): 
        data1 = []
        for row in self.data1:
            peli = row['nom']
            if peli not in data1:
                data1.append(peli)
        return data1