def equilateral(sides: list) -> bool:
    """
    Determines whether the triangle is equilateral. An equilateral triangle has three sides of equal length.
    :param sides:
    """
    check_side_length_uniqueness = set(sides)
    return len(check_side_length_uniqueness) == 1


def isosceles(sides: list) -> bool:
    """
    Determines whether the triangle is isosceles. An isosceles triangle has at least two sides the same length.
    :param sides:
    """
    check_side_length_uniqueness = set(sides)
    return len(check_side_length_uniqueness) == 2


def scalene(sides: list) -> bool:
    """
    Determines whether the triangle is scalene. Scalene triangles have no sides of equal length.
    :param sides:
    """
    check_side_length_uniqueness = set(sides)
    return len(check_side_length_uniqueness) == 3
