from copy import deepcopy
from utils import tree_to_string, sorted, string_to_tree_space
from tree import uTree


class TreeMerger:
    def __init__(self, S, T):
        self.S_og_space = S
        self.T_og_space = T
        self.tree_str = self.merge(deepcopy(S[0]), deepcopy(T[0]))

    def get_result(self):
        return (
            self.tree_str,
            self.S_og_space[1].operations,
            self.T_og_space[1].operations,
        )

    def merge(self, S, T):
        self.add_color_base(S, T.trunk)
        return tree_to_string(S)

    def add_color_edge(self, T, c, depth):
        T.trunk = f"{c}-{T.trunk}"
        T.branches = self.rename_keys(T, c, True)
        T.depth += depth
        for Ti in T.branches.values():
            self.add_color_edge(Ti, c, depth)
        return T

    def rename_keys(self, S, c, inv=False):
        aux = {}
        for i, Si in S.branches.items():
            if not inv:
                aux[f"{i}-{c}"] = Si
            else:
                aux[f"{c}-{i}"] = Si
        return aux

    def add_color_base(self, S, c):
        S.trunk = f"{S.trunk}-{c}"
        S.branches = self.rename_keys(S, c)
        for i, Si in S.branches.items():
            if isinstance(Si, uTree):
                S.branches[i] = self.add_color_edge(
                    deepcopy(self.T_og_space[0]), i.split("-")[0], S.depth + 1
                )
            else:
                self.add_color_base(Si, c)


class TreeManipulator:
    def __init__(self, tree_str, S_og_operations, T_og_operations, operad):
        self.tree_str = tree_str
        self.S_og_operations = S_og_operations
        self.T_og_operations = T_og_operations
        self.tree, self.operad = string_to_tree_space(tree_str, operad)

    def find_percolant_branches(self, S=None, found=[]):
        if not S:
            S = self.tree
        if S.node in self.S_og_operations.keys():
            if any(
                branch.node in self.T_og_operations.keys()
                for branch in S.branches.values()
            ):
                found.append(S)

        for Si in S.branches.values():
            self.find_percolant_branches(Si, found)
        return found

    def make_percolation(self, location):
        operations = self.tree_str.split("|")
        branches = list(location.branches.values())
        new_node = branches[0].node
        old_node = location.node
        to_change = [str(location)] + [str(branch) for branch in branches]
        old_operation = self.S_og_operations[old_node]
        new_operation = self.T_og_operations[new_node]

        morfed = []
        for _, c in new_operation.branches.items():
            morfed.append(
                f"{old_operation.node}({','.join(map(lambda x: x+'-'+c.trunk, old_operation.branches.keys()))};{old_operation.trunk}-{c.trunk})"
            )
        morfed.append(
            f"{new_operation.node}({','.join(map(lambda x: old_operation.trunk+'-'+x, new_operation.branches.keys()))};{old_operation.trunk}-{new_operation.trunk})"
        )

        for branch in to_change:
            operations.remove(branch)
        operations += morfed
        operations = sorted(operations)
        new_tree = "|".join(operations)
        return new_tree
