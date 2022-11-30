import math


def area_func(shape, value_1, value_2):
    match shape:
        case 1:
            return math.pi * value_1**2
        case 2:
            return value_1 * value_2
        case 3:
            return value_1**2
        case 4:
            return value_1 * value_2 * 0.5
