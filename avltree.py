from linkedlist import *

class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    balanceFactor = None


def rotateLeft(Tree,avlnode):
    parentnodeX = avlnode.parent
    y = avlnode.rightnode
    if y != None:
        leftnodeY = y.leftnode
        #Conectamos el parent del nodo a rotar
        if parentnodeX != None:
            if parentnodeX.rightnode == avlnode:
                parentnodeX.rightnode = y
                y.parent = parentnodeX
            if parentnodeX.leftnode == avlnode:
                parentnodeX.leftnode = y
                y.parent = parentnodeX

        avlnode.parent = y
        if avlnode == Tree.root: #Si es la raiz debemos actualizarla
            Tree.root = y
            y.parent = None
        y.leftnode = avlnode
        avlnode.rightnode = leftnodeY
        if leftnodeY != None:
            leftnodeY.parent = avlnode
    return y

def rotateRight(Tree,avlnode):
    parentnodeY = avlnode.parent
    x = avlnode.leftnode
    if x != None:
        rightnodeX = x.rightnode
        #Conectamos el parent del nodo a rotar
        if parentnodeY != None:
            if parentnodeY.rightnode == avlnode:
                parentnodeY.rightnode = x
                x.parent = parentnodeY
            if parentnodeY.leftnode == avlnode:
                parentnodeY.leftnode = x
                x.parent = parentnodeY
        avlnode.parent = x
        if avlnode == Tree.root: #Si es la raiz debemos actualizarla
            Tree.root = x
            x.parent = None
        x.rightnode = avlnode
        avlnode.leftnode = rightnodeX
        if rightnodeX != None:
            rightnodeX.parent = avlnode
    return x

def calculateBalance(AVLTree):
  currentNode=AVLTree.root
  if currentNode.leftnode==None and currentNode.rightnode==None:
    currentNode.balanceFactor=0
    return 0
  else:  
    calculateBalanceR2(AVLTree,currentNode)

def calculateBalanceR2(AVLTree,currentNode):
  left=None
  right=None
  if currentNode.leftnode==None: #Si no tengo nodo vale 0
    left=0
  else:
    left=calculateBalanceR2(AVLTree,currentNode.leftnode)+1 #Voy llamando a la recursividad mas 1 si tengo nodo
  if currentNode.rightnode==None:
    right=0
  else:
    right=calculateBalanceR2(AVLTree,currentNode.rightnode)+1
  currentNode.balanceFactor= left - right 
  if left > right: #Me quedo con el valor del la rama mas alta
    return left
  else:
    return right


def reBalance(AVLTree):
    L = traverseBreadFirstInverse(AVLTree)
    node = L.head
    if length(L) > 2: 
        while node != None:
            calculateBalance(AVLTree)
            AVLNode = node.value
            if AVLNode.balanceFactor < -1:
                if AVLNode.rightnode.balanceFactor > 0:
                    rotateRight(AVLTree,AVLNode.rightnode)
                    rotateLeft(AVLTree,AVLNode)
                else:  #CASO A y B
                    rotateLeft(AVLTree,AVLNode)
            elif AVLNode.balanceFactor > 1:
                if AVLNode.leftnode.balanceFactor < 0:
                    rotateLeft(AVLTree,AVLNode.leftnode)
                    rotateRight(AVLTree,AVLNode)
                else: #CASO D y E
                    rotateRight(AVLTree,AVLNode)
            node = node.nextNode


#Funcion wrapper para la recursividad
def insertR(NewNode,currentnode):
    NewNode.parent = currentnode
    
    if NewNode.key > currentnode.key: #Si es mayor
        if currentnode.rightnode == None:
            currentnode.rightnode = NewNode
            return NewNode.key #Si esta vacio lo inserto en esa posicion y retorno la key 
        else:
            return insertR(NewNode,currentnode.rightnode)
            #Si no, llamo a la recursividad
    else:
        if NewNode.key == currentnode.key:
            return None
        if currentnode.leftnode == None:
            currentnode.leftnode = NewNode
            return NewNode.key #lo mismo pero del lado izquierdo
        else:
            return insertR(NewNode,currentnode.leftnode)
            #Si no, llamo a la recursividad

#Funcion que inserta un nodo
def avl_insert(AVLtree,e,k):
    NewNode = AVLNode()
    NewNode.key = k
    NewNode.value = e #Creo el nodo y le asigno los valores
    if AVLtree.root == None:
        AVLtree.root = NewNode
        return k
    else:
        keyinserted = insertR(NewNode,AVLtree.root)
        reBalance(AVLtree) #Aplico el rebalance
        return keyinserted

def avl_accessnode(B,key):
    return accessnodeR(B.root, key)
def accessnodeR(currentnode,key):
    if currentnode != None:
        if currentnode.key == key:
                return currentnode
        if currentnode.key < key:
            return accessnodeR(currentnode.rightnode,key)
        else:
            return accessnodeR(currentnode.leftnode,key)
    else:
        return None
   
def avl_deletekey(B,key):
    if B.root == None:
        return None
    nodo = avl_accessnode(B,key) #Tomo el puntero del nodo
    if nodo == None:
        return None
    reBalance(B) #Rebalanceo el arbol resultante
    return deletekeyR(nodo,key, B)

def deletekeyR(currentnode, key, B):
    if currentnode.leftnode == None and currentnode.rightnode == None: #Si el nodo no tiene hijos
        currentnode.leftnode = None
        currentnode.rightnode = None
        if currentnode.key > currentnode.parent.key:
            currentnode.parent.rightnode = None
        else:
            currentnode.parent.leftnode = None
        return key
    if currentnode.leftnode != None and currentnode.rightnode != None: #Si el nodo tiene ambos hijos
        menor = menordelosmayores(currentnode.rightnode)
        if currentnode.leftnode != menor:
            menor.leftnode = currentnode.leftnode
            menor.leftnode.parent = menor
        if currentnode.rightnode != menor:
            menor.rightnode = currentnode.rightnode
            menor.rightnode.parent = menor
        menor.parent = currentnode.parent
        currentnode.leftnode = None
        currentnode.rightnode = None
        if currentnode.parent != None:
            if currentnode.parent.key > currentnode.key:
                currentnode.parent.leftnode = menor
            else:
                currentnode.parent.rightnode = menor
        else:
            B.root = menor
        return key
    if currentnode.leftnode != None or currentnode.rightnode != None: #Si el nodo tiene un solo hijo
        if currentnode.leftnode == None:
            currentnode.rightnode.parent = currentnode.parent
            currentnode.parent.rightnode = currentnode.rightnode
            return key
        if currentnode.rightnode == None:
            currentnode.leftnode.parent = currentnode.parent
            currentnode.parent.leftnode = currentnode.leftnode
            return key
    

#Tengo que pasarle como parametro el nodo de la derecha
def menordelosmayores(currentnode):
    if currentnode.leftnode == None:
        menor = currentnode
        #currentnode.parent.leftnode = None
        #if currentnode.rightnode != None:
            #currentnode.rightnode.parent = currentnode.parent
            #currentnode.parent.rightnode = currentnode.rightnode
        return menor
    else:
        return menordelosmayores(currentnode.leftnode)

def avl_delete(AVLtree,element):
    key = avl_search(AVLtree,element)
    if key == None:
        return None
    else:
        keydeleted = avl_deletekey(AVLtree,key)
        reBalance(AVLtree) 
        return keydeleted 

        
def searchL(currentnode,element):
    k = None    
    if currentnode.value == element:
        k = currentnode.key # Si lo encuentro lo guardo en k
    if currentnode.leftnode != None and k == None: 
        #Si no lo encuentro y k no ha sido asignada
        #Y reviso los hijos
        if currentnode.leftnode.value != element:
            k = searchL(currentnode.leftnode,element)
            #Si no esta en el hijo llamo a la recursividad
        else:
            k = currentnode.leftnode.key #Si esta en el hijo lo asigno a k
        #Lo mismo pero del lado derecho
    if currentnode.rightnode != None and k == None:
        if currentnode.rightnode.value != element:
            k = searchL(currentnode.rightnode,element)
        else:
            k = currentnode.rightnode.key
    if k != None:   #Si ya encontro k en las recurisivades
        return k
#Le paso un arbol y devuelve el la key del elemento
def avl_search(B, element):
    if B.root == None: #Si esta vacio
        return None
    if B.root.value == element: #Si lo encuentro en la raiz
        return B.root.key
    return searchL(B.root, element) 

def imprimirsubnodes(B,node):
  if node.leftnode!=None:
    print("/ node de la izquierda de key {",node.leftnode.key,"} de element",node.leftnode.value)
  else:
    print("/ no hay node de la izquierda")
  if node.rightnode!=None:
    print("\ node de la derecha key {",node.rightnode.key,"} de element",node.rightnode.value)
  else:
    print("\ no hay node de la derecha")\
    
  print("==Valor de balanceo== ",node.balanceFactor)


def imprimirarbol__P(B,node):
  print("____________________________________________________________")
  if node==B.root:
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("()La raiz con key {",node.key,"} con element[",node.value,"]")
  else:
    print("ººdesde key {",node.key,"} con element [",node.value," ]con parent=",node.parent.key)
  imprimirsubnodes(B,node)
  if node.leftnode!=None:
    imprimirarbol__P(B,node.leftnode)
  if node.rightnode!=None:
    imprimirarbol__P (B,node.rightnode)


        
def traverseBreadFirstInverse(B):
    if B.root == None:
        return None
    QueueAux = LinkedList()
    Queue1 = LinkedList()
    enqueue(QueueAux,B.root) #Meto la raiz en una cola aux

    while(length(QueueAux) != 0):#Voy sacando uno por uno de la cola auxiliar mientras meto en otra cola los hijos de cada uno y asi sucesivamente
        aux = dequeue(QueueAux)
        enqueue(Queue1,aux)
        if aux.leftnode != None:
            enqueue(QueueAux,aux.leftnode)
        if aux.rightnode != None:
            enqueue(QueueAux,aux.rightnode)
    L = LinkedList()
    currentnode = Queue1.head
    #Como lo de antes me da los punteros, saco los values o lo meto en una lista
    while currentnode != None:
        add(L,currentnode.value)
        currentnode = currentnode.nextNode
    return inverse(L)  
