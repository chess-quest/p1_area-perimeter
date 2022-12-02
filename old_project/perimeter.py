import math


def perimeter_func(shape, value_1, value_2, value_3):
    match shape:
        case 1:
            return math.pi * value_1 * 2
        case 2:
            return value_1 * 2 + value_2 * 2
        case 3:
            return value_1 * 4
        case 4:
            return value_3 + value_2 + value_1
