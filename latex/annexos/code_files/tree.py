class Tree:
    def __init__(
        self, operation, trunk, branches, operad, root=False
    ):
        self.root = root

        trunk, parent = operad.add_color(trunk, self)
        self.trunk = trunk
        if parent:
            parent.branches[trunk] = self
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.branches = {
            operad.add_color(branch, self)[0]: uTree(
                branch, depth=self.depth
            )
            for branch in branches
        }
        self.node = operad.add_operation(operation, self)

    def print_edges(self):
        return "".join(
            [f"{str(self.trunk)}\n"]
            + [
                "\t" * (self.depth + 1)
                + f"{branch.print_edges()}\n"
                for branch in self.branches.values()
            ]
        )

    def print_nodes(self):
        return "".join(
            [f"{str(self.node)}\n"]
            + [
                "\t" * (self.depth + 1)
                + f"{branch.print_nodes()}\n"
                for branch in self.branches.values()
            ]
        )

    def print_self(self):
        return "".join(
            [f"{str(self)}\n"]
            + [
                "\t" * (self.depth + 1)
                + f"{branch.print_self()}\n"
                for branch in self.branches.values()
            ]
        )

    def __str__(self):
        return (
            f"{self.node}({','.join(self.branches.keys())}"
            + f";{self.trunk})"
        )

    def __repr__(self):
        return (
            f"{self.node}({','.join(self.branches.keys())}"
            + f";{self.trunk})"
        )


class uTree(Tree):
    def __init__(self, name, depth, root=False):
        self.trunk = name
        self.branches = {}
        self.node = None
        self.depth = depth
        self.root = root
