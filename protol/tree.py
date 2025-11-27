class TreeBuilder:
    def __init__(self):
        self.struct = []
        self.index = 0

    def add(self, obj):
        if self.index == 0:
            self.struct.append(obj)
        

    def structure(self):
        return self.struct

    def __enter__(self):
        print("xuy")
        self.index += 1
        if self.index - 1 == 0:
            self.struct.append([])    
        return self.struct

    def __exit__(self, *args, **kwargs):
        pass


tree = TreeBuilder()
print(tree.structure())
tree.add("1st")
print(tree.structure())
with tree:
    tree.add("2nd")
    with tree:
        tree.add("3nd")
    tree.add("4nd")
print(tree.structure())
