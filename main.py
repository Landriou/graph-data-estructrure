from linkedlist import *
from graph import *
from BFS import *
from Gponderado import *
V = LinkedList()
add(V,"Corona de hielo")
add(V,"Taanan")
add(V,"Talador")
add(V,"Nagrand")
add(V,"Sombraluna")
add(V,"Arak")
add(V,"Pirofrio")
add(V,"Gorgrond")

A = LinkedList()
add(A,"0,1")
add(A,"0,5")
add(A,"2,5")
add(A,"3,5")
add(A,"4,5")
add(A,"5,6")
add(A,"1,4")
V1 = LinkedList()
add(V1,"1")
add(V1,"0")
A1 = LinkedList()
add(A1,"0,1")
G2 = createGraph(V1,A1)
print(existPath(G2,"0","0"))
G = createGraph(V,A)
print(existPath(G,"Gorgrond","Gorgrond"))
print(existPath(G,"Nagrand","Pirofrio"))

print(existPath(G,"Gorgrond","Talador"))
print(existPath(G,"Nagrand","Sombraluna"))
print(existPath(G,"Taanan","Pirofrio"))
print(existPath(G,"Nagrand","Corona de hielo"))




print("")
print(isTree(G))

V3=LinkedList()
A3=LinkedList()

#add(V,"Mendza")
#add(V,"San Luis")
add(V3,"Cordoba")
add(V3,"BS AS")
add(V3,"Santa Fe")
add(V3,"Rioja")

add(A3,"0,1")
#add(A,"0-2")
#add(A,"0-3")
add(A3,"1,2")
#add(A,"1-3")
add(A3,"2,3")
#add(A,"3-0")


Grafo2=createGraph(V3,A3)



print(existPath(Grafo2,"Santa Fe","Santa Fe"))

#imprimirlista(convertTree(G))

V5 = LinkedList()
add(V5,"a")
add(V5,"b")
add(V5,"c")
add(V5,"d")
add(V5,"e")
add(V5,"f")
add(V5,"g")
add(V5,"h")
add(V5,"i")
add(V5,"j")

A5= LinkedList()

add(A5,"8,6")
add(A5,"5,3")
add(A5,"9,7")
add(A5,"2,1")
add(A5,"9,8")
add(A5,"5,4")
add(A5,"8,7")


G5 = createGraph(V5,A5)
print(countConnections(G5))


V7 = LinkedList()

add(V7,"v")#7#
add(V7,"u")#6#
add(V7,"s")#5#
add(V7,"t")#4#
add(V7,"y")#3#
add(V7,"r")#2#
add(V7,"x")#1#
add(V7,"w")#0#

A7= LinkedList()

add(A7,"5,2")
add(A7,"5,0")
add(A7,"2,7")
add(A7,"0,4")

add(A7,"0,1")
add(A7,"1,4")


add(A7,"4,6")
add(A7,"6,3")

add(A7,"1,6")
add(A7,"1,3")


G7 = createGraph(V7,A7)
bdf = bfsTree(G7,"s")


V8 = LinkedList()

add(V8,"z")
add(V8,"y")
add(V8,"x")
add(V8,"w")
add(V8,"v")
add(V8,"u")

A8= LinkedList()

add(A8,"5,5")
add(A8,"3,0")
add(A8,"0,1")
add(A8,"3,1")
add(A8,"3,4")
add(A8,"1,4")
add(A8,"2,4")
add(A8,"2,5")


G8 = createGraph(V8,A8)


G8 =dsfTree(G8,V8)
print("")

imprimirlista(findPath(G,"Nagrand","Pirofrio","Pirofrio",True))
imprimirlista(findPath(G,"Pirofrio","Sombraluna","Pirofrio",False))
print("")
imprimirlista(bestRoad(G,"Pirofrio","Talador"))
print("")
imprimirlista(bestRoad(G,"Pirofrio","Pirofrio"))
print("")
imprimirlista(bestRoad(G,"Talador","Talador"))
print(bestRoad(G,"Corona de hielo","Corona de hielo"))


V11 = LinkedList()

add(V11,"3")
add(V11,"2")
add(V11,"1")
add(V11,"0")

A11 = LinkedList()
add(A11,"0,1")
add(A11,"1,2")
add(A11,"2,3")

G11 = createGraph(V11,A11)
print(isBipartite(G11))

V12 = LinkedList()
add(V12,"Taanan")
add(V12,"Talador")
add(V12,"Nagrand")
add(V12,"Sombraluna")
add(V12,"Arak")
add(V12,"Pirofrio")
add(V12,"Gorgrond")
A12 = LinkedList()
add(A12, CreateArist(0,1,"3"))
add(A12, CreateArist(0,6,"12"))
add(A12, CreateArist(0,5,"4"))
add(A12, CreateArist(5,6,"6"))
add(A12, CreateArist(5,1,"3"))
add(A12, CreateArist(5,4,"4"))
add(A12, CreateArist(5,2,"2"))
add(A12, CreateArist(5,3,"3"))
add(A12, CreateArist(3,2,"10"))

M = CreateGraphPond(V12,A12)
Imprimirmatriz(M)
print("")
V13=LinkedList()
A13=LinkedList()

add(V13,"6")
add(V13,"5")
add(V13,"4")
add(V13,"3")
add(V13,"2")
add(V13,"1")

add(A13, CreateArist(0,2,"1"))
add(A13, CreateArist(0,1,"6"))
add(A13, CreateArist(0,3,"5"))
add(A13, CreateArist(1,4,"3"))
add(A13, CreateArist(3,5,"2"))
add(A13, CreateArist(2,1,"5"))
add(A13, CreateArist(2,3,"5"))
add(A13, CreateArist(2,4,"6"))
add(A13, CreateArist(2,5,"4"))
add(A13, CreateArist(4,5,"6"))
M2 = CreateGraphPond(V13,A13)
Imprimirmatriz(M2)
M3 = PRIM(M2)
print("")
Imprimirmatriz(M3)

print("")
M2 = CreateGraphPond(V13,A13)
Imprimirmatriz(M2)
M3 = KRUSKAL(M2)
print("")
Imprimirmatriz(M3)

V23 = LinkedList()

add(V23,"z")#4
add(V23,"x")#3
add(V23,"t")#2
add(V23,"y")#1
add(V23,"s")#0

A23 = LinkedList()
add(A23, CreateArist(0,1,"5"))
add(A23, CreateArist(0,2,"10"))
add(A23, CreateArist(1,2,"3"))
add(A23, CreateArist(1,3,"9"))
add(A23, CreateArist(1,4,"2"))
add(A23, CreateArist(2,1,"2"))
add(A23, CreateArist(2,3,"1"))
add(A23, CreateArist(3,4,"4"))
add(A23, CreateArist(4,0,"7"))
add(A23, CreateArist(4,3,"6"))
M23 = CreateGraphPondDir(V23,A23)
imprimirlista(shortestPath(M23,"s","t"))
print("")
imprimirlista(shortestPath(M23,"s","x"))
print("")
imprimirlista(shortestPath(M23,"s","z"))
print("")
imprimirlista(shortestPath(M23,"s","y"))