########################### Os Tipos de Métodos ########################################
########################################################################################

# @classmethod
# @staticmethod
# Private Method

import random

class Livro():
    ano_atual= 2022
    def __init__(self,titulo,autor,ano):
        self.titulo= titulo
        self.autor= autor
        self.ano= ano
        
    
    ## Método de classe usando a função decoradora ##
    @classmethod
    def calculoanopublicacao(vclasse,nome,ano):
        calculo= vclasse.ano_atual - ano
        return(nome,'Tempo Publicação',str(calculo),'anos')
    
            
    
    ##### Método de Instância usa o self ####
    
    def imprime(self):
        print('Esse livro é %s e o Autor %s' %(self.titulo,self.autor))
        
    def anopublicacao(self):
        print('Tempo de Publicação',self.ano_atual - self.ano, 'anos')
        
    
    
    
    #### Método Oculto ou Método Privado ###  Private Method - pouco utilizado
    
    def __autor(self):
        return(self.autor)
    
    
    
    ### Método Estático ###
    
    @staticmethod
    def geraisbn():
        isbn= random.randint(0,1000)
        return isbn    
        



## Testando as Instâncias

## Valores e objetos criados a partir da instância(self)
livro1= Livro('O Pescador','José Cunha',1988)
livro1.imprime()
livro1.anopublicacao()




## Usando Métodos de Classe

## Esse objeto não nasceu a partir do namespace self(Próprios Atributos)
# Esse objeto foi instanciado a partir de valores criados nos parâmetros do método de classe

livro2= Livro.calculoanopublicacao('Livro Por Classe',1984)
print(livro2)

livro3= Livro('Mobby Dick', 'Gasparzinho', 1970)
print(livro3.autor)
print(livro3._Livro__autor())

livro3.geraisbn()
print(livro3.geraisbn())
print(livro3.__dict__)


