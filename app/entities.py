class carro():
    
    #metodo constructor
    def __init__(self, placa , tipo_vehiculo):
        self.placa = placa 
        self.tipo_vehiculo = tipo_vehiculo
    
    
class cliente():
    
    #metodo constructor
    def __init__(self, 
                 nombre , 
                 celular , 
                 documento,
                 lista_carros 
                 ):
        self.nombre = nombre
        self.celular = celular
        self.documento = documento
        self.lista_carros = lista_carros
        
    def addcar(self , car):
        self.lista_carros.append(car)
        
    def listcar(self):
        for i in self.lista_carros:
            print("carro con placas: " + i.placa)
        
        
        
      