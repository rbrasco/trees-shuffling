from tree_shuffle.utils import string_to_tree_space, print_tree
from tree_shuffle.operad import Operad
from tree_shuffle.lattice import ShuffleLattice
from tree_shuffle.latex_gen import tree_to_latex, separator

# S = string_to_tree_space("0W(1;0)|1W(2,4,6;1)|2W(3;2)|3W(5;4)|4W(7;6)", Operad())
# T = string_to_tree_space("0B(b,f;a)|1B(c;b)|2B(d;c)|3B(e;d)|4B(g;f)", Operad())
# S = string_to_tree_space("0W(b,c;a)|1W(d,e,f;c)", Operad())
# T = string_to_tree_space("0B(y;x)", Operad())
# tree_to_latex("0W(1;0)|1W(2,4,6;1)|2W(3;2)|3W(5;4)|4W(7;6)")
# tree_to_latex("0B(b,f;a)|1B(c;b)|2B(d;c)|3B(e;d)|4B(g;f)")
# shl = ShuffleLattice(S, T)

# shl.print_result_skeleton()
# shl.print_trees()
# space = string_to_tree_space(shl.get_dictionary()["R_2"], Operad())
# print(space[0].print_self())
# shl.print_latex(labels=False, between=10, size_f=(5,5), sort=False, every=4)

tree_to_latex("c\\otimes qB(b_1,b_2;b)|wW(\\Omega;b_1)", tree_name="S", size_f=(20,15))
# separator(20)
# tree_to_latex("0B(b_1-x,b_n-x;a-x)|1W(;b_1-x)|2W(;b_n-x)", size_f=(25,10))