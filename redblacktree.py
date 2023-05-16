class RedBlackTree:
	root = None

class RedBlackNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    color = None


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
def r_insert(rbtree,e,k):
    NewNode = RedBlackNode()
    NewNode.key = k
    NewNode.value = e 
    NewNode.color = "red"           #Creo el nodo y le asigno los valores
    if rbtree.root == None:
        rbtree.root = NewNode
        NewNode.color = "black"
        return k
    else:
        keyinserted = insertR(NewNode,rbtree.root)
        painttree(rbtree,NewNode)
        return keyinserted
def painttree(rbtree,rbnode):
    tionone = False
    tio = gettio(rbnode)
    if rbnode.parent.color == "black": #Caso base
            return
    if tio == None:
      tionone = True
    else:
      if tio.color == "black":
        tionone = True
    if tionone: #Si el tio es none o black
            if tio == rbnode.parent.parent.leftnode or rbnode.parent.parent.leftnode == None : #LADO DERECHO
                if rbnode.parent.leftnode == rbnode: #TRIANGULO CASO 2:
                    rotateRight(rbtree,rbnode.parent)
                else: #CASO 3 LINEA
                    recolor(rbnode.parent)
                    recolor(rbnode.parent.parent)
                    rotateLeft(rbtree,rbnode.parent.parent)
            else:  #LADO IZQUIERDO
                if rbnode.parent.rightnode == rbnode: #TRIANGULO CASO 2:
                    rotateLeft(rbtree,rbnode.parent)
                else: #CASO 3 LINEA
                    recolor(rbnode.parent)
                    recolor(rbnode.parent.parent)
                    rotateRight(rbtree,rbnode.parent.parent) 
    if tio != None:
        if tio.color == "red": #CASO 1
            recolor(rbnode.parent)
            recolor(rbnode.parent.parent)
            recolor(tio)
            if rbnode.parent.parent != None:
                if rbnode.parent.parent.parent != None:
                    painttree(rbtree, rbnode.parent.parent)
            
    if rbtree.root.color == "red": #Caso 0
            rbtree.root.color = "black"
    if rbnode.color == "red" and rbnode.leftnode != None:
        if rbnode.leftnode.color == "red":
            painttree(rbtree,rbnode.leftnode)
        else:
            painttree(rbtree,rbnode)
    if rbnode.color == "red" and rbnode.rightnode != None:
        if rbnode.rightnode.color == "red":
            painttree(rbtree,rbnode.rightnode)
        else:
            painttree(rbtree,rbnode)
    else:
        painttree(rbtree,rbnode)

def recolor(node):
    if node.color == "red":
        node.color = "black"
    else:
        node.color = "red"



def gettio(node):
    if node.parent.parent != None:
        if node.parent == node.parent.parent.rightnode:
            return node.parent.parent.leftnode
        elif node.parent == node.parent.parent.leftnode:
            return node.parent.parent.rightnode
        else:
            return None


def imprimirsubnodes(B,node):
  if node.leftnode!=None:
    print("/ node de la izquierda de key {",node.leftnode.key,"} de element",node.leftnode.value)
  else:
    print("/ no hay node de la izquierda")
  if node.rightnode!=None:
    print("\ node de la derecha key {",node.rightnode.key,"} de element",node.rightnode.value)
  else:
    print("\ no hay node de la derecha")\
    
  print("==Color== ",node.color)


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
