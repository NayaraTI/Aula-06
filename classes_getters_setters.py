#### Os Getters deixam um atributo privado como público
# Ele transforma fazendo uma abstração

## Os Setters mudam o valor ou comportamento de um método ou atributo
# que sofreu abstração

## Encapsulamento é onde os atributos ou métodos estão privados dentro de uma classe
# Abstração está mudando o estado do atributo, aplicando getters


class Vendasprodutos():
    def __init__(self,produto,quantidade,valor):
        self.__produto= produto
        self.__quantidade= quantidade
        self.__valor= valor
        
    
    ### Aplicando o Getter ###
    @property                 # = Getter (Abstração)
    def produto(self):
        return self.__produto
    
    @property
    def quantidade(self):
        return self.__quantidade 
    
    @property
    def valor_total_compra(self):
        return self.__quantidade * self.__valor
    
    
    ## Aplicando o Setter ##
    @quantidade.setter
    def quantidade(self,nova_quantidade):
        self.__quantidade= nova_quantidade
        
        

# Instanciar um objeto

produto1= Vendasprodutos('Arroz',34,12.45)

#print(produto1.__produto)


produto1.quantidade= 45

print(produto1.quantidade)
print(produto1.produto)

print(produto1.valor_total_compra)