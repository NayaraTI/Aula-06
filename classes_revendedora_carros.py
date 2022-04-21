## Classe filha da classe revendedora ###

from classes_revendedora import Revendedora

## Exemplo de Herança de Atributos do pai e criação de atributos próprios do filho

"""
class RevendedoraCarros(Revendedora):
    def __init__(self,nome,sobrenome,atributodofilho)
        super().__init__(nome,sobrenome)
        
        self.atributodofilho= atributodofilho
      
      
"""        

class RevendedoraCarros(Revendedora):
    def __init__(self):
        super().__init__()
        print("Carro Cadastrado")
        
    def marca(self,marca):
        self.marca= marca
        print('Marca Adicionada')
        
    def modelo(self,modelo):
        self.modelo= modelo
        print('Modelo Adicionado')
    
        
            
            