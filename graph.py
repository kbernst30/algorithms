from queue import Queue


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

    def breadth_first_search(self, source):
        queue = Queue()

        source_node = self.add_node(source)
        queue.put(source_node)

        visited = []

        while not queue.empty():
            next_node = queue.get()

            print(next_node.value)

            visited.append(next_node)

            for neighbor in next_node.get_adjacents():
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.put(neighbor)

    def depth_first_search(self, source, visited=None):
        source_node = self.add_node(source)

        if visited is None:
            visited = []

        if source_node not in visited:
            visited.append(source_node)
            print(source_node.value)
            for child in source_node.get_adjacents():
                self.depth_first_search(child.value, visited)


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


if __name__ == '__main__':

    graph = Graph(UNDIRECTED)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(5, 2)
    graph.add_edge(6, 3)
    graph.add_edge(7, 3)
    graph.add_edge(8, 4)
    graph.add_edge(9, 5)
    graph.add_edge(10, 6)

    graph.breadth_first_search(1)
    print("\n")
    graph.breadth_first_search(9)
    print("\n")
    graph.depth_first_search(1)
