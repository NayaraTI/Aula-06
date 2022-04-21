from classes_revendedora import Revendedora

class RevendedoraMotos(Revendedora):
    def __init__(self):
        super().__init__()
        print('Moto Cadastrada')
        
    def marca(self,marca):
        self.marca= marca
        print("Marca Adicionada")
        
    def modelo(self,modelo):
        self.modelo= modelo
        print(" Modelo Adicionado")
        
    def potencia(self,potencia):
        self.potencia= str(potencia)
        print('Potencia Adicionada')