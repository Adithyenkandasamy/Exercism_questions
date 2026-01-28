"""
Ghost Gobble Arcade Game logic.
"""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Determine if Pac-Man eats a ghost.

    :param power_pellet_active: Whether the power pellet is active
    :param touching_ghost: Whether Pac-Man is touching a ghost
    :return: True if ghost is eaten, else False
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """
    Determine if the player scores points.

    :param touching_power_pellet: Player touches a power pellet
    :param touching_dot: Player touches a dot
    :return: True if player scores, else False
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Determine if the player loses the game.

    :param power_pellet_active: Whether power pellet is active
    :param touching_ghost: Player touches a ghost
    :return: True if player loses, else False
    """
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Determine if the player wins the game.

    :param has_eaten_all_dots: Whether all dots are eaten
    :param power_pellet_active: Whether power pellet is active
    :param touching_ghost: Player touches a ghost
    :return: True if player wins, else False
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
