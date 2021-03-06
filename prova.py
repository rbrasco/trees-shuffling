from tree_shuffle.utils import string_to_tree_space
from tree_shuffle.operad import Operad
from tree_shuffle.lattice import ShuffleLattice

S = string_to_tree_space("0W(b;a)|1W(d;b)", Operad())
T = string_to_tree_space("0B(b,c;a)|1B(d;c)", Operad())
shl = ShuffleLattice(S, T)
shl.print_result_skeleton()