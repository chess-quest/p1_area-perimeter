import math


def perimeter_func(shape, value_1, value_2, value_3) -> float:
    """
    Solves the perimeter of a shape with dimensions given by the user
    :param shape: Index of the shape from the dropdown box
    :param value_1: Numeraic value 1
    :param value_2: Numeraic value 2
    :param value_3: Numeraic value 3
    :return: Perimiter of the shape
    """
    match shape:
        case 1:
            return value_1 * 4
        case 2:
            return value_1 * 2 + value_2 * 2
        case 3:
            return math.pi * value_1 * 2
        case _:
            return value_3 + value_2 + value_1


def area_func(shape, value_1, value_2) -> float:
    """"
    Solves the area of a shape with dimensions given by the user
    :param shape: Index of the shape from the dropdown box
    :param value_1: First numeraic value
    :param value_2: Second numeric value
    :return: Area of the shape
    """
    match shape:
        case 1:
            return value_1**2
        case 2:
            return value_1 * value_2
        case 3:
            return math.pi * value_1**2
        case _:
            return value_1 * value_2 * 0.5
