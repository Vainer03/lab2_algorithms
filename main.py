import copy
import time

# =============== Auxiliary functions for testing ======================
# this function prints out the matrix in a programmer's way
def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print(matrix[x][y], end = "\t")
        print("")


'''
0 1 2 3 4 5 y
1
2
3
x
'''


# while this function prints out the matrix in a mathematical way
def print_matrix_turned(matrix):
    for y in range(len(matrix[0]) - 1, -1, -1):
        for x in range(len(matrix)):
            print(matrix[x][y], end = "\t")
        print("")


'''
y 
3
2
1
0 1 2 3 4 5 x
'''


def get_time(start,finish):
    return int(1000000*(finish - start))


def generated_testing_rectangles(n, rectangles):
    for i in range(n):
        rectangles.append([10 * i, 10 * i, 10 * (2 * n - i), 10 * (2 * n - i)])
    return rectangles


def generated_testing_points(m, points):
    for i in range(m):
        points.append([pow(87178291199 * i, 31) % (20 * m), pow(39916801 * i, 31) % (20 * m)])
    return points


# the first algorithm and the auxiliary functions for it
def first_algorithm(rectangles, points):
    start = time.perf_counter()
    res = ""
    for point in points:
        intersections = 0
        x = point[0]
        y = point[1]
        for rectangle in rectangles:
            x1 = rectangle[0]
            x2 = rectangle[2]
            y1 = rectangle[1]
            y2 = rectangle[3]
            if (x >= x1) and (x < x2) and (y >= y1) and (y < y2):
                intersections += 1
        res = res + str(intersections) + " "
    res = res[0: len(res) - 1]
    print(res)
    finish = time.perf_counter()
    return get_time(start, finish)


# the second algorithm and the auxiliary functions for it
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


def second_algorithm(rectangles, points):
    start = time.perf_counter()
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

    matrix = [0] * len(x_compressed)
    for j in range(len(x_compressed)):
        matrix[j] = [0] * len(y_compressed)

    for rectangle in rectangles:
        rectangle[0] = x_compressed.index(rectangle[0])
        rectangle[2] = x_compressed.index(rectangle[2])
        rectangle[1] = y_compressed.index(rectangle[1])
        rectangle[3] = y_compressed.index(rectangle[3])
        for x in range(rectangle[0], rectangle[2]):
            for y in range(rectangle[1], rectangle[3]):
                matrix[x][y] += 1

    for point in points:
        intersections = 0
        if x_compressed[0] <= point[0] <= x_compressed[-1] and y_compressed[0] <= point[1] <= y_compressed[-1]:
            x = binary_search(x_compressed, point[0], 0, len(x_compressed))
            y = binary_search(y_compressed, point[1], 0, len(y_compressed))
            intersections = matrix[x][y]
        res = res + str(intersections) + " "
    res = res[0: len(res) - 1]
    print(res)
    finish = time.perf_counter()
    return get_time(start, finish)


# the third algorithm and the auxiliary functions for it
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
    start = time.perf_counter()
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
    finish = time.perf_counter()
    return get_time(start, finish)


def testing(t, k):
    results = [0] * k
    for i in range(k):
        results[i] = [0]*4
        results[i][0] = str(i+1) + '). '

    for i in range(k):
        rectangles = []
        generated_testing_rectangles(2**i, rectangles)
        points = []
        generated_testing_points(2**(i+1), points)
        for j in range(t):
            results[i][1] += first_algorithm(rectangles, points)
            results[i][2] += second_algorithm(copy.deepcopy(rectangles), points)
            results[i][3] += third_algorithm(copy.deepcopy(rectangles), points)
        results[i][1] //= t
        results[i][2] //= t
        results[i][3] //= t
    return results


def user_interaction_main_menu():
    print("Enter the number of the mode")
    print("0 - Entering the coordinates manually")
    print("1 - Generated coordinates for both rectangles and points but numbers are entered manually")
    print("2 - Generated and automated testing")
    print("3 - Exit")
    mode = input()
    match mode:
        case "0":
            n = int(input())
            rectangles = []
            for i in range(n):
                rectangles.append(list(map(int, input().split())))
            m = int(input())
            points = []
            for i in range(m):
                points.append(list(map(int, input().split())))

            first_algorithm(copy.deepcopy(rectangles), copy.deepcopy(points))
            second_algorithm(copy.deepcopy(rectangles), copy.deepcopy(points))
            third_algorithm(copy.deepcopy(rectangles), copy.deepcopy(points))
        case "1":
            n = int(input("Enter the number of rectangles: "))
            rectangles = []
            generated_testing_rectangles(n, rectangles)
            m = int(input("Enter the number of points: "))
            points = []
            generated_testing_points(m, points)

            first_algorithm(copy.deepcopy(rectangles), copy.deepcopy(points))
            second_algorithm(copy.deepcopy(rectangles), copy.deepcopy(points))
            third_algorithm(copy.deepcopy(rectangles), copy.deepcopy(points))
        case "2":
            res = testing(100, 8)
            for i in res:
                print(i[0], i[1], i[2], i[3])
        case "3":
            exit()
        case _:
            print("I'm not quite sure what you want me to do...")
            user_interaction_main_menu()


# the main function
if __name__ == '__main__':
    print("Welcome to the Laboratory Task №2!")
    user_interaction_main_menu()


'''
4
2 2 6 8
5 4 9 10
4 0 11 6
8 2 12 12
5
2 2
12 12
10 4
5 5
2 10


3
11 15 57 61
23 21 31 32
27 23 35 44
2
29 26
33 17


2
1 1 7 7
3 3 5 5
9
3 0
3 1
3 2
3 3
3 4
3 5
3 6
3 7
3 8
'''
