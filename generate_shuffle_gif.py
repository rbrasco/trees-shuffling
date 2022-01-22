from tree_shuffle.utils import string_to_tree_space
from tree_shuffle.operad import Operad
from tree_shuffle.lattice import ShuffleLattice

from contextlib import redirect_stdout
import subprocess
import glob
import os



S = string_to_tree_space(
    "0W(b,c;a)|1W(d,e,f;b)|2W(g,h,i;c)", Operad()
)
T = string_to_tree_space(
    "0B(b,c;a)|1B(d;b)|2B(e;c)|3B(f,g;d)|4B(h,i;e)",
    Operad(),
)
shl = ShuffleLattice(S, T)
folder = "/home/rbrasco/Documents/GitHub/trees-shuffling/latex/shuffle_gif/png"
shuffles = shl.get_dictionary()

for key in shuffles.keys():
    name = f'{key.replace("R_{", "").replace("}", "")}.tex'
    with open(f"{folder}/{name}", "w") as f:
        with redirect_stdout(f):
            print("\\documentclass[convert={png,density=1000}]{standalone}")
            print("\\usepackage[all]{xy}")
            print("\\begin{document}")
            shl.print_latex(key=key, labels=False, size_f=(6,8))
            print("\\end{document}")
            # break

# subprocess.run(["cd", folder])
for key in shuffles.keys():
    name = f'{key.replace("R_{", "").replace("}", "")}.tex'
    subprocess.run(["pdflatex", "-shell-escape", name ], cwd=folder)
    # subprocess.call(f"pdflatex -shell-escape {name} & rm !(*.png)",shell=True, cwd=folder)
    # for fl in glob.glob(f"!({folder}/*.png)"):
    #     breakpoint()
    #     os.remove(fl)
    # break


# Comandos para hacer el gif
# ojo rm !(*.png) ojo
# ffmpeg   -framerate 2   -i  %d.png       out.gif ;
