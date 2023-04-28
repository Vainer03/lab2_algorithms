
# =============== Auxiliary functions for testing ======================
# this function prints out the matrix in a programmer's way
def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print(matrix[x][y], end = "\t")
        print("")


'''
0 y y y y y y y
x
x
x
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
y
y
y
0 x x x x x x x
'''


# the first algorithm and the auxiliary functions for it
def first_algorithm(rectangles, points):
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
    res = res[0: len(res)-1]
    print(res)


# the second algorithm and the auxiliary functions for it
def binary_search(coord_compressed, target, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if coord_compressed[mid] == target:
            return mid
        elif coord_compressed[mid] > target:
            return binary_search(coord_compressed, target, low, mid-1)
        else:
            return binary_search(coord_compressed, target, mid + 1, high)
    else:
        elem = max(high,0)
        return elem


def second_algorithm(rectangles, points):
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
        for x in range(x_compressed.index(rectangle[0]), x_compressed.index(rectangle[2])):
            for y in range(y_compressed.index(rectangle[1]), y_compressed.index(rectangle[3])):
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


# the main function
if __name__ == '__main__':
    print("Welcome to the Laboratory Task №2!")
    n = int(input())
    Rectangles = []
    for i in range(n):
        Rectangles.append(list(map(int, input().split())))

    m = int(input())
    Points = []
    for i in range(m):
        Points.append(list(map(int, input().split())))

    first_algorithm(Rectangles, Points)
    second_algorithm(Rectangles, Points)


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
'''