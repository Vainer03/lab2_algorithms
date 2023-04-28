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


n = int(input())
Rectangles = []
for i in range(n):
    Rectangles.append(list(map(int, input().split())))

m = int(input())
Points = []
for i in range(m):
    Points.append(list(map(int, input().split())))

first_algorithm(Rectangles, Points)
