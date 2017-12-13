from collections import OrderedDict


class Node:

    def __init__(self, name, parent=None):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        if not self.children:
            return "Node {n}".format(n = self.name)
        return "Node {n}, children {c}".format(n=self.name, c=[ch.name for ch in self.children])


def parse_and_create_node(line):
    words = line.split(" <-> ")

    name = words[0]
    node = Node(name)

#    children = words[1].split(", ")
#
#    node.add(children)

    return node


def parse_child_names(line):
    return line.split(" <-> ")[1].split(", ")


def create_tree(read_lines):
    created_nodes = OrderedDict()

    for line in read_lines:
        new_node = parse_and_create_node(line)
        created_nodes.update({new_node.name: new_node})

    return created_nodes


def assign_children(orphan_nodes, read_input):

    for parent, child_spec in zip(orphan_nodes, read_input):
        child_names = parse_child_names(child_spec)
        for name in child_names:
            child = orphan_nodes[name]
            par = orphan_nodes[parent]
            par.add_child(child)


def get_group(origin, group_members=set()):
    print(origin)

    group_members.add(origin)

    for child in origin.children:
        if child not in group_members:
            group_members.add(child)
            group_members.update(get_group(child))

    return group_members


if __name__ == "__main__":
    with open("input.txt") as f:
        read_pipes = [l.strip() for l in f.readlines()]

    nodes = create_tree(read_pipes)
    assign_children(nodes, read_pipes)

    group_0 = get_group(nodes['0'])
    print("Part 1:", len(group_0))

    groups = set(nodes.values())
    print(groups)
    count = 0
    while groups:
        count += 1
        group = get_group(groups.pop())
        # print(group)
        groups.difference_update(group)

    print(count)
