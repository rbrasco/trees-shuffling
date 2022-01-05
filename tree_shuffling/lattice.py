from operations import TreeMerger, TreeManipulator
from operad import Operad
from utils import sorted
from latex_gen import tree_to_latex, separator
from copy import deepcopy
from collections import defaultdict



class ShuffleLattice:
    def __init__(self, S, T):
        self.tm = TreeMerger(deepcopy(S), deepcopy(T))
        self.initial_tree, *self.operations = self.tm.get_result()
        self.skeleton = defaultdict(list)
        self.dictionary = defaultdict(str)
        self.initialize()
        self.generate_shuffles()

    def initialize(self):
        self.dictionary["R0"] = set(self.initial_tree.split("|"))
        self.skeleton["R0"] = []

    def generate_shuffles(self):
        queue = []
        queue.append(self.initial_tree)

        while len(queue):
            tree = queue.pop()
            manipulator = TreeManipulator(tree, *self.operations, Operad())

            tree_key=self.find_key(set(tree.split("|")))
            if not tree_key:
                raise RuntimeError(f"Parent key should be present on dict {tree}")

            for location in manipulator.find_percolant_branches(found=[]):
                fingerprint = manipulator.make_percolation(location)
                if not self.fingerprint_in_skeleton(fingerprint, tree_key):
                    queue.append(fingerprint)

    def fingerprint_in_skeleton(self, fingerprint, parent_key):
        operations = set(fingerprint.split("|"))
        if key := self.find_key(operations):
            self.skeleton[key].append(parent_key)
            return True
        key = f"R{len(self.dictionary)}"
        self.dictionary[key] = operations
        self.skeleton[key].append(parent_key)
        return False

    def find_key(self, operations):
        re = filter(lambda key: operations == self.dictionary[key], self.dictionary.keys())
        return next(re, None)
    
    def get_dictionary(self):
        return {key: "|".join(sorted(list(values))) for key, values in self.dictionary.items()}

    def print_result_skeleton(self):
        print("Number of trees: ", len(self.dictionary))
        print("Dictionary of trees: ", dict(self.get_dictionary()))
        print("Skeleton of trees: ", dict(self.skeleton))
    

    def print_latex(self, key=None, sort=True, size_f=(5, 5), labels=True, label_b=(3, (-2, 0)), between=10):
        sorted_dict = self.get_dictionary()
        if key:
            print(f"Tree {key}: {sorted_dict[key]}")
            tree_to_latex(sorted_dict[key], sort=sort, size_f=size_f, labels=labels, label_b=label_b)
        else:
            print("\\begin{equation}")
            for i, value in enumerate(sorted_dict.values()):
                tree_to_latex(value, sort=sort, size_f=size_f, labels=labels, label_b=label_b)
                separator(between)
                if not (i+1)%5:
                    print("\\end{equation}")
                    print("\\begin{equation}")
            print("\\end{equation}")
            