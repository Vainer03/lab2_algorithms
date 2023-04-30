def binary_search(coord_compressed, target, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if coord_compressed[mid] == target:
            return mid
        elif coord_compressed[mid] > target:
            return binary_search(coord_compressed, target, low, mid - 1)
        else:
            return binary_search(coord_compressed, target, mid + 1, high)
    else:
        elem = max(high, 0)
        return elem

class Node:
    def __init__(self, modifier = 0, left_i = 0, right_i = 0):
        self.modifier = modifier
        self.left_i = left_i
        self.right_i = right_i


class Tree:
    def __init__(self, depth = 0):
        self.tree = [0] * pow(2, depth + 1)
        for i in range(len(self.tree)):
            self.tree[i] = Node()

    def build_tree(self):
        for i in range((len(self.tree)) // 2):
            self.tree[(len(self.tree)) // 2 - 1 + i].left_i = i
            self.tree[(len(self.tree)) // 2 - 1 + i].right_i = i
        for i in range((len(self.tree)) // 2 - 2, -1, -1):
            self.tree[i].left_i = self.tree[2 * i + 1].left_i
            self.tree[i].right_i = self.tree[2 * i + 2].right_i


def add_to_tree(tree, cur_i, left, right, delta):
    if tree.tree[cur_i].left_i >= left and tree.tree[cur_i].right_i < right:
        tree.tree[cur_i].modifier += delta
        return
    elif tree.tree[cur_i].right_i < left or tree.tree[cur_i].left_i >= right:
        return
    else:
        add_to_tree(tree, cur_i * 2 + 1, left, right, delta)
        add_to_tree(tree, cur_i * 2 + 2, left, right, delta)
        return


def get_leaf(tree, leaf):
    i = 0
    modifier = 0
    modifier += tree.tree[i].modifier
    while tree.tree[i].left_i != tree.tree[i].right_i:
        if tree.tree[2 * i + 1].right_i >= leaf:
            i = 2 * i + 1
        elif tree.tree[2 * i + 2].left_i <= leaf:
            i = 2 * i + 2
        modifier += tree.tree[i].modifier
    return modifier


def copy_node(node1, node2):
    node2.modifier = node1.modifier
    node2.left_i = node1.left_i
    node2.right_i = node1.right_i


def copy_tree(tree1, tree2):
    for i in range(len(tree1.tree)):
        copy_node(tree1.tree[i], tree2.tree[i])


def third_algorithm(rectangles, points):
    res = ""
    # creating the sets
    x_compressed, y_compressed = set(), set()

    for rectangle in rectangles:
        x_compressed.add(rectangle[0])
        x_compressed.add(rectangle[2])
        y_compressed.add(rectangle[1])
        y_compressed.add(rectangle[3])

    # sorting the sets that were turned into lists
    x_compressed = sorted(x_compressed)
    y_compressed = sorted(y_compressed)

    corners_dict = {}
    corners = []

    rectangle_id = 0
    for rectangle in rectangles:
        rectangle[0] = x_compressed.index(rectangle[0])
        rectangle[2] = x_compressed.index(rectangle[2])
        rectangle[1] = y_compressed.index(rectangle[1])
        rectangle[3] = y_compressed.index(rectangle[3])

        beginning = (rectangle[0], rectangle[1], rectangle_id)
        ending = (rectangle[2], rectangle[3], rectangle_id)
        corners_dict[beginning] = ending

        corners.append(beginning)
        corners.append(ending)
        corners = sorted(corners, key = lambda x: x[0])
        rectangle_id += 1

    depth = 0
    while len(corners) > pow(2, depth):
        depth += 1

    persistent_tree = [0] * len(corners)
    for i in range(len(corners)):
        persistent_tree[i] = Tree(depth)

    tree = Tree(depth)
    tree.build_tree()

    for i in range(len(corners)):
        if corners[i] in corners_dict:
            add_to_tree(tree, 0, corners[i][1], corners_dict[corners[i]][1], 1)
            copy_tree(tree, persistent_tree[corners[i][0]])
        else:
            end_key = 0
            for k, v in corners_dict.items():
                if v == corners[i]:
                    end_key = k
                    break
            add_to_tree(tree, 0, end_key[1], corners[i][1], -1)
            copy_tree(tree, persistent_tree[corners[i][0]])

    for point in points:
        intersections = 0
        if x_compressed[0] <= point[0] <= x_compressed[-1] and y_compressed[0] <= point[1] <= y_compressed[-1]:
            x = binary_search(x_compressed, point[0], 0, len(x_compressed))
            y = binary_search(y_compressed, point[1], 0, len(y_compressed))
            intersections = get_leaf(persistent_tree[x], y)
        res = res + str(intersections) + " "

    res = res[0: len(res) - 1]
    print(res)

Rectangles = []
Points = []
n = int(input())
for i in range(n):
    Rectangles.append(list(map(int, input().split())))
m = int(input())
for i in range(m):
    Points.append(list(map(int, input().split())))
if n == 0:
    print(*[0 for i in range(m)])
else:
    third_algorithm(Rectangles, Points)

'''
2
2 2 5 5
5 5 8 8
2
5 5
8 5
'''