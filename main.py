point_one = (0, 2)
point_two = (2, 5)
point_three = (5, 2)
point_four = (6, 6)
point_five = (8, 3)


def distance_two_points(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def result():
    pass



a = distance_two_points(point_one, point_two)
print(a)
