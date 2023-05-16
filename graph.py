from algo1 import *
from linkedlist import *
from Set import *
def createGraph(V, A):
    Graph = Array(length(V),LinkedList())
    currentnode = V.head
    for i in range(len(Graph)):
        Graph[i] = LinkedList()
        add(Graph[i], currentnode.value)
        currentnode = currentnode.nextNode
    currentnodeA = A.head
    while currentnodeA != None:
        stri = String(currentnodeA.value)
        cant = 0
        for n in range(len(stri)):
            if stri[n] == ",":
                v1 = substr(stri,0,cant)
                break
            cant = cant + 1
        v2 = substr(stri,cant+1,len(stri))
        v1 = int(v1.arr.data)
        v2 = int(v2.arr.data)
        if v1 == v2:
            add(Graph[v1],v1)
        else:
            add(Graph[v1], v2)
            add(Graph[v2], v1)
        currentnodeA = currentnodeA.nextNode

    for j in range(len(Graph)):
        Graph[j] = inverse(Graph[j])
    return Graph

def existPath(Grafo, v1, v2):
    if v1 == v2:
        lista = LinkedList()
        return existCycleR(Grafo,v1,v1,None,lista,0)
    else:
        pos1 = searchInArrayGraph(Grafo,v1)
        #Busco en la lista del string v1 el string v2
        if searchInConexions(Grafo,pos1,v2) == True:
            return True
        else:
            L = LinkedList()
            add(L,pos1) #Creo una lista para los nodos en los que ya se busco asi no busco nuevamente
            currentnode = Grafo[pos1].head
            currentnode = currentnode.nextNode
            while currentnode != None: 
                if search(L,currentnode.value) == None: #Si la conexion no esta en la lista, llamo a la recursividad para buscar
                    if existPathWrapper(Grafo,currentnode.value,v2,L) == True:
                        return True
                    else:
                        currentnode = currentnode.nextNode
                else:
                    currentnode = currentnode.nextNode
            return False
def existPathWrapper(Grafo,pos,v2,L):
    exist = False
    if searchInConexions(Grafo,pos,v2) == True:
        return True
    else:
        add(L,pos)
        currentnode = Grafo[pos].head
        currentnode = currentnode.nextNode
        while currentnode != None:
            if search(L,currentnode.value) == None:
                exist = existPathWrapper(Grafo,currentnode.value,v2,L)
            currentnode = currentnode.nextNode
        return exist

def searchInArrayGraph(A,v): #Busco en el array el string correspondiente
    pos = 0
    for n in range(len(A)):
        if A[n].head.value == v:
            return pos
        pos = pos + 1
    return None

def searchInConexions(Grafo,pos,v): #Busco en la listas de conexiones el string correspondiente
    currentnode = Grafo[pos].head
    if search(Grafo[pos],pos):
        return True
    else:
        currentnode = currentnode.nextNode
    while currentnode != None:
        if Grafo[currentnode.value].head.value == v:
            return True
        currentnode = currentnode.nextNode
    return False


def isConnected(Grafo): #Hay que revisar si cada nodo tiene un camino hacia otro nodo
    for n in range(len(Grafo)):
        if existPath(Grafo,Grafo[0].head.value,Grafo[n].head.value) == False:
            return False
    return True

def isTree(Grafo): #Hay que revisar si cada nodo tiene un ciclo al mismo nodo
    for n in range(len(Grafo)):
        if existPath(Grafo,Grafo[n].head.value,Grafo[n].head.value) == True:
            return False
    return True

def isComplete(Grafo):
    for i in range(len(Grafo)-1):
        for j in range(i+1,len(Grafo)):
            if search(Grafo[i],j) == None:
                return False
    return True

def convertTree(Grafo):
    count = 0
    L = LinkedList()
    while isTree(Grafo) == False:
        if existPath(Grafo,Grafo[count].head.value,Grafo[count].head.value) == True:
            deleted = Grafo[count].head.nextNode.value
            deleteposition(Grafo[count],1)
            delete(Grafo[deleted],count)
            add(L, str(deleted) + "," + str(count))
    return L

def existCycleR(Grafo,v1,v2,before,lista,n): #La idea del es que busque en camino por donde no salio y para eso se usa el before como verificacion
    pos = searchInArrayGraph(Grafo,v1)

    if pos == None:
        return False
    
    currentNode= Grafo[pos].head.nextNode

    if search(Grafo[pos],searchInArrayGraph(Grafo,v2)) != None:
        if pos != before:
            return True
    
    add(lista,pos)
    while currentNode != None:
        if search(lista,currentNode.value) != None:
            currentNode=currentNode.nextNode
        else:
            if n == 0:
                before=currentNode.value
            if existCycleR(Grafo,Grafo[currentNode.value].head.value,v2,before,lista,n+1) == True:
                return True
    return False

#Ejercicio 7
def countConnections(Grafo):
    L = LinkedList()
    Aristoteles = extractArist(Grafo)
    Anode = Aristoteles.head
    for n in range(len(Grafo)):
        A = Array(1,0)
        A[0] = n
        add(L,A)
    while Anode != None:
        s = String(Anode.value)
        u = findSet(L,s[0])
        v = findSet(L,s[2])
        if u != v:
            deletenode(L,u)
            deletenode(L,v)
            add(L,Union(v.value,u.value))
        Anode = Anode.nextNode
    return length(L)

def extractArist(Grafo):
    listArist=LinkedList()
    for i in range(len(Grafo)):
        currentNode=Grafo[i].head.nextNode
        while currentNode != None:
            if i <= currentNode.value:
                add(listArist, str(i) + "-" + str(currentNode.value))
            currentNode=currentNode.nextNode

    return listArist

#Ejercicio 10
#Before es la posicion del array del elemento en cual se sale
def findPath(Grafo, v1, v2, before, isCycle):
    Black = LinkedList()
    Recorrido = LinkedList()
    anterior = searchInArrayGraph(Grafo,before)
    if findPathWrapped(Grafo,v1,v2,anterior,Black,Recorrido,isCycle,0) == True:
        return Recorrido
    else:
        return None
def findPathWrapped(Grafo,v1,v2,before,black,recorrido,isCycle,n): #La idea del es que busque en camino por donde no salio y para eso se usa el before como verificacion
    pos = searchInArrayGraph(Grafo,v1)

    if pos == None:
        return False
    
    currentNode= Grafo[pos].head.nextNode
    add(black,pos)
    add(recorrido,pos)
    if search(Grafo[pos],searchInArrayGraph(Grafo,v2)) != None:
        if n != 0 and isCycle == True:
            return True
        if isCycle == False:
            return True
    
  
    while currentNode != None:
        if search(black,currentNode.value) != None:
            currentNode=currentNode.nextNode
        else:
            if currentNode.value != before:
                if findPathWrapped(Grafo,Grafo[currentNode.value].head.value,v2,before,black,recorrido,isCycle,n+1) == True:
                    return True
            else:
                currentNode = currentNode.nextNode
    delete(recorrido,pos)
    return False

def bestRoad(G,v1,v2):
    currentNode=G[searchInArrayGraph(G,v1)].head.nextNode
    L = None
    minimum = None
    cont=0
    while currentNode != None:
        if v1 == v2:
            L = findPath(G,G[currentNode.value].head.value,v2, v2,True)
        else:
            L = findPath(G,G[currentNode.value].head.value,v2,v1,False)
        if L != None:
            if cont == 0:
                minimum= L
                cont = cont + 1
            else:
                if length(minimum) > length(L):
                    minimum=L
        currentNode=currentNode.nextNode
    if minimum != None:
        add(minimum,searchInArrayGraph(G,v2))
        currentNode = minimum.head
        L = LinkedList()
        while currentNode != None:
            add(L,G[currentNode.value].head.value)
            currentNode = currentNode.nextNode
        add(L,v1)
        return L
    else:
        return None

def isBipartite(G): 
    countiterations = 0
    countnones = 0
    for i in range(len(G)):
        currentNode=G[i].head.nextNode
        L = None
        while currentNode!=None:
            countiterations = countiterations + 1
            L = findPath(G,G[currentNode.value].head.value,G[i].head.value, G[i].head.value,True)
            if L != None:
                if length(L) % 2 == 0: #Si la longitud de la lista es par
                    #Entonces tiene un ciclo de longitud impar, no es bipartite
                    return False
            else:
                countnones = countnones + 1
            currentNode=currentNode.nextNode
    if countnones == countiterations:
        return False
    else:
        return True

