# Vuelos: Dashboard de Algoritmos de Búsqueda

## 📋 Descripción

**Vuelos** es un proyecto educativo que implementa y visualiza algoritmos de búsqueda y optimización a través de un dashboard interactivo. El sistema demuestra el funcionamiento de diferentes algoritmos aplicados a problemas prácticos como la resolución de puzzles y búsqueda de rutas.

### Algoritmos Implementados:
- **DFS (Búsqueda en Profundidad)**: Resolución de puzzle lineal [4, 2, 3, 1] → [1, 2, 3, 4]
- **BFS (Búsqueda en Anchura)**: Resolución del mismo puzzle con enfoque por niveles
- **Búsqueda de Vuelos**: Exploración de rutas entre ciudades usando DFS/BFS
- **Algoritmo de Dijkstra**: Cálculo del camino más corto en grafos ponderados

## 🚀 Características

- **Dashboard Visual**: Interfaz moderna con tarjetas animadas y diseño responsivo
- **Visualización de Pasos**: Muestra la secuencia completa de cada algoritmo
- **Análisis de Rendimiento**: Estadísticas de nodos visitados y complejidad
- **Múltiples Implementaciones**: DFS recursivo e iterativo
- **Código Modular**: Estructura organizada por algoritmos

## 📁 Estructura del Proyecto

```
vuelos/
├── app/
│   ├── templates/
│   │   └── resultado.html     # Plantilla del dashboard
│   ├── app.py                 # Aplicación Flask principal
│   ├── BFS.py                 # Implementación de BFS y clase Nodo
│   ├── DFS.py                 # Implementación de DFS iterativo
│   ├── funcionDFS.py          # Implementación de DFS recursivo
│   ├── dijkstra.py            # Algoritmo de Dijkstra
│   ├── Puzzle_Lineal.py       # Lógica del puzzle lineal con BFS
│   ├── Vuelo_3601.py          # Búsqueda de vuelos con BFS
│   └── vuelos_Busqueda.py     # Búsqueda de vuelos con DFS
├── README.md
└── requirements.txt
```

## 🔧 Requisitos

- Python 3.8 o superior
- Flask 2.0+

## 🛠️ Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/FERNANDOANGEL202123767/vuelos.git
   cd vuelos/app
   ```

2. **Crear entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   
   # En Windows:
   venv\Scripts\activate
   
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install flask
   ```

4. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

5. **Abrir en navegador**: http://127.0.0.1:5000/

## 🎯 Uso

### Dashboard Interactivo

El dashboard presenta cuatro secciones principales:

#### 1. **DFS (Búsqueda en Profundidad)**
- Visualiza la resolución paso a paso del puzzle lineal
- Muestra la secuencia de estados visitados
- Incluye tanto implementación recursiva como iterativa

#### 2. **BFS (Búsqueda en Anchura)**
- Demuestra la búsqueda por niveles
- Compara eficiencia con DFS
- Visualiza el árbol de búsqueda

#### 3. **Búsqueda de Vuelos**
- Simula búsqueda de rutas entre ciudades
- Ejemplo: Estado de México → Hidalgo
- Muestra nodos visitados y camino encontrado

#### 4. **Algoritmo de Dijkstra**
- Calcula el camino más corto en grafo ponderado
- Visualiza el proceso de relajación de aristas
- Muestra distancias mínimas y camino óptimo

### Personalización

Para experimentar con diferentes problemas:

1. **Modificar estado inicial del puzzle**:
   ```python
   # En app.py
   estado_inicial_dfs = [3, 1, 4, 2]  # Nuevo puzzle
   ```

2. **Cambiar grafo de Dijkstra**:
   ```python
   # En dijkstra.py
   grafo = {
       'A': {'B': 4, 'C': 2},
       'B': {'C': 1, 'D': 5},
       # ... más nodos
   }
   ```

3. **Agregar nuevas ciudades**:
   ```python
   # En vuelos_Busqueda.py
   vuelos = {
       'NUEVA_CIUDAD': ['DESTINO1', 'DESTINO2']
   }
   ```

## 📊 Ejemplos de Resultados

### DFS - Puzzle Lineal
```
Estado inicial: [4, 2, 3, 1]
Paso 1: [2, 4, 3, 1]
Paso 2: [2, 3, 4, 1]
...
Estado final: [1, 2, 3, 4]
```

### Dijkstra - Camino Más Corto
```
Distancias mínimas desde nodo 1:
1 → 2: 4
1 → 3: 2
1 → 4: 7
Camino óptimo: 1 → 3 → 4
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz fork del repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Realiza cambios y commit: `git commit -m "Añade nueva funcionalidad"`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Crea un Pull Request

### Ideas para Contribuir
- Implementar A* (A-estrella)
- Añadir visualización con gráficos
- Optimizar algoritmos existentes
- Mejorar interfaz de usuario
- Añadir más casos de prueba

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 👨‍💻 Autor

**Fernando Angel**
- GitHub: [@FERNANDOANGEL202123767](https://github.com/FERNANDOANGEL202123767)
- Proyecto: [Vuelos - Dashboard de Algoritmos](https://github.com/FERNANDOANGEL202123767/vuelos)

## 🏷️ Tags

`algoritmos` `python` `flask` `dfs` `bfs` `dijkstra` `búsqueda` `grafos` `dashboard` `visualización`

---

⭐ **¡Si te gusta este proyecto, dale una estrella!**
