import json

def gerar_id(lista=[]):
    cont = 1 
    for i in lista:
        cont += 1 
    
    return cont 



def jsonificar(dicionario):
    with open ('dados.json','w') as lista_jaison:
        json.dump(dicionario,lista_jaison,indent=4)
    

def desjsonificar():
    with open ('dados.json','r') as lista_jaison:
        lista = json.load(lista_jaison)
    
    return lista
