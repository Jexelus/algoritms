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

# Функция для реализации алгоритма Флойда-Уоршелла
def floyd_warshall(graph):
    # Инициализация матрицы расстояний
    nodes = list(graph.keys())
    distance = {i: {j: float('inf') if i != j else 0 for j in nodes} for i in nodes}
    
    # Заполнение матрицы расстояний исходными значениями из графа
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            distance[node][neighbor] = weight
    
    # Алгоритм Флойда-Уоршелла
    for k in nodes:
        for i in nodes:
            for j in nodes:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

# Вычисление кратчайших расстояний
distances = floyd_warshall(graph)

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
for node1 in distances:
    for node2 in distances[node1]:
        if node1 == "A" or node2 == "A":
            print(f"{node1} to {node2}: {distances[node1][node2]}")
            plt.text(pos[node1][0], pos[node1][1], f'{node1} to {node2}: {distances[node1][node2]}', 
                    horizontalalignment='center', verticalalignment='center', fontsize=16, color='red')

# Отображение графика
plt.show()