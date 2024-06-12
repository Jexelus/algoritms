import networkx as nx
import matplotlib.pyplot as plt

def viterbi(graph, start, end):
    # Инициализация таблицы вероятностей и предков
    probabilities = {node: 0.0 for node in graph}
    predecessors = {node: None for node in graph}
    probabilities[start] = 1.0

    # Вычисление наиболее вероятных путей
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, transition_prob in graph[node].items():
                if probabilities[node] * transition_prob > probabilities[neighbor]:
                    probabilities[neighbor] = probabilities[node] * transition_prob
                    predecessors[neighbor] = node

    # Восстановление пути
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.reverse()

    return path, probabilities[end]

# Пример использования
graph = {
    'A': {'B': 0.9, 'C': 0.1},
    'B': {'D': 0.7, 'E': 0.3},
    'C': {'D': 0.5, 'E': 0.5},
    'D': {'F': 0.4, 'G': 0.6},
    'E': {'F': 0.6, 'G': 0.4},
    'F': {},
    'G': {}
}

start_node = 'A'
end_node = 'F'
path, probability = viterbi(graph, start_node, end_node)

# Создание графа
G = nx.DiGraph()
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Визуализация графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Выделение наиболее вероятного пути
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

# Отображение графика
plt.show()

print("Путь:", path)
print("Вероятность:", probability)