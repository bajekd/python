class Vertex:
    def __init__(self, name):
        self.name = name
        self.node = None


class Node:
    def __init__(self, height, node_id, parent_node):
        self.height = height
        self.node_id = node_id
        self.parent_node = parent_node


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    """Override compare and less than operator -> need to establish for what characteristic sorted by"""
    def __cmp__(self, other_edge):
        return self.cmp(self.weight, other_edge.weight)

    def __lt__(self, other_edge):
        self_priority = self.weight
        other_edge_priority = other_edge.weight
        return self_priority < other_edge_priority


class UnionFind:
    def __init__(self, vertices_list):
        self.vertices_list = vertices_list
        self.root_nodes = []
        self.count_nodes = 0
        self.count_sets = 0
        self.make_sets(vertices_list)

    def make_sets(self, vertices_list):
        for vertex in vertices_list:
            self.make_set(vertex)

    def make_set(self, vertex):
        node = Node(0, len(self.root_nodes), None)
        vertex.parent_node = node
        self.root_nodes.append(node)
        self.count_nodes += 1
        self.count_sets += 1

    def find(self, node):
        """Return id of root for given node"""
        current_node = node

        while current_node.parent_node is not None:
            current_node = current_node.parent_node
        root = current_node

        """Path compression"""
        current_node = node
        while current_node is not root:
            temp = current_node.parent_node
            current_node.parent_node = root
            current_node = temp

        return root.node_id

    def union(self, node_1, node_2):
        """'Merge' given nodes if their root's id are not the same"""
        index_1 = self.find(node_1)
        index_2 = self.find(node_2)

        if index_1 == index_2:
            return

        root_1 = self.root_nodes[index_1]
        root_2 = self.root_nodes[index_2]

        if root_1.height > root_2.height:
            root_2.parent_node = root_1
        elif root_1.height < root_2.height:
            root_1.parent_node = root_2
        else:
            root_1.parent_node = root_2
            root_2.height += 1

        self.count_sets -= 1

    def construct_spanning_tree(self, vertices_list, edges_list):
        disjoint_set = UnionFind(vertices_list)
        spanning_tree = []

        edges_list.sort()
        for edge in edges_list:
            s_0 = edge.start_vertex
            s_1 = edge.target_vertex

            if disjoint_set.find(s_0.parent_node) is not disjoint_set.find(s_1.parent_node):
                spanning_tree.append(edge)
                disjoint_set.union(s_0.parent_node, s_1.parent_node)

        """
        for edge in spanning_tree:
            print(f'{edge.start_vertex.name} --- {edge.target_vertex.name}'
        """