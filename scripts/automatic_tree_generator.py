class Operad:
    def __init__(self, n=1):
        self.colors = {f"c{i}": None for i in range(n)} or {}
        self.operations = {f"o{i}": None for i in range(n)} or {}

    def get_next_color(self, prop={}):
        for color, obj in self.colors.items():
            if not obj:
                self.colors[color] = True or prop
                return color
        color = f"c{len(self.colors)}"
        self.colors[color] = True or prop
        return color

    def get_next_operation(self, prop={}):
        for operation, obj in self.operations.items():
            if not obj:
                self.operations[operation] = True or prop
                return operation
        operation = f"o{len(self.operations)}"
        self.operations[operation] = True or prop
        return operation


class Tree:
    def __init__(self, depth=0, prop={}, operad=None):
        self.operad = Operad() if not operad else operad
        self.trunk = Edge(self.operad.get_next_color(), prop)
        self.branches = []
        self.depth = depth
        self.node = None

    def add_node(self, prop={}):
        self.node = Node(self.operad.get_next_operation(), prop)

    def add_branch(self, tree):
        self.branches.append(tree)

    def get_branch(self, index):
        return self.branches[index]

    def get_node(self):
        return self.node

    def __str__(self):
        return "".join(
            [f"{str(self.trunk)}\n"]
            + ["\t" * (self.depth + 1) + f"{str(branch)}\n" for branch in self.branches]
        )


class Node:
    def __init__(self, name, prop):
        self.name = name
        self.prop = prop

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, name, prop):
        self.name = name
        self.prop = prop

    def __str__(self):
        return self.name
