from linkedlist import *
from algo1 import *
from random import randint

def MergeSort(L):
    large = length(L)
    if large == 1:
        return L #Si la lista es de lenght 1, retorno la lista para el merge
    mid = int(large/2)
    Le = LinkedList() #Creo la lista izquierda
    currentnode = L.head
    for n in range(0,mid): #Paso los elementos hasta la mitad
        add(Le,currentnode.value)
        currentnode = currentnode.nextNode
    R = LinkedList() #Creo la lista derecha
    for u in range(mid+1,large +1 ): #Lo mismo
        add(R,currentnode.value)
        currentnode = currentnode.nextNode
    Left = MergeSort(Le) #Llamo a la recursividad del lado izquierdo y lo guardo
    Right = MergeSort(R) #LLamo a la recursividad del lado derecho y lo guardo
    return gitmerge(Left,Right) #Merge a los resultados
#Funcion que mergea 2 listas en 1  y los ordena
def gitmerge(L,R):
    Lfinal = LinkedList()
    largeL = length(L)
    largeR = length(R)
    i = j = 0
    nodeleft = L.head
    noderight = R.head
    for k in range (0, largeL+largeR): #Comparo los values de las listas y los voy agregando ordenados
        if nodeleft == None:
            add(Lfinal,noderight.value)
            noderight = noderight.nextNode
            continue
        if noderight == None:
            add(Lfinal,nodeleft.value)
            nodeleft = nodeleft.nextNode
            continue
        if nodeleft.value.weight <= noderight.value.weight:
            add(Lfinal,nodeleft.value)
            nodeleft = nodeleft.nextNode
        else:
            add(Lfinal, noderight.value)
            noderight = noderight.nextNode
    Lfinal = inverse(Lfinal) #le doy inverse para que queden ordenados de menor a mayor
    return Lfinal