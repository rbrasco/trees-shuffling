from tree import Tree, uTree
from operad import Operad
import re


def string_to_tree_space(string, operad, sort=True):
    operads = []
    operations = string.split("|")
    if sort:
        operations = sorted(operations)
    for i, operation in enumerate(operations):
        operation, trunk, branches = extract_info(operation)
        operads.append(
            Tree(operation, trunk, branches, operad, not i)
        )
    return operads[0], operad


def tree_space_to_string(tree_space):
    _, operad = tree_space
    return "|".join(
        str(tree) for tree in operad.operations.values()
    )


def _recursive_str(tree, s):
    s.append(str(tree))
    for branch in tree.branches.values():
        if not isinstance(branch, uTree):
            _recursive_str(branch, s)
    return s


def tree_to_string(tree):
    operations = sorted(_recursive_str(tree, []))
    return "|".join(operations)


def extract_info(item):
    regex = r"(.*)\((.*)\)"
    match = re.match(regex, item)
    if not match:
        raise RuntimeError(
            f"Operation not defined correctly {item}"
        )
    operation, parameters = match.groups()
    branches, trunk = parameters.split(";")
    return (
        operation,
        trunk,
        branches.split(",") if branches else [],
    )


def sorted(operations):
    n = len(operations)
    items = list(
        map(lambda x: (extract_info(x), x), operations)
    )
    i = 0
    while i < n:
        item1 = items[i]
        for j in range(i + 1, n):
            item2 = items[j]
            if item1[0][1] in item2[0][2]:
                items.pop(i)
                items.insert(j, item1)
                break
        else:
            i += 1
    return list(map(lambda x: x[1], items))


def print_tree(tree, mode, sort=True):
    if mode in ["self", "nodes", "edges"]:
        T = string_to_tree_space(tree, Operad(), sort)
        print(eval(f"T[0].print_{mode}()"))
    else:
        raise RuntimeError(
            f"Print tree mode {mode} does "
            + "not exist, try: self, nodes or edges"
        )
