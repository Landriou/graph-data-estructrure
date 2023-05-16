from algo1 import *
#Ejercicio 11

class DiccionaryDA:
    nextNode = None
    flag = None
    value = None
    temp = None
    previousNode = None

def DAsetup(D,L):
    for n in range(len(D)):
        D[n] = DiccionaryDA()

    for i in range(len(D)):
        if i != len(D)-1:
            D[i].nextNode = D[i+1]
        if i != 0:
            D[i].previousNode = D[i-1]
    L.head = D[0]
    
def insertDA(D,L,value,hashresult):
    if D[hashresult].value == None or D[hashresult].flag == True:
        D[hashresult].value = value
        D[hashresult].temp = D[hashresult].nextNode
        if D[hashresult] != L.head:
            anterior = D[hashresult].previousNode
            posterior = D[hashresult].nextNode
            anterior.nextNode = posterior
        else:
            L.head = D[hashresult].nextNode
            D[hashresult].nextNode = None
         #Deleteo el nodo de la misma posicion de la lista
    else:
        if D[hashresult].temp != None:
            node = D[hashresult].temp
            node.temp = node.nextNode
            node.previousNode.temp = node.temp
            D[hashresult].temp = node.temp
            node.value = value
            
            rebalance(D,node.temp,node)
            if node != L.head:
                anterior = node.previousNode
                posterior = node.nextNode
                anterior.nextNode = posterior
            else:
                L.head = node.nextNode
                node.nextNode = None
def rebalance(D,temp,previousnode):
    if previousnode != None:
        if None == previousnode.value:
            return
        else:
            if temp == previousnode.temp:
                rebalance(D,temp,previousnode.previousNode)
            else:
                previousnode.temp = temp
                rebalance(D,temp,previousnode.previousNode)
    
def deleteDA(D,hashresult):
    D[hashresult].flag == True
    D[hashresult].value == None
    rebalance(D,D[hashresult],D[hashresult].previousnode)