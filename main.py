## Arquivo Principal para importar as Classes

from classes_revendedora_carros import RevendedoraCarros

from classe_revendedora_motos import RevendedoraMotos

## Instanciando os objetos


## Carros

carro1= RevendedoraCarros()
carro1.modelo("Gol")
carro1.valor(34.700)
carro1.quantidade(3)
carro1.marca('Volks')
carro1.tipoveiculo('Carro')

print(carro1.__dict__)


## Motos

moto1= RevendedoraMotos()
moto1.tipoveiculo('Motocicleta')
moto1.valor(40.800)
moto1.marca('Honda')
moto1.modelo('CB1000')
moto1.potencia('1000CC')
