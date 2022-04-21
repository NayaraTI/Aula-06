############################## Tipos de Atributos #######################################
#########################################################################################

# Público, Privados e Protegidos #

# self.__nome = nome = Atributo Privado (duplo underline)
# self._nome = nome = Atributo Protegido (não pode ser herdado por outra classe)

class Cadastrouser():
    def __init__(self,usuario,senha):
        self.usuario= usuario
        self.__senha= senha
        

# Instanciar um objeto

user1= Cadastrouser('João','123456')

print(user1.usuario)

#print(user1._senha) # ocorre um erro por ser privado
                    
            
## Exibindo atributos privados com a função dir
# A função dir retorna as propriedades dos objetos, métodos e etc

print(dir(user1))

print(user1._Cadastrouser__senha)

print(user1.__dict__)


## Deletar uma instância

del user1.usuario

print(user1.__dict__)