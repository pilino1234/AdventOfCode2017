

class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

        self.parent = None
        self.children = []

    def add_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return self.name + " (" + str(self.weight) + ")" + " parent: (" + str(self.parent) +\
               "), children: (" + str(len(self.children)) + ")"

    def __str__(self):
        return self.__repr__()


def get_tower_weight(root):
    return int(root.weight) + sum(get_tower_weight(child) for child in root.children)


def read_node_data(input_text):
    words = input_text.split()
    name = words[0]

    weight = int(words[1][1:-1])

    return Node(name, weight)


def read_child_data(input_text):
    if "->" not in input_text:
        return None

    name = input_text.split()[0]

    children = [child.strip("\n") for child in input_text.split("-> ")[1].split(", ")]

    return {name: children}


def create_nodes(read_lines):
    nodes = {}

    for line in read_lines:
        new_node = read_node_data(line)
        nodes.update({new_node.name: new_node})

    return nodes


def assign_children(nodes, input_text):

    children = {}

    for line in input_text:
        child = read_child_data(line)
        if child is not None:
            children.update(child)

    for parent, child_list in children.items():
        parent_node = nodes[parent]

        for child in child_list:
            child_node = nodes[child]

            # Store the parent node in the child
            child_node.add_parent(parent_node)

            # Assign the child node to the parent
            parent_node.add_child(child_node)

    return nodes


def get_differing_index(lst):
    st = set(lst)

    for val in st:
        if lst.count(val) == 1:
            return lst.index(val)


def get_diff_from_list(lst):
    st = list(set(lst))
    d_idx = get_differing_index(st)

    if max(st) == st[d_idx]:
        return min(st) - st[d_idx]
    else:
        return max(st) - st[d_idx]
    

def balance_tower(root):
    weights = []

    for tower in root.children:
        weight = get_tower_weight(tower)
        weights.append(weight)

    diff_idx = get_differing_index(weights)

    if diff_idx is not None:
        if balance_tower(root.children[diff_idx]) == -1:
            # If a recursive call found that all towers beyond a certain point are balanced,
            # it will return -1, and this code will run to find child node that has a bad weight

            new_weight = int(root.children[diff_idx].weight) + get_diff_from_list(weights)

            print("Child with bad weight is", root.children[diff_idx])
            print("Its weight should be changed by", get_diff_from_list(weights), "to", new_weight)
    else:
        # All towers from this root are balanced, so this root must be the culprit
        return -1


if __name__ == "__main__":
    with open("input.txt") as f:
        read_programs = f.readlines()

    #read_programs = [
    #    ["pbga (66)"],
    #    ["xhth (57)"],
    #    ["ebii (61)"],
    #    ["havc (66)"],
    #    ["ktlj (57)"],
    #    ["fwft (72) -> ktlj, cntj, xhth"],
    #    ["qoyq (66)"],
    #    ["padx (45) -> pbga, havc, qoyq"],
    #    ["tknk (41) -> ugml, padx, fwft"],
    #    ["jptl (61)"],
    #    ["ugml (68) -> gyxo, ebii, jptl"],
    #    ["gyxo (61)"],
    #    ["cntj (57)"]
    #]

    programs = create_nodes(read_programs)

    structure = assign_children(programs, read_programs)

    root = None
    for node in structure.values():
        if node.parent is None:
            root = node

    print("Root node:", root, "\n")

    balance_tower(root)
