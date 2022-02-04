from tree_shuffle.utils import string_to_tree_space, print_tree
from tree_shuffle.operad import Operad
from tree_shuffle.lattice import ShuffleLattice
from tree_shuffle.latex_gen import tree_to_latex, separator

S = string_to_tree_space("0W(b;a)|1W(d;b)", Operad())
T = string_to_tree_space("0B(b,c;a)|1B(d;c)", Operad())
# S = string_to_tree_space("0W(b,c;a)|1W(d,e,f;b)|2W(g,h,i;c)", Operad())
# T = string_to_tree_space("0B(b,c;a)|1B(d;b)|2B(e;c)|3B(f,g;d)|4B(h,i;e)", Operad())
# S = string_to_tree_space("0W(1;0)|1W(2,4,6;1)|2W(3;2)|3W(5;4)|4W(7;6)", Operad())
# T = string_to_tree_space("0B(b,f;a)|1B(c;b)|2B(d;c)|3B(e;d)|4B(g;f)", Operad())
# S = string_to_tree_space("0W(b,c;a)|1W(d,e,f;c)", Operad())
# T = string_to_tree_space("0B(y;x)", Operad())
# tree_to_latex("0W(1;0)|1W(2,4,6;1)|2W(3;2)|3W(5;4)|4W(7;6)")
#  tree_to_latex("0B(b,f;a)|1B(c;b)|2B(d;c)|3B(e;d)|4B(g;f)")
shl = ShuffleLattice(S, T)
shl.print_result_skeleton()
# space = string_to_tree_space(shl.get_dictionary()["R_{2}"], Operad())
# print(space[0].print_self())
# shl.print_latex(labels=False, between=5, size_f=(3,5), sort=False, every=2)

# tree_to_latex("0B(e_1,b,c_1;a)|1B(c_2;c_1)|2B(;c_2)|3B(e_2;e_1)|4B(d,f;e_2)", tree_name="T", labels=True)
# # separator(20)
# tree_to_latex("0B(e,d,c_1;a)|1B(c_2;c_1)|2B(;c_2)|3B(b,f;e)", tree_name="T\\backslash v", labels=True)