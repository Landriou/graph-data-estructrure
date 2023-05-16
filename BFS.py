from linkedlist import *

class bfsNode:
    value = None
    color = None
    child = None
    dist = None
    parent = None

def bfsTree(Grafo,V):
    for i in range(len(Grafo)):
        node=bfsNode()
        node.value=Grafo[i].head.value
        node.color="WHITE"

        currentNode=Grafo[i].head
        Grafo[i].head=currentNode.nextNode
        currentNode=None
        add(Grafo[i],node)

    queue= LinkedList()
    vert= None
    contador = 0

    while vert == None:
        if Grafo[contador].head.value.value == V:
            vert = Grafo[contador].head
        contador=contador + 1

    vert.value.color="GRAY"
    vert.value.dist = 0
    enqueue(queue,vert) ## Nodo dentro de nodo
    dist=0

    while length(queue) != 0 : 

        value = dequeue(queue)
        currentNode = value.nextNode

        while currentNode != None:
            if Grafo[currentNode.value].head.value.color == "WHITE":
                Grafo[currentNode.value].head.value.color = "GRAY"
                Grafo[currentNode.value].head.value.parent = queue.head 
                Grafo[currentNode.value].head.value.dist = value.value.dist +1
        
                enqueue(queue,Grafo[currentNode.value].head)
            currentNode=currentNode.nextNode

        
        value.value.color = "BLACK"
    return Grafo


class dsfNode:
    value = None
    color = None
    child = None
    temp = None
    parent = None
    finaliza = None

def dsfTree(Grafo,V):
    for i in range(len(Grafo)):
        node=dsfNode()
        node.value=Grafo[i].head.value
        node.color="WHITE"

        currentNode=Grafo[i].head
        Grafo[i].head=currentNode.nextNode
        currentNode=None
        add(Grafo[i],node)
    time = 0
    for i in range(len(Grafo)):
        if Grafo[i].head.value.color == "WHITE":
            DFSVisit(Grafo,Grafo[i].head,time)
    return Grafo

def DFSVisit(Grafo,v,time):
    currentnode = v.nextNode
    time = time + 1
    v.value.temp = time
    v.value.color = "GRAY"
    while currentnode != None:
        if Grafo[currentnode.value].head.value.color == "WHITE":
            Grafo[currentnode.value].head.value.parent = v.value
            time = DFSVisit(Grafo,Grafo[currentnode.value].head,time)
        currentnode = currentnode.nextNode
    v.value.color = "BLACK"
    time = time + 1
    v.value.finaliza = time
    return time