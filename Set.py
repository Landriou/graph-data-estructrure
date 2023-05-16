from algo1 import *

def findSet(L,x):
    currentnode = L.head
    while currentnode != None:
        if searchArray(currentnode,x) != None:
            return currentnode
        currentnode = currentnode.nextNode
    return None

def searchArray(A,x):
    pos = 0
    for n in range(len(A.value)):
        if A.value[n] == int(x):
            return pos
        pos = pos + 1
    return None

def Union(vector1, vector2):
  k = 0
  vector1 = Create_set(vector1)
  vector2 = Create_set(vector2)
  lentotal = len(vector1) + len(vector2)    #Hago un vector que sea del tamaño de ambos vectores
  vectorunion = Array(lentotal,0)         
  for n in range(len(vector1)):       #Paso los elementos del primer vector al vector resultante
    vectorunion[n] = vector1[n]
  for i in range(len(vector1), lentotal): #Hago lo mismo pero a partir de donde se quedo
    vectorunion[i] = vector2[k]
    k = k + 1
  vectorunion = Create_set(vectorunion) #Elimino los repetidos
  return vectorunion

def repetidos(array):
  repetido = 0
  for n in range(len(array)):
    for j in range(n+1, len(array)):
        if array[n] == array[j] and array[j]!= None:
          array[j] = None
          repetido = repetido + 1
        
  return repetido

def unicidad(array, arraysinrepetidos):
  i = 0
  for n in range(len(array)):
    if array[n] == None:
      print("Eliminando elemento repetido ")
    else:  
      arraysinrepetidos[i] = array[n] 
      i= i + 1
  return arraysinrepetidos


def Create_set(array):
  Arrayunico = Array(len(array) - repetidos(array), 0)
  array = unicidad( array , Arrayunico)
  return array