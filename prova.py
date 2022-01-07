from tree_shuffle.utils import string_to_tree_space
from tree_shuffle.operad import Operad
from tree_shuffle.lattice import ShuffleLattice
from tree_shuffle.latex_gen import tree_to_latex, separator


# S = string_to_tree_space("0W(b,c;a)|1W(d,e,f;c)", Operad())
# T = string_to_tree_space("2B(y;x)", Operad())

# shl = ShuffleLattice(S, T)

# shl.print_result_skeleton()
# space = string_to_tree_space(shl.get_dictionary()["R2"], Operad())
# print(space[0].print_self())
# shl.print_latex(labels=True, between=10, size_f=(16,12.5), sort=False)

tree_to_latex("0W(a-y_1,a-y_m;a-x)|1B(b_1-y_1,b_n-y_1;a-y_1)|2B(b_1-y_m,b_n-y_m;a-y_m)", size_f=(25,15), labels=True)
separator(10)
tree_to_latex("0B(b_1-x,b_n-x;a-x)|1W(b_1-y_1,b_1-y_m;b_1-x)|2W(b_n-y_1,b_n-y_m;b_n-x)", size_f=(25,15), labels=True)