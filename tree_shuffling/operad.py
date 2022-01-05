class Operad:
    def __init__(self):
        self.colors = {}
        self.operations = {}

    def add_color(self, name, prop={}):
        if t := self.colors.get(name):
            self.colors[name] = (t, prop)
        else:
            self.colors[name] = prop
        return name, t

    def add_operation(self, name, prop={}):
        self.operations[name] = prop
        return name