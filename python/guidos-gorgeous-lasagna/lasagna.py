"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(prep_time):
    """Calculate the lasagna preparation time in minutes.

    Args:
        PREPARATION_TIME (int): Time in minutes to prepare a single layer.

    Returns:
        int: Preparation time in minutes.
    """
    return prep_time * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Display the elapsted time in minutes.

    Args:
        number_of_layers (int): Number of layers in the lasagna.
        elapsed_bake_time (int): Time spent baking.

    Returns:
        int: Elapsed time in minutes.
    """
    return 2*number_of_layers + elapsed_bake_time
