from linkedlist import *
from queue import *
class BinaryTree:
	Root=None

class BinaryTreeNode:
    Key=None
    Value=None
    Leftnode=None
    Rightnode=None
    Parent=None



#Funcion wrapper para la recursividad
def insertR(NewNode,currentnode):
    NewNode.Parent = currentnode
    
    if NewNode.Key > currentnode.Key: #Si es mayor
        if currentnode.Rightnode == None:
            currentnode.Rightnode = NewNode
            return NewNode.Key #Si esta vacio lo inserto en esa posicion y retorno la key 
        else:
            return insertR(NewNode,currentnode.Rightnode)
            #Si no, llamo a la recursividad
    else:
        if NewNode.Key == currentnode.Key:
            return None
        if currentnode.Leftnode == None:
            currentnode.Leftnode = NewNode
            return NewNode.Key #lo mismo pero del lado izquierdo
        else:
            return insertR(NewNode,currentnode.Leftnode)
            #Si no, llamo a la recursividad

#Funcion que inserta un nodo
def bt_insert(B,e,k):
    NewNode = BinaryTreeNode()
    NewNode.Key = k
    NewNode.Value = e #Creo el nodo y le asigno los valores
    if B.Root == None:
        B.Root = NewNode
        return k
    else:
        return insertR(NewNode,B.Root)

#Funcion wrapper para la recursividad del search
def searchL(currentnode,element):
    k = None    
    if currentnode.Value == element:
        k = currentnode.Key # Si lo encuentro lo guardo en k
    if currentnode.Leftnode != None and k == None: 
        #Si no lo encuentro y k no ha sido asignada
        #Y reviso los hijos
        if currentnode.Leftnode.Value != element:
            k = searchL(currentnode.Leftnode,element)
            #Si no esta en el hijo llamo a la recursividad
        else:
            k = currentnode.Leftnode.Key #Si esta en el hijo lo asigno a k
        #Lo mismo pero del lado derecho
    if currentnode.Rightnode != None and k == None:
        if currentnode.Rightnode.Value != element:
            k = searchL(currentnode.Rightnode,element)
        else:
            k = currentnode.Rightnode.Key
    if k != None:   #Si ya encontro k en las recurisivades
        return k
#Le paso un arbol y devuelve el la key del elemento
def bt_search(B, element):
    if B.Root == None: #Si esta vacio
        return None
    if B.Root.Value == element: #Si lo encuentro en la raiz
        return B.Root.Key
    return searchL(B.Root, element)
        
def bt_access(B,key):
    return accessR(B.Root,key)
#Busco en el arbol la key
def accessR(currentnode,key):
    if currentnode.Key == key: #Si encuentro la key dejo de buscar y retorno el value
            return currentnode.Value
    if currentnode.Key < key: #Recorro el arbol
        return accessR(currentnode.Rightnode,key)
    else:
        return accessR(currentnode.Leftnode,key)
#Funcion que en ves del value me devuelve el nodo
def B_accessnode(B,key):
    return accessnodeR(B.Root, key)
def accessnodeR(currentnode,key):
    if currentnode != None:
        if currentnode.Key == key:
                return currentnode
        if currentnode.Key < key:
            return accessnodeR(currentnode.Rightnode,key)
        else:
            return accessnodeR(currentnode.Leftnode,key)
    else:
        return None
def bt_update(B,element, key):
    nodo = B_accessnode(B,key) #Acceso al nodo
    if nodo == None:
        return None
    nodo.Value = element
    return key
    
def bt_deleteKey(B,key):
    if B.Root == None:
        return None
    nodo = B_accessnode(B,key) #Tomo el puntero del nodo
    if nodo == None:
        return None
    return deleteKeyR(nodo,key, B)

def deleteKeyR(currentnode, key, B):
    if currentnode.Leftnode == None and currentnode.Rightnode == None: #Si el nodo no tiene hijos
        currentnode.Leftnode = None
        currentnode.Rightnode = None
        if currentnode.Key > currentnode.Parent.Key:
            currentnode.Parent.Rightnode = None
        else:
            currentnode.Parent.Leftnode = None
        return key
    if currentnode.Leftnode != None and currentnode.Rightnode != None: #Si el nodo tiene ambos hijos
        menor = menordelosmayores(currentnode.Rightnode)
        if currentnode.Leftnode != menor:
            menor.Leftnode = currentnode.Leftnode
            menor.Leftnode.Parent = menor
        if currentnode.Rightnode != menor:
            menor.Rightnode = currentnode.Rightnode
            menor.Rightnode.Parent = menor
        menor.Parent = currentnode.Parent
        currentnode.Leftnode = None
        currentnode.Rightnode = None
        if currentnode.Parent != None:
            if currentnode.Parent.Key > currentnode.Key:
                currentnode.Parent.Leftnode = menor
            else:
                currentnode.Parent.Rightnode = menor
        else:
            B.Root = menor
        return key
    if currentnode.Leftnode != None or currentnode.Rightnode != None: #Si el nodo tiene un solo hijo
        if currentnode.Leftnode == None:
            currentnode.Rightnode.Parent = currentnode.Parent
            currentnode.Parent.Rightnode = currentnode.Rightnode
            return key
        if currentnode.Rightnode == None:
            currentnode.Leftnode.Parent = currentnode.Parent
            currentnode.Parent.Leftnode = currentnode.Leftnode
            return key
    

#Tengo que pasarle como parametro el nodo de la derecha
def menordelosmayores(currentnode):
    if currentnode.Leftnode == None:
        menor = currentnode
        currentnode.Parent.Leftnode = None
        if currentnode.Rightnode != None:
            currentnode.Rightnode.Parent = currentnode.Parent
            currentnode.Parent.Rightnode = currentnode.Rightnode
        return menor
    else:
        return menordelosmayores(currentnode.Leftnode)

def bt_delete(B,element):
    key = bt_search(B,element)
    if key == None:
        return None
    else:
        return bt_deleteKey(B,key)


def traverseInOrder(B):
    if B.Root == None:
        return None
    Listinorder = LinkedList()
    traverseR(B.Root,Listinorder)
    return inverse(Listinorder)
def traverseR(currentnode,L):
    if currentnode.Leftnode != None:
        traverseR(currentnode.Leftnode,L)
    add(L,currentnode.Value)
    if currentnode.Rightnode != None:
        traverseR(currentnode.Rightnode,L)

def traverseInPostOrder(B):
    if B.Root == None:
        return None
    ListPostorder = LinkedList()
    traversePostR(B.Root,ListPostorder)
    return inverse(ListPostorder)
def traversePostR(currentnode,L):
    if currentnode.Leftnode != None:
        traversePostR(currentnode.Leftnode,L)
    if currentnode.Rightnode != None:
        traversePostR(currentnode.Rightnode,L)
    add(L,currentnode.Value)

def traverseInPreOrder(B):
    if B.Root == None:
        return None
    ListPreorder = LinkedList()
    traversePreR(B.Root,ListPreorder)
    return inverse(ListPreorder)
def traversePreR(currentnode,L):
    add(L,currentnode.Value)
    if currentnode.Leftnode != None:
        traversePreR(currentnode.Leftnode,L)
    if currentnode.Rightnode != None:
        traversePreR(currentnode.Rightnode,L)

def traverseBreadFirst(B):
    if B.Root == None:
        return None
    QueueAux = LinkedList()
    Queue1 = LinkedList()
    enqueue(QueueAux,B.Root) #Meto la raiz en una cola aux

    while(length(QueueAux) != 0):#Voy sacando uno por uno de la cola auxiliar mientras meto en otra cola los hijos de cada uno y asi sucesivamente
        aux = dequeue(QueueAux)
        enqueue(Queue1,aux)
        if aux.Leftnode != None:
            enqueue(QueueAux,aux.Leftnode)
        if aux.Rightnode != None:
            enqueue(QueueAux,aux.Rightnode)
    L = LinkedList()
    currentnode = Queue1.head
    #Como lo de antes me da los punteros, saco los values o lo meto en una lista
    while currentnode != None:
        add(L,currentnode.value.Value)
        currentnode = currentnode.nextNode
    return L  