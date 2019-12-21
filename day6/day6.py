import argparse


class OrbitNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def get_name(self):
        return self.name

    def add_child(self, child):
        self.children.append(child)


class OrbitGraph:
    """
    Directed graph of orbit nodes:
    Directed edges of the form
        A --> B
    if B orbits A.
    """

    def __init__(self, COM, nodes):
        self.COM = COM
        self.nodes = nodes
        self.num_direct_orbits = 0    # Track number of direct orbits
        self.num_indirect_orbits = 0  # Track number of indirect orbits

    def dfs(self, node, steps, visited):
        """
        DFS helper to count indirect orbits. If we have gone more than 1 step
        into the recursion, then the number of indirect orbits is steps-1. This
        is because if we have made it at least 2 steps into the recursion, then
        an ancestor, which is at least the grandparent of the current node
        called this path in the recursion tree. The current node will by
        definition be indirect to all its ancestors that are not parents, which
        is tracked by steps.
        """

        visited += [node]

        if steps > 1:
            self.num_indirect_orbits += steps - 1

        for child in node.children:
            if child not in visited:
                self.dfs(child, steps + 1, visited)

    def count_direct_orbits(self):
        """
        The number of direct orbits is just the size of the edge set for the
        graph.
        """

        visited = [self.COM]
        self.num_direct_orbits = len(self.COM.children)
        stack = [node for node in self.COM.children]
        while stack:
            node = stack.pop()
            visited.append(node)
            self.num_direct_orbits += len(node.children)
            for child in node.children:
                if child not in visited:
                    stack.append(child)
        return self.num_direct_orbits

    def count_indirect_orbits(self):
        """
        Call DFS helper to keep track number of indirect orbits.
        """

        visited = []
        self.dfs(self.COM, 0, visited)
        return self.num_indirect_orbits


def construct_orbit_graph(orbits):
    orbit_nodes = {}
    for orbit in orbits:
        parent_name, child_name = orbit
        child_name = child_name.strip()

        if parent_name in orbit_nodes:
            parent_node = orbit_nodes[parent_name]
            if child_name in orbit_nodes:
                child_node = orbit_nodes[child_name]
            else:
                child_node = OrbitNode(child_name)
                orbit_nodes[child_name] = child_node
            parent_node.add_child(child_node)
        else:
            parent_node = OrbitNode(parent_name)
            orbit_nodes[parent_name] = parent_node
            if child_name in orbit_nodes:
                child_node = orbit_nodes[child_name]
            else:
                child_node = OrbitNode(child_name)
                orbit_nodes[child_name] = child_node
            parent_node.add_child(child_node)

    graph = OrbitGraph(orbit_nodes["COM"], list(orbit_nodes.values()))
    return graph


def construct_orbit_transfer_graph(orbits):
    orbit_nodes = {}
    for orbit in orbits:
        parent_name, child_name = orbit
        child_name = child_name.strip()

        if parent_name in orbit_nodes:
            parent_node = orbit_nodes[parent_name]
            if child_name in orbit_nodes:
                child_node = orbit_nodes[child_name]
            else:
                child_node = OrbitNode(child_name)
                orbit_nodes[child_name] = child_node
            parent_node.add_child(child_node)
        else:
            parent_node = OrbitNode(parent_name)
            orbit_nodes[parent_name] = parent_node
            if child_name in orbit_nodes:
                child_node = orbit_nodes[child_name]
            else:
                child_node = OrbitNode(child_name)
                orbit_nodes[child_name] = child_node
            parent_node.add_child(child_node)

    graph = OrbitGraph(orbit_nodes["COM"], list(orbit_nodes.values()))
    return graph


def compute_orbit_count_checksum(input_file="input.txt"):
    if not input_file.endswith(".txt"):
        raise NameError(f"{input_file} is not a .txt file.")

    orbits = None
    checksum = 0

    with open(input_file) as f:
        orbits = [orbit.split(")") for orbit in f]

    if orbits:
        orbit_graph = construct_orbit_graph(orbits)
        num_direct_orbits = orbit_graph.count_direct_orbits()
        num_indirect_orbits = orbit_graph.count_indirect_orbits()
        checksum = num_direct_orbits + num_indirect_orbits

    else:
        raise NameError(f"File {input_file} could not be read.")

    return checksum


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input file of orbits.")

    args = parser.parse_args()
    input_file = args.input_file

    checksum = compute_orbit_count_checksum(input_file)

    print("-------------------- Part One --------------------")
    print(f"Orbit count checksum: {checksum}")

    print("-------------------- Part Two --------------------")
