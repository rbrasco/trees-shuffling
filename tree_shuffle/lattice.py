from operations import TreeMerger, TreeManipulator
from operad import Operad
from tree import uTree
from utils import sorted, print_tree
from latex_gen import tree_to_latex, separator
from copy import deepcopy
from collections import defaultdict
from math import prod


class ShuffleLattice:
    def __init__(self, S, T):
        self.tm_i = TreeMerger(deepcopy(S), deepcopy(T))
        self.i_tree, *self.operations = self.tm_i.get_result()
        # self.f_tree, *_ = TreeMerger(deepcopy(T), deepcopy(S)).get_result()
        self.skeleton = defaultdict(set)
        self.dictionary = defaultdict(str)
        self.nb_percolations = self.sh(S[0], T[0])
        self.initialize()
        self.generate_shuffles()

    def initialize(self):
        self.dictionary["R_{1}"] = set(self.i_tree.split("|"))
        self.skeleton["R_{1}"] = set()
        # self.dictionary[f"R{self.nb_percolations}"] = set(self.f_tree.split("|"))
        # self.skeleton[f"R{self.nb_percolations}"] = set()

    def sh(self, S, T):
        if isinstance(S, uTree) or (S.root and not S.node):
            return 1
        if isinstance(T, uTree) or (T.root and not T.node):
            return 1
        return prod([self.sh(Si, T) for Si in S.branches.values()]) + prod(
            [self.sh(S, Ti) for Ti in T.branches.values()]
        )

    def generate_shuffles(self):
        queue = []
        queue.append(self.i_tree)

        while len(queue):
            tree = queue.pop(0)
            manipulator = TreeManipulator(tree, *self.operations, Operad())

            tree_key = self.find_key(set(tree.split("|")))
            if not tree_key:
                raise RuntimeError(f"Parent key should be present on dict {tree}")

            for location in manipulator.find_percolant_branches(found=[]):
                fingerprint = manipulator.make_percolation(location)
                if not self.fingerprint_in_skeleton(fingerprint, tree_key):
                    queue.append(fingerprint)

    def fingerprint_in_skeleton(self, fingerprint, parent_key):
        operations = set(fingerprint.split("|"))
        if key := self.find_key(operations):
            self.skeleton[key].add(parent_key)
            return True
        key = "R_{" + str(len(self.dictionary) + 1) + "}"
        self.dictionary[key] = operations
        self.skeleton[key].add(parent_key)
        return False

    def find_key(self, operations):
        re = filter(
            lambda key: operations == self.dictionary[key], self.dictionary.keys()
        )
        return next(re, None)

    def get_dictionary(self):
        return {
            key: "|".join(sorted(list(values)))
            for key, values in self.dictionary.items()
        }

    def print_result_skeleton(self):
        print("Number of trees: ", self.nb_percolations)
        print("Number of trees generated: ", len(self.dictionary))
        print("Dictionary of trees: ", dict(self.get_dictionary()))
        print("Skeleton of trees: ", dict(self.skeleton))

    def print_latex(
        self,
        key=None,
        sort=True,
        size_f=(15, 10),
        labels=True,
        label_b=(3, (-2, 0)),
        between=10,
        every=5,
        slice=slice(None),
    ):
        sorted_dict = self.get_dictionary()
        if key:
            print(f"Tree {key}: {sorted_dict[key]}")
            tree_to_latex(
                sorted_dict[key],
                sort=sort,
                size_f=size_f,
                labels=labels,
                label_b=label_b,
                tree_name=key,
            )
        else:
            print("$$")
            li = list(sorted_dict.items())
            for i, (name, value) in enumerate(li[slice]):
                tree_to_latex(
                    value,
                    sort=sort,
                    size_f=size_f,
                    labels=labels,
                    label_b=label_b,
                    tree_name=name,
                )
                separator(between)
                if not (i + 1) % every:
                    print("$$")
                    print("")
                    print("$$")
            print("$$")

    def print_trees(self, key=None, sort=True, mode="self", slice=slice(None)):
        sorted_dict = self.get_dictionary()
        if key:
            print(f"Tree {key}: {sorted_dict[key]}")
            print_tree(
                sorted_dict[key],
                mode=mode,
                sort=sort,
            )
        else:
            li = list(sorted_dict.items())
            for name, value in li[slice]:
                print(f"Tree {name}: {value}")
                print_tree(
                    value,
                    mode=mode,
                    sort=sort,
                )
