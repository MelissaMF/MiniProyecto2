import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Importar Datos
data = pd.read_csv("twitter_connections.csv", sep=";")

# Crear Grafo Dirigido
G = nx.DiGraph()
print("Grafo creado")

# Agregar Nodos y Aristas
G.add_nodes_from(data["followee"])
G.add_nodes_from(data["follower"])
print("Nodos agregados")
for _, row in data.iterrows():
    G.add_edge(row["follower"], row["followee"])
print("Aristas agregadas")

# Visualizar Matriz de Adyacencia
adj_list = G.adj
# print(adj_list)

# Grafo Dirigido que sólo considera a quienes siguen alguno de los diarios
# cuentas = ["latercera", "soyvaldiviacl", "elmostrador", "Cooperativa"]

# # Crea un grafo dirigido usando NetworkX
# grafo = nx.DiGraph()

# # Agrega las relaciones de seguimiento al grafo
# for index, row in data.iterrows():
#     cuenta = row["followee"]
#     seguidor = row["follower"]
#     if cuenta in cuentas:
#         grafo.add_edge(cuenta, seguidor)

# # Dibuja el digrafo utilizando Matplotlib y NetworkX
# pos = nx.spring_layout(grafo)  # Posiciones de los nodos para una mejor visualización
# nx.draw(grafo, pos, node_color='skyblue', node_size=6, arrowsize=1)
# plt.title("Digrafo de relaciones de seguimiento")
# plt.show()

# Pregunta 2
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

# Pregunta 1

newsaccount = [node for node, degree in sorted_in_degrees[:4]]
print("Diarios a analizar: " + str(newsaccount))
# Soy Valdivia
soyvaldivia_followers = list(G.predecessors("soyvaldiviacl"))
# print(soyvaldivia_followers)
n_followers_soyvaldivia = G.in_degree("soyvaldiviacl")
print("Soy Valdivia :" + str(n_followers_soyvaldivia))
# La Tercera
latercera_followers = list(G.predecessors("latercera"))
# print(latercera_followers)
n_followers_latercera = G.in_degree("latercera")
print("La Tercera :" + str(n_followers_latercera))
# Cooperativa
cooperativa_followers = list(G.predecessors("Cooperativa"))
# print(cooperativa_followers)
n_followers_cooperativa = G.in_degree("Cooperativa")
print("Cooperativa :" + str(n_followers_cooperativa))
# El Mostrador
elmostrador_followers = list(G.predecessors("elmostrador"))
# print(elmostrador_followers)
n_followers_elmostrador = G.in_degree("elmostrador")
print("El mostrador :" + str(n_followers_elmostrador))

fig, ax = plt.subplots()
ax.bar(["La tercera", "El Mostrador", "Soy Valdivia", "Cooperativa"], [
       n_followers_latercera, n_followers_elmostrador, n_followers_soyvaldivia, n_followers_cooperativa])
ax.set_xlabel("Diarios")
ax.set_ylabel("Seguidores por diario")
ax.set_title("Cantidad de seguidores que tiene cada diario")
plt.show()

# Crear un diccionario para almacenar las cuentas seguidas por cada seguido
followee_accounts = {}
cant_followee_accounts = {}
compass = {}
for nodo in G.nodes:
    cont = 0
    compass_sum = 0
    followee_accounts[nodo] = []  # Inicializar una lista vacía para cada nodo

    if nodo in soyvaldivia_followers:
        followee_accounts[nodo].append("soyvaldiviacl:centro")
        cont += 1
    if nodo in latercera_followers:
        followee_accounts[nodo].append("la tercera:derecha")
        cont += 1
        compass_sum += 75
    if nodo in elmostrador_followers:
        followee_accounts[nodo].append("el mostrador:libertario")
        cont += 1
        compass_sum += 25
    if nodo in cooperativa_followers:
        followee_accounts[nodo].append("cooperativa:izquierda")
        cont += 1
        compass_sum += -75
    if not followee_accounts[nodo]:
        continue
    else:
        followee_accounts[nodo].append("y su tendencia política es")
        followee_accounts[nodo].append(f"{compass_sum/cont}")

    cant_followee_accounts[nodo] = cont
filter_accounts = {}
for follower, followee in followee_accounts.items():
    if not followee:
        pass
    else:
        print(f"{follower} sigue a {followee}")
        filter_accounts[follower] = followee[-1]

values_compass = Counter(filter_accounts.values())
# Obtener las claves (valores numéricos) y los valores (number de seguidores) del conteo
numeric_values = sorted(list(values_compass.keys()), key=float)
number_followers = [values_compass[number] for number in numeric_values]
# Graficar el gráfico de barras
plt.bar(numeric_values, number_followers)
# Graficar el gráfico de barras agrupado por valores
plt.bar(numeric_values, number_followers)

# Etiqueta del eje x
plt.xlabel('Tendencia Política')

# Etiqueta del eje y
plt.ylabel('Cantidad de Seguidores')

# Título del gráfico
plt.title('Political Compass Adaptado')

# Muestra el gráfico
plt.show()
# # Estadísticas de cuantos diarios sigue cada perosna que sigue al menos un diario.
usuarios_1_diario = 0
usuarios_2_diarios = 0
usuarios_3_diarios = 0
usuarios_4_diarios = 0

# # Contamos el número de usuarios en cada grupo
for number in cant_followee_accounts.values():
    if number == 1:
        usuarios_1_diario += 1
    elif number == 2:
        usuarios_2_diarios += 1
    elif number == 3:
        usuarios_3_diarios += 1
    elif number == 4:
        usuarios_4_diarios += 1

# # Imprimimos los resultados
print(f"Usuarios que siguen 1 diario: {usuarios_1_diario}")
print(f"Usuarios que siguen 2 diarios: {usuarios_2_diarios}")
print(f"Usuarios que siguen 3 diarios: {usuarios_3_diarios}")
print(f"Usuarios que siguen 4 diarios: {usuarios_4_diarios}")

fig, ax = plt.subplots()
ax.bar(["1 diario", "2 Diarios", "3 Diarios", "4 Diarios"], [
       usuarios_1_diario, usuarios_2_diarios, usuarios_3_diarios, usuarios_4_diarios])
ax.set_xlabel("Cantidad de diarios seguidos")
ax.set_ylabel("Número de usuarios")
ax.set_title("Cantidad de usuarios que siguen cierta number de diarios")
plt.show()
