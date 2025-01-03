# Lab 6
# shortest_distance.py


import math


def dist(p1, p2):
    return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))


def shortest_distance(points):
    num = 1
    distance = dist(points[1], points[0])

    # compare the first point with all other points and get the shortest distance from that
    # then compare the 2nd point with all other points but the first point since those have already been compared
    for base_point in points:
        for j in range(num, len(points)):
            if  dist(points[j], base_point) < distance:
                distance = dist(points[j], base_point)
        num += 1  # skip all points before the point being compared with
    return distance
                    

def main():
    print(dist([10, 78], [-2, 50]) == 30.463092423455635)
    print(shortest_distance([[8, -5], [0, 9], [8, 1], [3, 4], [-10, -4]]) == 5.830951894845301)
    print(shortest_distance([[45, -99], [24, 83], [-48, -68], [-97, 99], [-8, -77], [-2, 50], [44, 41], [-48, -58], [-1, 53], [14, 86], [31, 94], [12, -91], [33, 50], [82, 72], [83, -90], [10, 78], [7, -22], [90, -88], [-21, 5], [6, 23]]) == 3.1622776601683795)


if __name__ == '__main__':
    main()
