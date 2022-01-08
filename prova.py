from tree_shuffle.utils import string_to_tree_space
from tree_shuffle.operad import Operad
from tree_shuffle.lattice import ShuffleLattice
from tree_shuffle.latex_gen import tree_to_latex, separator


S = string_to_tree_space("0W(1;0)|1W(2,3;1)", Operad())
T = string_to_tree_space("0B(b,d;a)|1B(c;b)|2B(e;d)", Operad())

shl = ShuffleLattice(S, T)

shl.print_result_skeleton()
# space = string_to_tree_space(shl.get_dictionary()["R_2"], Operad())
# print(space[0].print_self())
# shl.print_latex(labels=False, between=10, size_f=(10,5), sort=False, every=3, slice=slice(3, None))

tree_to_latex("0W(;a-x)")
separator(20)
tree_to_latex("0B(b_1-x,b_n-x;a-x)|1W(;b_1-x)|2W(;b_n-x)", size_f=(25,10))