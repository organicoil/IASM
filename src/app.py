import networkx as networkx
import matplotlib.pyplot as pyplot
import random as random

m_param = 6
k_param = 2
node_count = 8192
graph = networkx.MultiDiGraph()


def get_priority_node():
    weights = []

    total_degree = graph.number_of_edges() * 2
    for i in range(graph.number_of_nodes()):
        weights.append(graph.degree[i] / total_degree)
    priority_node = random.choices(list(graph.nodes()), k=1, weights=weights)[0]
    return priority_node


def get_random_node():
    return random.choice(list(graph.nodes()))


def generate_initial_graph():
    for i in range(m_param):
        graph.add_node(i)

    for i in range(int((m_param * k_param) / 2)):
        graph.add_edge(get_random_node(), get_random_node())

    return graph


def extend_graph():
    for i in range(m_param, node_count):
        for j in range(k_param):
            graph.add_edge(i, get_priority_node())
        for k in range(m_param - k_param):
            graph.add_edge(get_random_node(), get_priority_node())


def preview_graph():
    networkx.draw(graph, with_labels=True)
    pyplot.show()


def export_graph():
    networkx.write_gexf(graph,
                        '../out/iasm_m=' + str(m_param) + '_k=' + str(k_param) + '_count=' + str(node_count) + '.gexf')


generate_initial_graph()
extend_graph()
preview_graph()
export_graph()
