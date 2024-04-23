def dijkstra(nodos, conexiones, inicio, fin):
    # Inicializar los costos mínimos y los padres de los nodos
    costos = {nodo: float('inf') for nodo in nodos}
    padres = {nodo: None for nodo in nodos}
    costos[inicio] = 0
    
    # Algoritmo de Dijkstra
    nodos_visitados = []
    while nodos_visitados != nodos:
        nodo_actual = min((nodo for nodo in nodos if nodo not in nodos_visitados), key=lambda x: costos[x])
        nodos_visitados.append(nodo_actual)
        for vecino, peso in conexiones[nodo_actual].items():
            nuevo_costo = costos[nodo_actual] + peso
            if nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                padres[vecino] = nodo_actual
    
    # Construir el camino mínimo
    camino = [fin]
    while camino[-1] != inicio:
        camino.append(padres[camino[-1]])
    camino.reverse()
    return camino

# Definir nodos y conexiones
nodos = ['1', '2', '3', '4', '5', '6', '7']
conexiones = {
    '1': {'2': 125, '3': 513},
    '2': {'1': 125, '3': 616},
    '3': {'1': 513, '2': 616, '4': 962, '5': 716, '6': 925},
    '4': {'3': 962},
    '5': {'3': 716, '6': 826},
    '6': {'3': 925, '5': 826, '7': 950},
    '7': {'6': 950}
}

# Calcular el camino mínimo del nodo 1 al nodo 7
inicio = '1'
fin = '7'
camino_minimo = dijkstra(nodos, conexiones, inicio, fin)
print("Camino mínimo del nodo 1 al nodo 7:", camino_minimo)
