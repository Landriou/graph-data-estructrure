from algo1 import *
from linkedlist import *
from sort import *
from Set import *
from graph import *
class Arista:
    v1 = None
    v2 = None
    weight = None

def CreateGraphPond(V,A):
    size = length(V)
    Graph = Array(size+1,Array(size+1,""))
    currentnode = V.head
    for i in range(1,size+1):
        Graph[0][i] = currentnode.value
        currentnode = currentnode.nextNode
    currentnode = V.head
    for j in range(1,size+1):
        Graph[j][0] = currentnode.value
        currentnode = currentnode.nextNode
    Anode = A.head
    while Anode != None:
        Graph[Anode.value.v1+1][Anode.value.v2+1] = Anode.value.weight
        Graph[Anode.value.v2+1][Anode.value.v1+1] = Anode.value.weight
        Anode = Anode.nextNode
    return Graph

def Imprimirmatriz(A):
    sizerows = len(A)
    sizecolumns = len(A[0])
    for i in range(sizerows):
        for j in range(sizecolumns):
            print(A[i][j],end=" ")
        print("")
    print("\n\n\n")

def CreateArist(v1,v2,weight):
    Arist = Arista()
    Arist.v1 = v1
    Arist.v2 = v2
    Arist.weight = weight
    return Arist

def PRIM(G):
    T = LinkedList()
    U = LinkedList()

    add(U,1)
    for j in range(len(G)-2):
        A = searchPRIM(G,U)
        add(T,A)
        add(U,A.v2)
    size = length(U)
    L = LinkedList()
    for n in range(size,0,-1):
        add(L,G[0][n])
    currentnode = T.head
    while currentnode != None:
        currentnode.value.v1 = currentnode.value.v1 -1
        currentnode.value.v2 = currentnode.value.v2 -1
        currentnode = currentnode.nextNode
    return CreateGraphPond(L,T)



def searchPRIM(G,U):
    currentnode = U.head
    Aristo = Arista()
    while currentnode != None:
        for i in range(1,len(G)):
            if G[currentnode.value][i] != None:
                if search(U,i) == None and Aristo.weight == None:
                    Aristo.v1 = currentnode.value
                    Aristo.v2 = i
                    Aristo.weight = G[currentnode.value][i]
                else:
                    if search(U,i) == None and int(Aristo.weight) > int(G[currentnode.value][i]):
                        Aristo.v1 = currentnode.value
                        Aristo.v2 = i
                        Aristo.weight = G[currentnode.value][i]
        currentnode = currentnode.nextNode
    return Aristo


def KRUSKAL(G):
    V=LinkedList()

    for i in range(1,len(G)):
        add(V,G[i][0])
    V=inverse(V)

    A = LinkedList()
    #Extraigo las aristas del grafo
    for i in range(1,len(G)):
        for j in range(1,i+1):
            if G[i][j] != None:
                Aristo = Arista()
                Aristo.v1 = i - 1
                Aristo.v2 = j - 1
                Aristo.weight = G[i][j]
                add(A,Aristo)
    A = MergeSort(A) #Las ordenos por peso con un Mergesort morificado

    L = LinkedList()
    #Hago un set con cada nodo
    Anode = A.head
    for n in range(len(G)-1):
        A = Array(1,0)
        A[0] = n
        add(L,A)
    Afinal = LinkedList()
    while Anode != None: #Recorro la lista de aristas y voy uniendo set por set.
        u = findSet(L,Anode.value.v1)
        v = findSet(L,Anode.value.v2)
        if u != v:
            deletenode(L,u)
            deletenode(L,v)
            add(L,Union(v.value,u.value))
            add(Afinal, Anode.value)
        Anode = Anode.nextNode
    return CreateGraphPond(V,Afinal)





def imprimirlistaWeight(A):
    currentnode = A.head
    while currentnode != None:
        print(currentnode.value.weight, end="  ")
        currentnode = currentnode.nextNode    
    print("")

class DijkstraNode():
    value = None
    d = None
    pi = None
    color = None

def CreateGraphPondDir(V,A):
    size = length(V)
    Graph = Array(size+1,Array(size+1,""))
    currentnode = V.head
    for i in range(1,size+1):
        Graph[0][i] = currentnode.value
        currentnode = currentnode.nextNode
    currentnode = V.head
    for j in range(1,size+1):
        Graph[j][0] = currentnode.value
        currentnode = currentnode.nextNode
    Anode = A.head
    while Anode != None:
        Graph[Anode.value.v1+1][Anode.value.v2+1] = Anode.value.weight
        Anode = Anode.nextNode
    return Graph





def AdyacenciaMtoList(M):
    G = Array(len(M)-1,LinkedList())
    
    for i in range(1,len(M)):
        node = DijkstraNode()
        node.value = M[i][0]
        G[i-1] = LinkedList()

        for j in range(1,len(M)):
            if M[i][j] != None:
                aristo = Arista()
                aristo.v1 = i-1
                aristo.v2 = j-1
                aristo.weight = M[i][j]
                add(G[i-1],aristo)
        add(G[i-1],node)

    return G    

def searchInArrayGraphInsideNode(A,v): #Busco en el array el string correspondiente
    pos = 0
    for n in range(len(A)):
        if A[n].head.value.value == v:
            return pos
        pos = pos + 1
    return None

def initRelax(G, s):
    for i in range(len(G)):
        G[i].head.value.d = 2147483648
        G[i].head.value.pi = None
        pos = searchInArrayGraphInsideNode(G,s)
        G[pos].head.value.d = 0
def relax(G,Arista):
    u = G[Arista.v1].head.value
    v = G[Arista.v2].head.value
    if v.d > (u.d + int(Arista.weight)):
        v.d = u.d + int(Arista.weight)
        v.pi = u
def shortestPath(M, s, v):
    G = AdyacenciaMtoList(M)
    initRelax(G, s)
    GV = LinkedList()
    for i in range(len(G)):
        add(GV,G[i].head.value)
    while length(GV) > 0:
        u = minQueue(GV)
        u.color = "black"
        
        pos = searchInArrayGraphInsideNode(G,u.value.value)
        currentnode = G[pos].head.nextNode
        while currentnode != None:
            if G[currentnode.value.v2].head.value.color != "black":
                relax(G,currentnode.value) 
            currentnode = currentnode.nextNode
    posV = searchInArrayGraphInsideNode(G,v)
    posS = searchInArrayGraphInsideNode(G,s)
    currentnode = G[posV].head
    L = LinkedList()
    add(L,currentnode.value.value)
    currentnode = currentnode.value.pi
    while currentnode != None:
        add(L,currentnode.value)
        currentnode = currentnode.pi
    if L.head.value == G[posS].head.value.value:
        return L
    else:
        return None
def minQueue(GV):
    currentnode = GV.head
    minimum = currentnode
    currentnode = currentnode.nextNode
    while currentnode != None:
        if currentnode.value.d < minimum.value.d:
            minimum = currentnode
        currentnode = currentnode.nextNode
    deletenode(GV,minimum)
    return minimum