#INTRIAGO FRANCO WASHINGTON EMMANUEl
###########################################################

#EJERCICIO EN PYTHON -Probar los métodos de las Listas en Python-


print("AGREGAR UN NUMERO A UNA LISTA -ESTE SE AGREGARA AL FINAL DE LA LISTA-")
def agregar(lista,n):
 lista.append(n)   
lista = [1,2,3,4,5]

print(lista)
n = 6

agregar(lista,n)


print (lista)

#########################################################
print ("Concatenar dos listas")
def extender_lista(lista1, lista2):
    lista1[len(lista1):] = lista2
    return lista1

numeros1 = [1, 2, 3]
print("los datos de la lista 1 son ", numeros1)
numeros2 = [4, 5, 6]
print("Los datos de la lista 2 son ",numeros2)

resultado = extender_lista(numeros1, numeros2)


print("la concatenacion de ambas listas",resultado)

#######################################################
print("tambien se puede usar utilizando un extend")

def concatenardiferente(lista1, lista2):
    lista1.extend(lista2)
    print(lista1)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenardiferente(lista1, lista2)










def insertar_elemento(lista, indice, elemento):
    lista.insert(indice, elemento)
    return lista

letras = ['a', 'b', 'c', 'd','e']  #washington intriago
indice = 5
elemento = 'f'
resultado = insertar_elemento(letras, indice, elemento)
print(resultado)

print("se eliminara un elemento de la lista")

def eliminar_elemento(lista, indice):
       lista.remove(lista[indice])
       return lista

lista = [1,2,3,4]
indice = 0
resultado = eliminar_elemento(lista,indice)
print(resultado)

##############################################
print("eliminar y obtener el ultimo dato de la la lista")
def obtener_ultimo_elemento(lista):
    ultimo_elemento = lista.pop()
    return ultimo_elemento                   #washington intriago

lista = [1, 2, 3]
print(lista)
ultimo_elemento = obtener_ultimo_elemento(lista)
print(lista)  
print(ultimo_elemento) 
#############################################

print("Cuenta cuantos elemenos n hay en la lista")
def contar_elemento(lista, elemento):
    conteo = lista.count(elemento)
    return conteo

lista = [1, 2, 3, 2, 4, 2]               #washington intriago
elemento = 4

conteo = contar_elemento(lista, elemento)

print(conteo)

##############################################
print("ordenar una lista de forma ascendete")

def ordenar_ascendente(lista):
    lista.sort()

lista = [3, 1, 4, 2]
print(lista)
ordenar_ascendente(lista)                              #washington intriago
print(lista)

###############################################
print("Esta funcion invierte la lista")
def invertir_lista(lista):
    lista.reverse()

lista = [1, 2, 3, 4]
invertir_lista(lista)
print(lista)  # Resultado: [4, 3, 2, 1]