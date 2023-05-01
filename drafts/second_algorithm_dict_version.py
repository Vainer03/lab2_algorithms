def print_matrix_turned(matrix):
    for y in range(len(matrix[0]) - 1, -1, -1):
        for x in range(len(matrix)):
            print(matrix[x][y], end = "\t")
        print("")


def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print(matrix[x][y], end = "\t")
        print("")


def binarysearch_v1(coord_compressed_keys, target, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if coord_compressed_keys[mid] == target:
            return coord_compressed_keys[mid]
        elif coord_compressed_keys[mid] > target:
            return binarysearch_v1(coord_compressed_keys, target, low, mid-1)
        else:
            return binarysearch_v1(coord_compressed_keys, target, mid + 1, high)
    else:
        elem = max(high,0)
        return coord_compressed_keys[elem]


def second_algorithm_v1(rectangles, points):
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
        print_matrix_turned(matrix)
        print("\n")

    # print_matrix(matrix)
    # print("\n")
    print_matrix_turned(matrix)


'''
    for point in points:
        coord_compressed_x = list(x_compressed.keys())
        coord_compressed_y = list(y_compressed.keys())
        intersections = 0
        if not (point[0] > coord_compressed_x[-1] or point[1] > coord_compressed_y[-1]):
            x = binarysearch_v1(coord_compressed_x, point[0], 0, len(coord_compressed_x))
            y = binarysearch_v1(coord_compressed_y, point[1], 0, len(coord_compressed_y))
            intersections = matrix[x][y]
        print(intersections, end = " ")
'''