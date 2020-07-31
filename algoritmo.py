import pandas as pd
import numpy as np
import copy
import os
import matplotlib.pyplot as plt
import networkx as nx



os.system('cls' if os.name == 'nt' else 'clear')

Weights = {('A', 'B'):5 , ('A', 'C'): 5, ('B', 'D'): 5, ('B', 'L'): 5, ('C', 'A'): 5, ('C', 'E'): 5, ('D', 'B'): 5, ('D', 'G'): 5, ('E', 'C'): 5, ('E', 'F'): 5,('E', 'G'): 5, ('F', 'G'): 5, ('F', 'E'): 5, ('F', 'H'): 5, ('F', 'I'): 5, ('F', 'J'): 5, ('G', 'D'): 5, ('G', 'E'): 5, ('G', 'F'): 5, ('H', 'F'): 5,('H', 'I'): 5, ('H', 'J'): 5, ('I', 'F'): 5, ('I', 'H'): 5, ('I', 'J'): 5, ('J', 'F'): 5, ('J', 'H'): 5, ('J', 'I'): 5, ('J', 'Q'): 5, ('K', 'I'): 5,('K', 'M'): 5, ('K', 'N'): 5, ('L', 'B'): 5, ('L', 'K'): 5, ('M', 'K'): 5, ('M', 'N'): 5, ('M', 'R'): 5, ('M', 'S'): 5, ('M', 'BB'): 5, ('N', 'K'): 5,('N', 'M'): 5, ('N', 'O'): 5, ('O', 'I'): 5, ('O', 'N'): 5, ('O', 'P'): 5, ('P', 'I'): 5, ('P', 'O'): 5, ('P', 'R'): 5, ('P', 'S'): 5, ('P', 'T'): 5,('Q', 'J'): 5, ('Q', 'T'): 5, ('Q', 'U'): 5, ('Q', 'DD'): 5, ('R', 'M'): 5, ('R', 'S'): 5, ('R', 'P'): 5, ('R', 'BB'): 5, ('S', 'M'): 5, ('S', 'R'): 5,('S', 'P'): 5, ('S', 'T'): 5, ('T', 'P'): 5, ('T', 'Q'): 5, ('T', 'S'): 5, ('T', 'U'): 5, ('U', 'Q'): 5, ('U', 'V'): 5, ('U', 'T'): 5, ('U', 'DD'): 5,('V', 'U'): 5, ('V', 'W'): 5, ('V', 'DD'): 5, ('W', 'V'): 5, ('W', 'X'): 5, ('X', 'W'): 5, ('X', 'Y'): 5, ('Y', 'X'): 5, ('Y', 'Z'): 5, ('Z', 'Y'): 5,('Z', 'AA'): 5, ('AA', 'Z'): 5, ('AA', 'BB'): 5, ('AA', 'CC'): 5, ('BB', 'M'): 5, ('BB', 'R'): 5, ('BB', 'AA'): 5, ('CC','AA'): 5,  ('DD', 'Q'): 5, ('DD', 'U'): 5, ('DD','V'): 5 }

G = nx.Graph()
# each edge is a tuple of the form (node1, node2, {'weight': weight})
edges = [(k[0], k[1], {'weight': v}) for k, v in Weights.items()]
G.add_edges_from(edges)

pos = nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=100)

# labels
nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

# edges
nx.draw_networkx_edges(G,pos,edgelist=edges, width=2)

# weights
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels = labels)


plt.title(' KINSI ')

plt.suptitle( 'Ordorica', multialignment='center')
plt.show()
plt.savefig('redunam.png')



print( " Bienvenido a PumaOptimo ")
print(" Andres Ordorica Fernandez")
print(" PumaOptimo te de la mejor combinacion de caminar y puma bus para llegar a tu destino")
print(" A continuacion se le preguntara la hora a la que desea viajar ( ejemplo 7 para 7 am o 15 para 3 pm) y despues se le preguntara si desea viajar 30 minutos despues ( ejemplo si es 7:30 , primero selecciona 7 y despues 1) ")

tiempodeseado = int(input("Porfavor escriba la hora a la que deseara viajar, hora sin minutos (0-23)  y presione enter: "))
exacto = str(input("Tiene flojera de caminar o esta lloviendo ? (si/no) : "))


if exacto == 'si':
    f=5
else :
    if exacto == 'no':
        f = 0


if tiempodeseado >= 23 :
    print (" Programa tu viaje bien, ya no hay servicio ")

else :
    if tiempodeseado == 6:
        i = 3
    else:
        if tiempodeseado == 7:
            i = 1
        else:
            if tiempodeseado == 14:
                i = 3
            else :
                if tiempodeseado == 15:
                    i = 3
                else:
                    if tiempodeseado == 19:
                        i = 2
                    else: 
                        if tiempodeseado == 20:
                            i = 1
                        else:
                            i = 1



os.system('cls' if os.name == 'nt' else 'clear')

print(" porfavor presta atencion a la letra  que corresponde tu sitio actual y tu destino, a continuacion se presentara la lista")

destinos = [ 'A-MUAC','B-MB zona cultural','C-UNIVERSUM','D-Espacio Escultorico','E-TV UNAM','F-Tienda UNAM','G-FCPyS','H-Metro UNAM','I-FC','J-Anexo Quimica','K-MB CU','L-I Biomedica','M-Estadio Practicas','N-Trabajo Social','O-FCyA','P-Anexo Ingenieria','Q-FVyZ','R-FI','S-ENALT','T-FQ','U-FM','V-FO','W-FE','X-FD','Y-FFyL','Z-FP','AA-Rectoria','BB-FA','CC-Estadio Olimpico','DD-Metro Copilco']
print(destinos)

inicio = str(input("Porfavor escriba la letro ( en mayusculas)  de su punto de inicio y presione enter: "))

fin = str(input("Porfavor escriba la letra (en mayusculas ) de su destino y presione enter: "))

'''create a graph with the nodes and their weights'''
distances= {
           'A':{'B': 4+f, 'C': 10+f},
           'B':{'D': 9+f, 'L': 36+f,'c2':i},
           'c2':{'D':6,'L':9},
           'C':{'A': 10+f, 'E': 10+f,'c3':i},
           'c3':{'A':6,'E':21},
           'D':{'B': 9+f, 'G': 8+f,'c4':i},
           'c4':{'B':3 , 'G':3},
           'E':{'C': 10+f, 'F': 7+f, 'G':8+f, 'c5':i} ,
           'c5':{'C':18, 'F':6},
           'F':{'E': 7+f, 'G': 16+f,'H': 3+f, 'I': 9+f,'J': 4+f, 'c6':i},
           'c6':{'E':6, 'G':6},
           'G':{'D': 9+f, 'E': 8+f, 'F': 15+f, 'c7':i},
           'c7':{'F':9},
           'H':{'F': 3+f, 'I': 6+f, 'J': 5+f, 'c8':i},
           'c8':{'I':3, 'J':3},
           'I':{'F': 7+f, 'H': 6+f, 'J': 6+f, 'O': 5+f, 'P': 10+f, 'c9':i},
           'c9':{'F':3, 'H':6 , 'O':3 , 'P':3},
           'J':{'F': 4+f, 'H': 5+f, 'I': 6+f, 'Q': 13+f, 'c10':i},
           'c10':{'H':3, 'Q':6},
           'K':{'I': 20+f, 'M': 6+f, 'N': 3+f, 'c11':i},
           'c11':{'L':3, 'M':12, 'N':6},
           'L':{'B': 36+f, 'K': 20+f, 'c12':i},
           'c12':{'B':27, 'K':6},
           'M':{'K': 6+f, 'N': 7+f, 'R': 11+f, 'S': 12+f, 'BB': 9+f, 'c13':i},
           'c13':{'K':3, 'N':6, 'R':27 , 'S':24},
           'N':{'K': 3+f, 'M': 6+f, 'O': 4+f, 'c14':i},
           'c14':{'M':12, 'O':3},
           'O':{'I': 5+f, 'N': 4+f, 'P': 13+f, 'c15':i},
           'c15':{'I':3, 'P':6},
           'P':{'I': 12+f, 'O': 14+f, 'R': 6+f, 'S': 6+f, 'T': 2+f, 'c16':i},
           'c16':{'I':12, 'O':15 , 'R':12 , 'S':9 , 'T':6},
           'Q':{'J': 14+f, 'T': 18+f, 'U': 17+f, 'DD': 19+f, 'c17':i} ,
           'c17':{'J':3, 'T':3 , 'U':3 , 'DD':3},
           'R':{'M': 11+f, 'P': 5+f, 'S': 1+f, 'BB': 10+f, 'c18':i},
           'c18':{'M':3, 'S':3},
           'S':{'M': 13+f, 'P': 5+f, 'R': 1+f, 'T': 3+f, 'c19':i},
           'c19':{'M':30},
           'T':{'P': 13+f, 'Q': 5+f, 'S': 1+f, 'U': 3+f, 'c20':i},
           'c20':{'U':3},
           'U':{'Q': 2+f, 'T': 3+f, 'V': 4+f, 'DD': 1+f, 'c21':i},
           'c21':{'Q':3, 'V':3},
           'V':{'U': 6+f, 'W': 6+f, 'DD': 10+f , 'c22':i},
           'c22':{'W':3},
           'W':{'V': 6+f, 'X': 6+f},
           'X':{'W': 6+f, 'Y': 6+f, 'c24':i},
           'c24':{'Y':3},
           'Y':{'X': 6+f, 'Z': 6+f, 'c25':i},
           'c25':{'Z':3},
           'Z':{'Y': 6+f, 'AA': 6+f, 'c26':i},
           'c26':{'AA':6},
           'AA':{'Z': 6+f, 'BB': 4+f, 'CC': 7+f, 'c27':i},
           'c27':{'CC':9},
           'BB':{'M': 9+f, 'R': 10+f, 'AA': 4+f, 'c28':i},
           'c28':{'M':3},
           'CC':{'AA': 7+f, 'c29':i},
           'c29':{'AA':3},
           'DD':{'Q': 18+f, 'U': 14+f, 'V': 13+f, 'c30':i},
           'c30':{'R':12}
           }

'''next create two dictionaries, one to store the predecessor nodes and the other to 
store and update the weights of the nodes as the algorithm progresses'''
city_records= {}
dist_records= {}

'''duplicate the graph and populate it with infinity values'''
for k in distances.keys():
    dist_records[k]= float('Inf')
    city_records[k]= None
        
'''create a list to store all visited nodes'''        
visited= []

'''assign the start and end nodes to two variables'''
start= inicio
end= fin

'''function that selected the unvisited node with the least total distance from the start node'''
def pick_node(dist_records):
    
    dist_records2= copy.deepcopy(dist_records)
    for node in visited:
        del dist_records2[node]
        
    return min(dist_records2, key= dist_records2.get)
def shortest_path(start_node, end_node, records):
    
    shortest_path= [end_node]
    while True:
        shortest_path.append(records.get(end_node))
        end_node= records.get(end_node)

        if end_node == start_node:
            break

    '''reverse the list to get the nodes from start to end'''        
    return shortest_path[::-1]
def djikstras_algo(start, end, dist_records, city_records, visited):
    '''update the two dictionaries to make sure that the weight of the start node is 0 and 
    it's predecessor node is itself'''
    
    dist_records[start]= 0
    city_records[start]= start

    if start == end:
        print('shortest path is {}'.format(0))

    while True:    
        node= pick_node(dist_records)
        for k in distances[node].keys():
            if k in visited:
                continue

            if dist_records[node] + distances[node].get(k) < dist_records[k]:
                dist_records[k]= dist_records[node] + distances[node].get(k)
                city_records[k]= node

        visited.append(node)

        if end in visited:
            break
    os.system('cls' if os.name == 'nt' else 'clear')


    print('La ruta mas corta es: ', shortest_path(start_node= start, end_node= end, records= city_records))
    
    ruta = []
    ruta = (shortest_path(start_node= start, end_node= end, records= city_records))
    
    print( 'Tu camino empieza en :')
    for elemento in ruta:
        if elemento == 'A':
            print ( ' MUAC ')
            print ( ' y te diriges a : ')
        else:
            if elemento == 'B':
                print ( ' MB zona cultural ')
                print ( ' y te diriges a : ')
            else:
                if elemento == 'C':
                    print ( ' UNIVERSUM ')
                    print ( ' y te diriges a : ')
                else:
                    if elemento == 'D':
                        print ( ' Espacio Escultorico ')
                        print ( ' y te diriges a : ')
                    else:
                        if elemento == 'E':
                            print ( ' TV UNAM ')
                            print ( ' y te diriges a : ')
                        else:
                            if elemento == 'F':
                                print ( ' Tienda UNAM')
                                print ( ' y te diriges a : ')
                            else:
                                if elemento == 'G':
                                    print ( ' Facultad CP y S ')
                                    print ( ' y te diriges a : ')
                                else :
                                    if elemento == 'H':
                                        print ( ' Metro CU ')
                                        print ( ' y te diriges a : ')
                                    else :
                                        if elemento == 'I':
                                            print ( ' Facultad de Ciencias ')
                                            print ( ' y te diriges a : ')
                                        else :
                                            if elemento == 'J':
                                                print ( ' Anexo Quimica ')
                                                print ( ' y te diriges a : ')
                                            else :
                                                if elemento == 'K':
                                                    print ( ' MB CU ')
                                                    print ( ' y te diriges a : ')
                                                else :
                                                    if elemento == 'L':
                                                        print ( ' Instituto Biomedicas ')
                                                        print ( ' y te diriges a : ')
                                                    else:
                                                        if elemento == 'M':
                                                            print ( ' Estadio de Practicas ')
                                                            print ( ' y te diriges a : ')
                                                        else:
                                                            if elemento == 'N':
                                                                print ( ' Trabajo Social ')
                                                                print ( ' y te diriges a : ')
                                                            else:
                                                                if elemento == 'O':
                                                                    print ( ' Facultad C y A ')
                                                                    print ( ' y te diriges a : ')
                                                                else:
                                                                    if elemento == 'P':
                                                                        print ( ' Anexo de Ingenieria')
                                                                        print ( ' y te diriges a : ')
                                                                    else:
                                                                        if elemento == 'Q':
                                                                            print ( ' Facutlad V y Z')
                                                                            print ( ' y te diriges a : ')
                                                                        else:
                                                                            if elemento == 'R':
                                                                                print ( ' Facultad de Ingenieria ')
                                                                                print ( ' y te diriges a : ')
                                                                            else :
                                                                                if elemento == 'S':
                                                                                    print ( ' ENALT ')
                                                                                    print ( ' y te diriges a : ')
                                                                                else :
                                                                                    if elemento == 'T':
                                                                                        print ( ' Facultad de Quimica ')
                                                                                        print ( ' y te diriges a : ')
                                                                                    else :
                                                                                        if elemento == 'U':
                                                                                            print ( ' Facultad de Medicina ')
                                                                                            print ( ' y te diriges a : ')
                                                                                        else:
                                                                                            if elemento == 'V':
                                                                                                print ( ' Facultad de Odontologia ')
                                                                                                print ( ' y te diriges a : ')
                                                                                            else :
                                                                                                if elemento == 'W':
                                                                                                    print ( ' Facultad de Economia ')
                                                                                                    print ( ' y te diriges a : ')
                                                                                                else:
                                                                                                    if elemento == 'X':
                                                                                                        print ( ' Facultad de Derecho ')
                                                                                                        print ( ' y te diriges a : ')
                                                                                                    else:
                                                                                                        if elemento == 'Y':
                                                                                                            print ( ' Facultad de Filosofia ')
                                                                                                            print ( ' y te diriges a : ')
                                                                                                        else:
                                                                                                            if elemento == 'Z':
                                                                                                                print ( ' Facultad de Psicologia ')
                                                                                                                print ( ' y te diriges a : ')
                                                                                                            else:
                                                                                                                if elemento == 'AA':
                                                                                                                    print ( ' Torre de Rectoria ')
                                                                                                                    print ( ' y te diriges a : ')
                                                                                                                else:
                                                                                                                    if elemento == 'BB':
                                                                                                                        print('Facultad de Arquitectura')
                                                                                                                        print(' y te diriges a : ')
                                                                                                                    else:
                                                                                                                        if elemento == 'CC':
                                                                                                                            print('Estadio Olimpico')
                                                                                                                            print('y te diriges a :')
                                                                                                                        else:
                                                                                                                            if elemento == 'DD':
                                                                                                                                print('Metro Copilco')
                                                                                                                                print('y te diriges a :')
                                                                                                                            else:
                                                                                                                                print(' Dirigete a la estacion mas cercana de Puma Bus y toma el camion ')
                                                                                                                                print('Con direccion a : ')

                                                                                                            


               
    print(' Has llegado a tu destino ')
    if dist_records.get(end) > 45 and exacto == 'yes' : 
        print( ' El tiempo de traslado optimo caminando y con la red UNAM de transporte es : {} minutos '.format(dist_records.get(end)))
        print( ' Mejor toma un uber o un taxi ')
    else:
        if dist_records.get(end) > 45 and exacto == 'no' and tiempodeseado < 16 and tiempodeseado > 6:
            print( ' El tiempo de traslado optimo caminando y con la red UNAM de transporte es : {} minutos '.format(dist_records.get(end)))
            print( ' Es demasiado tiempo ! Toma una bici Puma mejor ')

        else:
            if dist_records.get(end) > 40 and exacto == 'no'  and tiempodeseado > 18:
                print( ' El tiempo de traslado optimo caminando y con la red UNAM de transporte es : {} minutos '.format(dist_records.get(end)))
                print( ' Es la ruta mas corta, pero ya esta obscuro ten cuidado ')
            else:
                print('El tiempo del traslado es el optimo  : {} minutos '.format(dist_records.get(end)))

    for elemento in ruta :
        if elemento == 'DD':
            print ("Por favor toma tus precacuines en Copilco y Cerro del Agua, ha habido muchos reportes de robos ")
        else :
            if elemento == 'H' :
                print (" Por favor toma tus precauciones en la salida a Metro UNAM, ha habido reportes de robo e intentos de secuestro ")

djikstras_algo(start, end, dist_records, city_records, visited)




print( " Gracias por utilizar KINSI ")
