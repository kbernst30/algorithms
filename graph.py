DIRECTED = "DIRECTED"
UNDIRECTED = "UNDIRECTED"


class Graph:

    def __init__(self, mode=DIRECTED):
        self.nodes = {}
        self.mode = mode

    def add_node(self, value):
        if value not in self.nodes:
            node = Node(value)
            self.nodes[value] = node
            return node
        else:
            return self.nodes[value]

    def add_edge(self, source, destination):

        source_node = self.add_node(source)
        destination_node = self.add_node(destination)

        source_node.add_adjacent(destination_node)
        if self.mode == UNDIRECTED:
            destination_node.add_adjacent(source_node)

        return (source_node, destination_node)

    def remove_node(self, value):
        if value in self.nodes:
            node = self.nodes[value]
            if self.mode == UNDIRECTED:
                for adj_node in node.get_adjacents():
                    adj_node.remove_adjacent(node)

            del self.nodes[value]

            return node

        return None

    def remove_edge(self, source, destination):

        source_node = self.add_node(source)
        destination_node = self.add_node(destination)

        source_node.remove_adjacent(destination_node)
        if self.mode == UNDIRECTED:
            destination_node.remove_adjacent(source_node)

        return (source_node, destination_node)

    def breadth_first_search(self):
        pass

    def depth_first_search(self):
        pass


class Node:

    def __init__(self, value):
        self.value = value
        self.adjacents = []

    def add_adjacent(self, node):
        if node not in self.adjacents:
            self.adjacents.append(node)

    def remove_adjacent(self, node):
        if node in self.adjacents:
            self.adjacents.remove(node)

    def get_adjacents(self):
        return self.adjacents

    def is_adjacent(self, node):
        return node in self.adjacents
