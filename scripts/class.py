class Node:
    name: str
    prop: dict
    
    def __init__(self, name, **prop):
        self.name = name
        self.prop = prop
    def __str__(self):
        return self.name

class Edge:
    name: str
    prop: dict

    def __init__(self, name, **prop):
        self.name = name
        self.prop = prop
    def __str__(self):
        return self.name


class Tree:
    trunk: Edge
    branches: list = []
    node: Node = None

    def __init__(self, name, **prop):
        self.trunk = Edge(name, **prop)
    
    def add_node(self, name, **prop):
        self.node = Node(name, **prop)

    def add_branch(self, tree):
        self.branches.append(tree)
    
    def add_branches(self, names, **prop):
        for name in names:
            self.add_branch(name, **prop)
    
    def get_branches(self):
        return [str(t.trunk) for t in self.branches]

def _recursive(n, name="e", depth=0):
    t = Tree(f"{name}-{depth}")
    
    if n <= 0:
        return t
    t.add_node(str(t.trunk))
    t.add_branch(_recursive(n-1, str(t.trunk), depth+1 ))

    return t

t = _recursive(1)
breakpoint()