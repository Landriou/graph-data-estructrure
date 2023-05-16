from linkedlist import *
from algo1 import *
class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False


def trie_insert(T,element):
    stri = String(element)
    if T.root == None:
        node = TrieNode()
        node.children = LinkedList()
        firstnode = TrieNode()
        firstnode.parent = node
        firstnode.key = stri[0]
        add(node.children,firstnode)
        T.root = node
        if len(stri) == 1: 
            firstnode.isEndOfWord = True
            return
        trie_insert_r(T,firstnode,stri,1)
    else:
        trie_insert_r(T,T.root,stri,0)


def trie_insert_r(T,node,stri,i):
    if node.children == None: #Si el nodo que le paso no tiene hijo
        node.children = LinkedList() #Creo la lista de los hijos
        newNode = TrieNode()
        newNode.key = stri[i]
        newNode.parent = node  #Asigno los elementos al nuevo nodo
        add(node.children,newNode)
        if len(stri)-1 == i: #Caso base de la recursividad
            newNode.isEndOfWord = True  #Si llegue al final lo marco como palabra final
            return
        trie_insert_r(T,newNode,stri,i+1)
    else: #Si no es None, significa q ya hay una lista
        wanted = searchNodeInTrie(node.children,stri[i]) #Busco el nodo con la key en la lista
        if wanted != None: #Si lo encuentro
            if len(stri)-1 == i: #Si es la final termino la recursividad y la marco
                wanted.isEndOfWord = True
                return
            trie_insert_r(T,wanted,stri,i+1)
        else: #Si no hay nodo en la lista con la letra debo agregarlo!
            newNode = TrieNode()
            newNode.key = stri[i]
            newNode.parent = node
            add(node.children,newNode) #Preparo nodo y lo agrego
            if len(stri)-1 == i:
                newNode.isEndOfWord = True
                return
            trie_insert_r(T,newNode,stri,i+1)


def searchNodeInTrie(L, key):
    if L == None:
        return None
    currentnode = L.head
    posicion = 0   
    while currentnode != None:
        if currentnode.value.key == key:
            return currentnode.value
        currentnode = currentnode.nextNode
    return None

def trie_search(T,element):
    stri = String(element)
    trienode = T.root
    for i in range(len(stri)):
        wanted = searchNodeInTrie(trienode.children,stri[i])
        if wanted == None:
            return False
        else:
            trienode = wanted
    if wanted.isEndOfWord == True:
        return True
    else:
        return False

def trie_delete(T,element):
    stri = String(element)
    if trie_search(T,element) == True: #Esto se ejecutara si la palabra esta efectivamente contenida
        trienode = T.root
        singlebranch = 0
        for i in range(len(stri)): #Voy buscando los nodos de la palabra
            wanted = searchNodeInTrie(trienode.children,stri[i])
            if wanted.children != None:
                if length(wanted.children) == 1: #Por cada vez q los nodos no tengan otras branchs
                    singlebranch = singlebranch + 1
            if i == len(stri)-1: #Si estoy en la ultima iteracion
                if wanted.children != None and wanted.isEndOfWord == True: #Si el nodo de la ultima letra tiene mas nodos debajo
                    wanted.isEndOfWord = False #Caso 3
                else: #Si la ultima letra esta en el ultimo nodo.
                    if singlebranch == len(stri)-1:
                        deleteInListTrie(T.root.children,stri[0]) #Deleto la branch completa
                    else:
                        for n in range(len(stri)):
                            if length(wanted.parent.children) == 2:
                                deleteInListTrie(wanted.parent.children,stri[len(stri)-n-1])
                                break
                            wanted = wanted.parent
            trienode = wanted
    else:
        return None


def deleteInListTrie(L, element):
    if searchNodePosition(L, element) == None:
        return None
    flag = True
    contador = 0 
    nodoanterior = 0
    nodoposterior = 0
    currentnode = L.head
    if searchNodePosition(L,element) == 0:
        for n in range(length(L)-1):
            currentnode.value = currentnode.nextNode.value
            if n != length(L)-2:
                currentnode = currentnode.nextNode
        currentnode.nextNode = None
        return searchNodePosition(L,element)
    while flag:
        contador = contador + 1
        if contador == searchNodePosition(L, element):
            flag = False
        nodoanterior = currentnode
        nodoposterior = currentnode.nextNode.nextNode
        currentnode = currentnode.nextNode
    nodoanterior.nextNode = nodoposterior
    return searchNodePosition(L,element)

def searchNodePosition(L, element):
    currentnode = L.head
    posicion = 0    
    while currentnode != None:
        if currentnode.value.key == element:
            return posicion
        posicion = posicion + 1
        currentnode = currentnode.nextNode
    return None
#Ejercicio 4
def recopilarPalabras(T,p,n):
    stri = String(p)
    if n < len(stri):
        return None
    trienode = T.root
    for i in range(len(stri)):
        wanted = searchNodeInTrie(trienode.children,stri[i])
        if wanted == None:
            return False
        else:
            trienode = wanted
    L = LinkedList()
    recorridoTrie(wanted,String(""),L)
    sizeL = length(L)
    currentnode = L.head
    for j in range(sizeL):
        currentnode.value = concat(stri,currentnode.value.arr.data)
        if len(currentnode.value) == n:
            print(currentnode.value)
        currentnode = currentnode.nextNode

            
def recorridoTrie(node,stri,L):
    currentnode = None
    if node.children != None:
        currentnode = node.children.head
    while currentnode != None:
        stri = concat(stri,currentnode.value.key) #Agrego la letra
        if currentnode.value.isEndOfWord == True: # Imprimo la palabra si es end of word
            add(L,stri)
        recorridoTrie(currentnode.value,stri,L)
        if currentnode.value.children != None:
            if length(currentnode.value.children) == 1:
                if length(currentnode.value.parent.children) == 2:
                    stri2 = String("")
                    for i in range(len(stri)-1):
                        stri2 = concat(stri2,stri[i])
                    stri = stri2
                else:
                    stri = String("")
        currentnode = currentnode.nextNode
#Ejercicio 5
def CompararTries(A,B):
    LT1 = LinkedList()
    recorridoTrie(A.root,String(""),LT1)
    LT2 = LinkedList()
    recorridoTrie(B.root,String(""),LT2)
    nodeLT1 = LT1.head
    nodeLT2 = LT2.head
    cant = 0
    while nodeLT2 != None:
        if searchStringInList(LT1,nodeLT2.value.arr.data):
            cant = cant + 1
        nodeLT2 = nodeLT2.nextNode
    if length(LT2) == cant:
        return True
    else:
        return False


def searchStringInList(L,element):
    currentnode = L.head
    while currentnode != None:
        if currentnode.value.arr.data == element:
            return True
        currentnode = currentnode.nextNode
    return False

#Ejercicio 6
def tieneInvertida(T):
    L = LinkedList()
    recorridoTrie(T.root,String(""),L)
    currentnode = L.head
    siguientenode = L.head
    while currentnode != None:
        while siguientenode != None:
            if currentnode != siguientenode:
                if strcompare(currentnode.value,Inverter(siguientenode.value)):
                    return True
            siguientenode = siguientenode.nextNode
        siguientenode = L.head
        currentnode = currentnode.nextNode
    return False


def Inverter(s):
    invertido = String("")
    for n in range(len(s)-1,-1,-1):
        invertido = concat(invertido,s[n])
    return invertido

def strcompare(t,p):
    if len(t) != len(p):
        return False
    for i in range(0,len(p)):
         if t[i] != p[i]:
            return False
    return True

#Ejercicio 7
def autoCompletar(Trie, cadena):
    stri = String(cadena)
    trienode = Trie.root
    for i in range(len(stri)):
        wanted = searchNodeInTrie(trienode.children,stri[i])
        if wanted == None:
            return False
        else:
            trienode = wanted
    L = LinkedList()
    recorridoTrie(wanted,String(""),L)
    if length(L) == 1:
        print(L.head.value)
    else:
        print("")