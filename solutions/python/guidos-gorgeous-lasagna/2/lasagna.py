"""
Lasagna cooking time calculations.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # minutes
PREPARATION_TIME = 2     # minutes per layer


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculate the remaining bake time.

    :param elapsed_bake_time: Time already spent baking the lasagna.
    :return: Remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Calculate the preparation time based on the number of layers.

    :param number_of_layers: Number of lasagna layers.
    :return: Preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calculate the total elapsed cooking time.

    :param number_of_layers: Number of lasagna layers.
    :param elapsed_bake_time: Time already spent baking.
    :return: Total elapsed time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
