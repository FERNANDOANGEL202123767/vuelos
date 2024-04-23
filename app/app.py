from flask import Flask, render_template
from DFS import buscar_solucion_DFS, obtener_resultado_DFS
from Puzzle_Lineal import buscar_solucion_BFS, obtener_resultado_Puzzle
from Vuelos_Busqueda import DFS_prof_iter, nodo_inicial

# Especifica la ubicación de la carpeta de plantillas
app = Flask(__name__)

@app.route('/')
def index():
    # Problema DFS
    estado_inicial_dfs = [4, 2, 3, 1]
    solucion_dfs = [1, 2, 3, 4]
    nodo_solucion_dfs = buscar_solucion_DFS(estado_inicial_dfs, solucion_dfs)
    resultado_dfs = obtener_resultado_DFS(nodo_solucion_dfs)
    
    # Problema Puzzle Lineal
    estado_inicial_puzzle = [4, 2, 3, 1]
    solucion_puzzle = [1, 2, 3, 4]
    nodo_solucion_puzzle = buscar_solucion_BFS(estado_inicial_puzzle, solucion_puzzle)
    resultado_puzzle = obtener_resultado_Puzzle(nodo_solucion_puzzle)
    
    # Problema Vuelos
    estado_inicial_vuelos = 'EDO.MEX'
    solucion_vuelos = 'HIDALGO'
    visitados = []  # Lista para almacenar los nodos visitados en la búsqueda de vuelos
    resultado_vuelos = DFS_prof_iter(nodo_inicial, solucion_vuelos, visitados)
    
    return render_template('resultado.html', resultado_dfs=resultado_dfs, resultado_puzzle=resultado_puzzle, resultado_vuelos=resultado_vuelos, nodos_visitados=visitados)

if __name__ == '__main__':
    app.run(debug=True)


