
def earliest_ancestor(ancestors, starting_node, visited=None):
    if visited is None:
        visited = []

    for i in ancestors:
        if i[1] == starting_node:
            visited.append(i[0])
            return earliest_ancestor(ancestors, i[0], visited)

    for i in ancestors:
        if i[0] == starting_node and i[0] in visited:
            return i[0]

    return -1