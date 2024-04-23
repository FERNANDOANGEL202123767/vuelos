import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous_nodes = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                previous_nodes[neighbor] = current_node

    return previous_nodes

def shortest_path(graph, start, end):
    previous_nodes = dijkstra(graph, start)
    path = []
    current_node = end

    while current_node != start:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    path.insert(0, start)
    return path

graph = {
    1: {2: 4},
    2: {3: 2},
    3: {5: 4},
    5: {7: 20},
    7: {}
}

start_node = 1
end_node = 7
shortest_path_nodes = shortest_path(graph, start_node, end_node)

print("Camino más corto:", shortest_path_nodes)