import networkx as nx
import matplotlib.pyplot as plt

# Функция для реализации алгоритма Дейкстры
def dijkstra(graph, start):
    # Инициализация расстояний до всех вершин как бесконечность
    distances = {node: float('infinity') for node in graph}
    # Расстояние до начальной вершины равно 0
    distances[start] = 0
    # Множество вершин, для которых расстояние уже вычислено
    visited = set()

    while len(visited) < len(graph):
        # Выбор вершины с наименьшим расстоянием
        current_node = min((set(distances.keys()) - visited), key=distances.get)
        # Помещаем вершину в множество посещенных
        visited.add(current_node)

        for neighbor, distance in graph[current_node].items():
            # Обновление расстояний через текущую вершину
            old_distance = distances[neighbor]
            new_distance = distances[current_node] + distance
            if new_distance < old_distance:
                distances[neighbor] = new_distance

    return distances

# Пример графа в виде словаря
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Вызов алгоритма Дейкстры
start_node = 'A'
distances = dijkstra(graph, start_node)

G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Визуализация графа
pos = nx.spring_layout(G)  # Выбор стиля расположения вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Вывод результатов
for node, distance in distances.items():
    print(f"Кратчайшее расстояние от вершины {start_node} до вершины {node} равно {distance}")
    plt.text(pos[node][0], pos[node][1], f'{distance}', horizontalalignment='center', verticalalignment='center', fontsize=26, color='red')

plt.show()