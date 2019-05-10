class Node:
    def __init__(self, value):
        self.value = value
        self.cum_value = value
        self.children = []
        self.visited = False
    def __repr__(self):
        return "Node({})".format(self.value)
def get_input_line():
    return input()
def bfs(root):
    if not root:
        return []
    nodes_ = []
    nodes_q = [root]
    while nodes_q:
        node = nodes_q.pop(0)
        nodes_.append(node)
        node.visited = True
        for i, child in enumerate(node.children):
            if not child.visited:
                nodes_q.append(child)
            else:
                node.children[i] = None
    return nodes_
def get_indexes(edges, index=1):
    visited = set()
    indexes = []
    indexes_q = [index]
    while indexes_q:
        val = indexes_q.pop(0)
        indexes.append(val)
        visited.add(val)
        for other_val in list(edges[val]):
            if other_val in visited:
                edges[val].remove(other_val)
            else:
                indexes_q.append(other_val)
    return indexes
def solve(nodes, x):
    bfs_nodes = bfs(nodes[0])
    # print(bfs_nodes)
    if len(nodes) != len(bfs_nodes):
        raise ValueError("plm")
    for i in range(len(nodes)-1, -1, -1):
        node = bfs_nodes[i]
        for child in node.children:
            if child:
                node.cum_value += child.cum_value
        if node.cum_value < -x:
            node.cum_value = -x
    print(nodes[0].cum_value)
def solve2(values, edges, v):
    indexes = get_indexes(edges, 1)
    for i in range(len(indexes)-1, -1, -1):
        index = indexes[i]
        for j in edges[index]:
            values[index-1] += values[j-1]
        if values[index-1] < -v:
            values[index-1] = -v
    print(values[0])
def main():
    test_count = int(get_input_line())
    for i in range(test_count):
        nodes_count, v = list(map(int, get_input_line().split()))
        values = list(map(int, get_input_line().split()))
        edges = {}
        for j in range(nodes_count-1):
            x, y = list(map(int, get_input_line().split()))
            if x not in edges:
                edges[x] = set()
            edges[x].add(y)
            if y not in edges:
                edges[y] = set()
            edges[y].add(x)
        solve2(values, edges, v)
if __name__ == "__main__":
    main()