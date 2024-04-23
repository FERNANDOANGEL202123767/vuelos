from flask import Flask, render_template
from Vuelo_3601 import Nodo

# Define nodo_inicial aquí
estado_inicial = 'EDO.MEX'
nodo_inicial = Nodo(estado_inicial)

conexiones = {
    'EDO.MEX': {'QRO', 'SLP', 'SONORA'},
    'PUEBLA': {'HIDALGO', 'SLP'},
    'CDMX': {'MICHOACAN'},
    'MICHOACAN': {'SONORA'},
    'SLP': {'QRO', 'PUEBLA', 'EDO.MEX', 'SONORA'},
    'QRO': {'EDO.MEX', 'SLP'},
    'HIDALGO': {'PUEBLA', 'SONORA'},
    'MONTERREY': {'HIDALGO', 'SLP'},
    'SONORA': {'MONTERREY', 'HIDALGO', 'SLP', 'EDO.MEX', 'MICHOACAN'},

}

def DFS_prof_iter(nodo, solucion, visitados=None):
    if visitados is None:
        visitados = []
    sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados)
    return sol

def buscar_solucion_DFS_Rec(nodo, solucion, visitados):
    if nodo.get_datos() == solucion:
        return nodo
    
    if nodo.get_datos() not in visitados:
        visitados.append(nodo.get_datos())
        print("Nodo actual:", nodo.get_datos())  # Imprimir el nodo actual
        print("Nodos visitados:", visitados)  # Imprimir nodos visitados
        for un_hijo in conexiones[nodo.get_datos()]:
            hijo = Nodo(un_hijo)
            print("Explorando hijo:", hijo.get_datos())  # Imprimir el nodo hijo actual
            sol = buscar_solucion_DFS_Rec(hijo, solucion, visitados)
            if sol is not None:
                return sol
    
    return None

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    solucion = 'HIDALGO'
    visitados = []
    nodo = DFS_prof_iter(nodo_inicial, solucion, visitados)
    if nodo is not None:
        resultado = []
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        return render_template('resultado.html', resultado_vuelos=resultado)
    else:
        return "Solución no encontrada"

if __name__ == "__main__":
    app.run(debug=True)
