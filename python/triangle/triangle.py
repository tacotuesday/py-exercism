""" Group of functions to classify three-member lists as different types of triangles. This would make a great set
of class methods, but that probably wouldn't pass tests."""


def is_triangle(sides):
    return sum(sides) != 0 and (
        sides[0] + sides[1] >= sides[2]
        and sides[1] + sides[2] >= sides[0]
        and sides[0] + sides[2] >= sides[1]
    )


def equilateral(sides: list) -> bool:
    """
    Determines whether the triangle is equilateral. An equilateral triangle has three sides of equal length.
    :param sides:
    """
    return is_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list) -> bool:
    """
    Determines whether the triangle is isosceles. An isosceles triangle has at least two sides the same length.
    :param sides:
    """
    return is_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: list) -> bool:
    """
    Determines whether the triangle is scalene. Scalene triangles have no sides of equal length.
    :param sides:
    """
    return is_triangle(sides) and len(set(sides)) == 3
