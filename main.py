
'''
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


class Rectangle:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

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


def first_algorithm(rectangles, points):
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
        print(intersections, end = " ")
    print("\n")


def binarysearch(coord_compressed_keys, target, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if coord_compressed_keys[mid] == target:
            return coord_compressed_keys[mid]
        elif coord_compressed_keys[mid] > target:
            return binarysearch(coord_compressed_keys, target, low, mid-1)
        else:
            return binarysearch(coord_compressed_keys, target, mid + 1, high)
    else:
        elem = max(high,0)
        return coord_compressed_keys[elem]


def second_algorithm(rectangles, points):
    # creating the dictionaries: original coordinates -> compressed coordinates
    x_compressed = {}
    y_compressed = {}
    for rectangle in rectangles:
        x_compressed[rectangle[0]] = 0
        x_compressed[rectangle[2]] = 0
        y_compressed[rectangle[1]] = 0
        y_compressed[rectangle[3]] = 0

    # making sure that 0 gets included
    x_compressed[0] = 0
    y_compressed[0] = 0

    # sorting the dictionaries
    x_compressed = dict(sorted(x_compressed.items()))
    y_compressed = dict(sorted(y_compressed.items()))

    # identifying the compressed coordinates
    compressed = 0
    for kx in x_compressed.keys():
        x_compressed[kx] = compressed
        compressed += 1

    compressed = 0
    for ky in y_compressed.keys():
        y_compressed[ky] = compressed
        compressed += 1
    # print(x_compressed)
    # print(y_compressed)

    matrix = [0] * len(x_compressed)
    for j in range(len(x_compressed)):
        matrix[j] = [0] * len(y_compressed)

    for rectangle in rectangles:
        for x in range(x_compressed[rectangle[0]], x_compressed[rectangle[2]]):
            for y in range(y_compressed[rectangle[1]], y_compressed[rectangle[3]]):
                matrix[x][y] += 1

    for k in range(len(x_compressed)):
        print(matrix[k])

    for point in points:
        coord_compressed_x = list(x_compressed.keys())
        coord_compressed_y = list(y_compressed.keys())
        intersections = 0
        if not (point[0] > coord_compressed_x[-1] or point[1] > coord_compressed_y[-1]):
            x = binarysearch(coord_compressed_x, point[0], 0, len(coord_compressed_x))
            y = binarysearch(coord_compressed_y, point[1], 0, len(coord_compressed_y))
            intersections = matrix[x][y]
        print(intersections, end = " ")


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
