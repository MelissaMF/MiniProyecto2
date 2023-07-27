import networkx as nx
import pandas as pd

#Importar Datos
data = pd.read_csv("twitter_connections.csv", sep=";")

#Crear Grafo Dirigido
G = nx.DiGraph()
print("Grafo creado")

#Agregar Nodos y Aristas
G.add_nodes_from(data["followee"])
G.add_nodes_from(data["follower"])
print("Nodos agragados")
for _, row in data.iterrows():
    G.add_edge(row["follower"], row["followee"])
print("Aristas agregadas")

# Visualizar Matriz de Adyacencia
adj_list = G.adj
#print(adj_list)

#Pregunta 2

# Calcula el grado de entrada y salida de cada nodo
in_degrees = G.in_degree()
out_degrees = G.out_degree()

# Ordena los nodos por su grado de entrada en orden descendente
sorted_in_degrees = sorted(in_degrees, key=lambda x: x[1], reverse=True)

# Ordena los nodos por su grado de salida en orden descendente
sorted_out_degrees = sorted(out_degrees, reverse=True)

# Selecciona los primeros 10 nodos con el mayor grado de entrada
top_10_most_influential = [node for node, degree in sorted_in_degrees[:10]]

# Selecciona los primeros 10 nodos con el mayor grado de salida
top_10_most_influenced = [node for node, degree in sorted_out_degrees[:10]]

print("Top 10 usuarios más influyentes:", top_10_most_influential)
print("Top 10 usuarios más influenciados:", top_10_most_influenced)

#Pregunta 1

newsaccount = [node for node, degree in sorted_in_degrees[:4]]
print("Diarios a analizar: " + str(newsaccount))
#Soy Valdivia
soyvaldivia_followers = list(G.predecessors("soyvaldiviacl"))
#print(soyvaldivia_followers)
n_followers_soyvaldivia = G.in_degree("soyvaldiviacl")
print("Soy Valdivia :" + str(n_followers_soyvaldivia))
#La Tercera
latercera_followers = list(G.predecessors("latercera"))
#print(latercera_followers)
n_followers_latercera = G.in_degree("latercera")
print("La Tercera :" + str(n_followers_latercera))
#Cooperativa
cooperativa_followers = list(G.predecessors("Cooperativa"))
#print(cooperativa_followers)
n_followers_cooperativa = G.in_degree("Cooperativa")
print("Cooperativa :" + str(n_followers_cooperativa))
#El Mostrador
elmostrador_followers = list(G.predecessors("elmostrador"))
#print(elmostrador_followers)
n_followers_elmostrador = G.in_degree("elmostrador")
print("El mostrador :" + str(n_followers_elmostrador))

# Crear un diccionario para almacenar las cuentas seguidas por cada seguido
cuentas_seguidas = {}

for nodo in G.nodes:
    if nodo in soyvaldivia_followers:
        cuentas_seguidas[nodo] = cuentas_seguidas.get(nodo, "") + "soyvaldiviacl 17%' centro "

    if nodo in latercera_followers:
        cuentas_seguidas[nodo] = cuentas_seguidas.get(nodo, "") + ", la tercera 33%' derecha "

    if nodo in elmostrador_followers:
        cuentas_seguidas[nodo] = cuentas_seguidas.get(nodo, "") + ", el mostrador 17%' libertario "

    if nodo in cooperativa_followers:
        cuentas_seguidas[nodo] = cuentas_seguidas.get(nodo, "") + ", cooperativa 33%' izquierda "

print(cuentas_seguidas)
