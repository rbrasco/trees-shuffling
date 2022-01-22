import igraph as ig
from utils import string_to_tree_space
from operad import Operad


def tree_to_latex(
    tree,
    sort=False,
    size_f=(15, 10),
    labels=True,
    label_b=(3, (-2, 0)),
    tree_name=None,
):
    T = string_to_tree_space(tree, Operad(), sort=sort)
    G = ig.Graph()
    _recursive_add_edges(T[0], G)
    layout = G.layout_reingold_tilford(mode="in", root=[0])
    vertices = list(zip(G.vs()["label"], layout.coords))
    edges = list((e["label"], e.tuple) for e in G.es)

    layout = layout.scale(1)

    scaled_vertices = list(
        map(
            lambda x: (
                x[0],
                (
                    round(x[1][0] * size_f[0], 2),
                    round(x[1][1] * size_f[1], 2),
                ),
            ),
            vertices,
        )
    )

    print("\\xy")
    print("<0.08cm, 0cm>:")

    print("%Vertices%")
    for i, vertex in enumerate(scaled_vertices):
        print(
            str(vertex[1])
            + node_name(vertex[0])
            + f'="{(i+1)}"; %{vertex[0]}'
        )

    print("%Edges%")
    for _, edge in edges:
        print(
            f'"{edge[0]+1}";"{edge[1]+1}"' + " **\dir{-};"
        )

    def get_label(name):
        if "root" in name or "leaf" in name:
            return None
        name = name.strip("B").strip("W")
        return (
            f"({name.split('-')[0]},"
            + "\\text{ }"
            + f"{name.split('-')[1]})"
            if "-" in name
            else name
        )

    if labels:
        print("%Labels%")
        for i, vertex in enumerate(scaled_vertices):
            pos = (vertex[1][0] + label_b[0], vertex[1][1])
            if name := get_label(vertex[0]):
                print(
                    str(pos)
                    + "*=0{\\scriptstyle "
                    + name
                    + "};"
                )

        for name, (s, t) in edges:
            label = get_label(name)
            s_pos = scaled_vertices[s][1]
            t_pos = scaled_vertices[t][1]
            pos = (
                round(
                    (s_pos[0] + t_pos[0]) / 2
                    + label_b[1][0],
                    2,
                ),
                round(
                    (s_pos[1] + t_pos[1]) / 2
                    + label_b[1][1],
                    2,
                ),
            )
            print(
                str(pos)
                + "*=0{\\scriptstyle "
                + label
                + "};"
            )
    if tree_name:
        print("(-13,0)*{" + tree_name + "};")
    print("\\endxy")


def has_node(graph, name):
    try:
        graph.vs.find(name=name)
    except:
        return False
    return True


def _recursive_add_edges(T, G):
    if T.root:
        s_n = f"root_{T.trunk}"
        t_n = (
            f"{T.node}-{T.trunk}"
            if T.node
            else f"leaf_{T.trunk}"
        )
        t_label = T.node if T.node else f"leaf_{T.trunk}"
        if not has_node(G, s_n):
            G.add_vertex(s_n, label=s_n)
        if not has_node(G, t_n):
            G.add_vertex(t_n, label=t_label)
        G.add_edge(s_n, t_n, label=T.trunk)

    if T.node:
        s_n = f"{T.node}-{T.trunk}"
        s_label = f"{T.node}"
        if not has_node(G, s_n):
            G.add_vertex(s_n, label=s_label)
        for branch in T.branches.values():
            t_n = (
                f"{branch.node}-{branch.trunk}"
                if branch.node
                else f"leaf_{branch.trunk}_from_{T.node}"
            )
            t_label = (
                branch.node
                if branch.node
                else f"leaf_{branch.trunk}"
            )
            if not has_node(G, t_n):
                G.add_vertex(t_n, label=t_label)
            G.add_edge(s_n, t_n, label=branch.trunk)
            _recursive_add_edges(branch, G)


def node_name(name):
    if "W" in name:
        return "*\cir<2pt>{}"
    if "B" in name:
        return "*=0{\\bullet}"
    return "*{}"


def separator(size):
    print("\\xy")
    print("<0.08cm, 0cm>:")
    print(f"(-{size}" + ', 0.0)*{}="1";')
    print(f"({size}" + ', 10.0)*{}="2";')
    print("\endxy")
