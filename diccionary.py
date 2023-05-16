class Diccionary:
    head=None

class Diccionarynode:
    value=None
    nextNode=None
    key=None

#Añade un elemento a la lista
def add(L, element, key):
    NodeA = Diccionarynode()
    NodeA.value = element
    NodeA.key = key
    NodeA.nextNode = L.head
    L.head = NodeA
#Devuelve la posicion de un elemento pasado por parametros
def search(L, key):
    currentnode = L.head
    posicion = 0    
    while currentnode != None:
        if currentnode.key == key:
            return posicion
        posicion = posicion + 1
        currentnode = currentnode.nextNode
    return None

def searchValue(L, key):
    currentnode = L.head
    while currentnode != None:
        if currentnode.key == key:
            return currentnode.value
        currentnode = currentnode.nextNode
    return None

#Devuelve la cantidad de elementos en la lista
def length(L):
    currentnode = L.head
    cant = 0
    while currentnode != None:
        cant = cant + 1
        currentnode = currentnode.nextNode
    return cant

#De igual forma q en insert
def delete(L, key):
    wanted = search(L,key)
    if wanted == None:
        return None
    flag = True
    contador = 0 
    nodoanterior = 0
    nodoposterior = 0
    currentnode = L.head
    if wanted == 0:
        for n in range(length(L)-1):
            currentnode.value = currentnode.nextNode.value
            if n != length(L)-2:
                currentnode = currentnode.nextNode
        currentnode.nextNode = None
        return wanted
    while flag:
        contador = contador + 1
        if contador == wanted:
            flag = False
        nodoanterior = currentnode
        nodoposterior = currentnode.nextNode.nextNode
        currentnode = currentnode.nextNode
    nodoanterior.nextNode = nodoposterior
    return wanted

def H(k):
    return k % 9

def imprimirlista(L):
    currentnode = L.head
    while currentnode != None:
        print(currentnode.value, end="  ")
        currentnode = currentnode.nextNode


def dic_insert(D,key,value,hashresult):
    if D[hashresult] == None:
        D[hashresult] = Diccionary()
        add(D[hashresult],value,key)
    else:
        add(D[hashresult],value,key)

def dic_search(D,key,hashresult):
    return searchValue(D[hashresult],key)

def dic_delete(D,key,hashresult):
    delete(D[hashresult],key)
