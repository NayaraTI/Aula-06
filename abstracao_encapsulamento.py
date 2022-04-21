import cProfile
import datetime

class Pessoa():
    anoatual= datetime.date.today().year
    def __init__(self,nome,sobrenome,cpf,anonascimento):
        self.nome= nome
        self.sobrenome= sobrenome
        self.__cpf = cpf  # encapsulado
        self._anonascimento= anonascimento  # abstraído
        
    @classmethod
    def __idade(vanoatual, _anonascimento):
        calculaidade= vanoatual.anoatual - _anonascimento
        print('Idade é:', calculaidade)
        
        
## Instanciar os objetos

p1= Pessoa('João',"Cavichiolli", 444333, 1985)

## Exibir atributos protected

#print(p1._anonascimento)

## Exibir os métodos de classe

#p1.idade(1985)

## Exibir Atributos Privados

#p1.__cpf

## Exibir Atributo Privado com Naming Mangling

#print(p1._Pessoa__cpf)


# Exibir Método de classe privado usando naming mangling

(p1._Pessoa__idade(1985))    
        
        