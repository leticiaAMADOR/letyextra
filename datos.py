import json

class Clientes:  
    dato = []

    def read(self):
        with open('clientes.json','r') as file:
            dato = json.load(file)
            self.data = dato['results'] 

    def getClientes(self): 
        clientes = []
        for row in self.data:
            dato = row['nom']
            if dato not in clientes:
                clientes.append(dato)
        return clientes

    
                
class Peliculas:  
    dato2 = []

    def read(self):
        with open('peliculas.json','r') as file:
            dato2 = json.load(file)
            self.data1 = dato2['results'] 

    def getPeliculas(self): 
        dato2 = []
        for row in self.data1:
            dato2 = row['nom']
            if dato2 not in peliculas:
                peliculas.append(dato2)
        return peliculas