class Operad:
    def __init__(self):
        self.colors = {}
        self.operations = {}

    def add_color(self, name, prop={}):
        if t:=self.colors.get(name):
            self.colors[name] = (t, prop)
        else:
            self.colors[name] = prop
        return name, t

    def add_operation(self, name, prop={}):
        self.operations[name] = prop
        return name


class Tree:
    def __init__(self, operation, trunk, branches, operad):

        trunk, parent = operad.add_color(trunk, self)
        self.trunk = trunk
        if parent:
            parent.branches[trunk] = self
        self.branches = {
            operad.add_color(branch, self)[0]: uTree(branch) for branch in branches
        }
        self.node = operad.add_operation(operation, self)

    def print_edges(self, depth=0):
        return "".join(
            [f"{str(self.trunk)}\n"]
            + [
                "\t" * (depth + 1) + f"{branch.print_edges(depth + 1)}\n"
                for branch in self.branches.values()
            ]
        )

    def print_nodes(self, depth=0):
        return "".join(
            [f"{str(self.node)}\n"]
            + [
                "\t" * (depth + 1) + f"{branch.print_nodes(depth + 1)}\n"
                for branch in self.branches.values()
            ]
        )

    def __str__(self):
        return f"{self.node}({','.join(self.branches.keys())};{self.trunk})"


class uTree(Tree):
    def __init__(self, name):
        self.trunk = name
        self.branches = {}
        self.node = None

import re

def string_to_tree_space(string, operad):

    operads = []
    operations = string.split("|")
    regex = r"(.*)\((.*)\)"
    for operation in operations:
        match = re.match(regex, operation)
        if not match:
            raise RuntimeError(f"Operation not defined correctly {operation}")
        operation, parameters = match.groups()
        branches, trunk = parameters.split(";")
        operads.append(Tree(operation, trunk, branches.split(","), operad))
    return operads[0], operad


def tree_space_to_string(tree_space):
    _, operad = tree_space
    return "|".join(str(tree) for tree in operad.operations.values())


# S = string_to_tree_space("o0w(c2,c1;c0)", Operad())
# T = string_to_tree_space("o0b(d2,d1;d0)", Operad())
# T = string_to_tree_space("o0w(c2,c1;c0)|o1w(c3,c4;c1)|o2w(c5,c6;c2)", Operad())
# S = string_to_tree_space("o0b(d2,d1;d0)|o1b(d3,d4;d1)|o2b(d5,d6;d2)", Operad())
# S = string_to_tree_space("W(b,c;a)", Operad())
# T = string_to_tree_space("B(1;0)", Operad())
# S = string_to_tree_space("0W(1;0)|1W(2,3;1)", Operad())
# T = string_to_tree_space("0B(b,d;a)|1B(c;b)|2B(e;d)", Operad())
# S = string_to_tree_space("0W(1;0)|1W(2,4,6;1)|2W(3;2)|3W(5;4)|4W(7;6)", Operad())
# T = string_to_tree_space("0B(b,f;a)|1B(c;b)|2B(d;c)|3B(e;d)|4B(;f)", Operad())
S = string_to_tree_space("0W(1;0)|1W(2,3;1)|2W(;3)", Operad())
T = string_to_tree_space("0B(b,c;a)|1B(;c)", Operad())
print(tree_space_to_string(S))
print(tree_space_to_string(T))


import math
def Sh(S, T):
    if isinstance(S, uTree) and isinstance(T, uTree):
        return str(S), str(T)
    if isinstance(S, uTree):
        return str(S), [Sh(S, Ti) for Ti in T.branches.values()]
    if isinstance(T, uTree):
        return [Sh(Si, T) for Si in S.branches.values()], str(T)

    return [Sh(Si, T) for Si in S.branches.values()], [
        Sh(S, Ti) for Ti in T.branches.values()
    ]

# Sin simetria
def sh(S, T):
    if isinstance(S, uTree):
        return 1 
    if isinstance(T, uTree):
        return  1
    breakpoint()
    return prod([sh(Si, T) for Si in S.branches.values()]) + prod([
        sh(S, Ti) for Ti in T.branches.values()
    ])
    
def prod(array):
    if not len(array):
        print("hey")
        return 0
    x = 1
    for e in array:
        x*=e
    return x
    
Sh_lattice = Sh(S[0], T[0])
sh_number = sh(S[0], T[0])
print(sh_number)
