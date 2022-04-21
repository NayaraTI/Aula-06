################################### Classe Principal ou SuperClasse ###############################
## Classe PAI
## Método super() que vai ser utilizar para herdar os atributos da classe pai

class Revendedora():
    def __init__(self):
        print('Veículo Cadastrado')
        
    def tipoveiculo(self,tipoveiculo):
        self.veiculo= tipoveiculo
        print('Tipo Adicionado')
        
    def quantidade(self,quantidade):
        self.quantidade= quantidade
        print("Quantidade Adicionada")
        
    def valor(self,valor):
        self.valor= valor
        print("Valor Adicionado")