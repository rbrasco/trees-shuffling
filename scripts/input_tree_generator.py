from collections import defaultdict
import re


class Operad:
    def __init__(self):
        self.colors = {}
        self.operations = {}

    def add_color(self, name, prop={}):
        if name in self.colors.keys():
            t = self.colors[name]
            self.colors[name] = (t, prop)
        else:
            self.colors[name] = prop
        return name

    def add_color_for_trunk(self, name, prop={}):
        t = None
        if name in self.colors.keys():
            t = self.colors[name]
            self.colors[name] = (t, prop)
        else:
            self.colors[name] = prop
        return name, t

    def add_operation(self, name, prop={}):
        self.operations[name] = prop
        return name


class Tree:
    def __init__(self, operation, trunk, branches, operad):

        trunk, parent = operad.add_color_for_trunk(trunk, self)
        self.trunk = trunk
        if parent:
            parent.branches[trunk] = self
        self.branches = {
            operad.add_color(branch, self): uTree(branch) for branch in branches
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


class uTree(Tree):
    def __init__(self, name):
        self.trunk = name
        self.branches = {}
        self.node = None
    def __eq__(self, other):
        # breakpoint()
        return bool(not other.node)


# operad = Operad()
# operads = []

# tree_str = "o0(c2,c1;c0)|o1(c3,c4;c1)|o2(c5,c6;c2)"
# operations = tree_str.split("|")
# regex = r"(o.*)\((.*)\)"
# for operation in operations:
#     match = re.match(regex, operation)
#     if match:
#         operation, parameters = match.groups()
#         branches, trunk = parameters.split(";")
#         operads.append(Tree(operation, trunk, branches.split(","), operad))

# print(operad.colors)
# print(operad.operations)
# t = operads[0]
# # breakpoint()
# print(t.print_edges())



# t = Tree.unitary_tree("hola")
# breakpoint()

t = uTree("hola")
breakpoint()