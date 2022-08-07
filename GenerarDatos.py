import random

lista = [] 


for x in range (1000000): #Se crean los valores 
    
    lista.append(x)   
    
print(len(lista)) # Se verifica la cantidad de valores 

random.shuffle(lista) # Se desordena esa monda

for x in range (1000000): # se verifica que este desordenado
    
    print(lista[x]) 


    

    
    