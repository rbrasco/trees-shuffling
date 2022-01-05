from tree_shuffle.utils import string_to_tree_space
from tree_shuffle.operad import Operad
from tree_shuffle.lattice import ShuffleLattice


S = string_to_tree_space("0W(1;0)|1W(2,3;1)", Operad())
T = string_to_tree_space("0B(b,d;a)|1B(c;b)|2B(e;d)", Operad())

shl = ShuffleLattice(S, T)

shl.print_result_skeleton()
space = string_to_tree_space(shl.get_dictionary()["R1"], Operad())
print(space[0].print_self())
shl.print_latex(labels=True, between=5)