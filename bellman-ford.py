import networkx as nx
import matplotlib.pyplot as plt

# Граф в виде словаря
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}


# Функция для реализации алгоритма Беллмана-Форда
def bellman_ford(graph, start):
    # Инициализация расстояний до всех вершин как бесконечность
    distances = {node: float('infinity') for node in graph}
    # Расстояние до начальной вершины равно 0
    distances[start] = 0

    # Обновление расстояний для всех ребер графа V-1 раз
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Проверка на наличие отрицательных циклов
    for node in graph:
        for neighbor, weight in graph[node].items():
            assert distances[node] + weight >= distances[neighbor], "Граф содержит отрицательный цикл"

    return distances


# Вычисление кратчайших расстояний
start_node = 'A'
distances = bellman_ford(graph, start_node)

# Создание графа
G = nx.Graph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Визуализация графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Добавление информации о кратчайших расстояниях
for node, distance in distances.items():
    plt.text(pos[node][0], pos[node][1], f'{distance}', horizontalalignment='center', verticalalignment='center',
             fontsize=20, color='red')

# Отображение графика
plt.show()
