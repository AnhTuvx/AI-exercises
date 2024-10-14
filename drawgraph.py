# import networkx as nx
# import matplotlib.pyplot as plt
#
# def draw_graph_from_adjacency_matrix(adj_matrix):
#     G = nx.Graph()
#
#     # Thêm các cạnh từ ma trận kề
#     for i in range(len(adj_matrix)):
#         for j in range(len(adj_matrix[i])):
#             if adj_matrix[i][j] != 0:
#                 G.add_edge(i, j, weight=adj_matrix[i][j])
#
#     # Vẽ đồ thị
#     pos = nx.spring_layout(G, seed=42)  # Giữ vị trí cố định
#     plt.figure(figsize=(8, 6))  # Kích thước hình ảnh
#     nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12,
#             edge_color='gray', arrowsize=20, width=2)
#     edge_labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
#
#     plt.show()
#
#
# def draw_directed_graph_from_adjacency_matrix(adj_matrix):
#     G = nx.DiGraph()  # Sử dụng DiGraph cho đồ thị có hướng
#
#     # Thêm các cạnh từ ma trận kề
#     for i in range(len(adj_matrix)):
#         for j in range(len(adj_matrix[i])):
#             if adj_matrix[i][j] != 0:
#                 G.add_edge(i, j)
#
#     pos = nx.spring_layout(G, seed=42)  # Giữ vị trí cố định
#     plt.figure(figsize=(8, 6))  # Kích thước hình ảnh
#     nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12,
#             edge_color='gray', arrowsize=20, width=2)
#     edge_labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
#
#     plt.title("Directed Graph from Adjacency Matrix")
#     plt.axis('off')  # Tắt hệ trục
#     plt.show()
#
#     plt.show()