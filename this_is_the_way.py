import numpy as np                                          #pip install numpy
from python_tsp.exact import solve_tsp_dynamic_programming  #pip install python-tsp



point_one = (0, 2)
point_two = (2, 5)
point_three = (5, 2)
point_four = (6, 6)
point_five = (8, 3)


def distance_two_points(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def result():
    pass


one_two = distance_two_points(point_one, point_two)
one_three = distance_two_points(point_one, point_three)
one_four = distance_two_points(point_one, point_four)
one_five = distance_two_points(point_one, point_five)
two_three = distance_two_points(point_two, point_three)
two_four = distance_two_points(point_two, point_four)
two_five = distance_two_points(point_two, point_five)
three_four = distance_two_points(point_three, point_four)
three_five = distance_two_points(point_three, point_five)
four_five = distance_two_points(point_four, point_five)

# print(one_two)
# print(one_three)
# print(one_four)
# print(one_five)
# print(two_three)
# print(two_four)
# print(two_five)
# print(three_four)
# print(three_five)
# print(four_five)


distance_matrix = np.array([[0, one_two, one_three, one_four, one_five],
                            [one_two, 0, two_three, two_four, two_five],
                            [one_three, two_three, 0, three_four, three_five],
                            [one_four, two_four, three_four, 0, four_five],
                            [one_five, two_five, three_five, four_five, 0]])

path, distance = solve_tsp_dynamic_programming(distance_matrix)

print(str(point_one) + " > " + str(point_two), str(one_two)
      + " > " + str(point_four), str(two_four)
      + " > " + str(point_five), str(four_five)
      + " > " + str(point_three), str(three_five)
      + " > " + str(point_one), str(one_three) + " =", distance, path)
#(0, 2) > (2, 5) 3.605551275463989 > (6, 6) 4.123105625617661 > (8, 3) 3.605551275463989 > (5, 2) 3.1622776601683795 > (0, 2) 5.0 = 19.49648583671402 [0, 1, 3, 4, 2]
