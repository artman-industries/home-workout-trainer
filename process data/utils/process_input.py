import numpy as np
from enum import Enum
import math

class AngleUnit(Enum):
    RADIANS = 'radians'
    DEGREES = 'degrees'


def calculate_angle(a: np.ndarray, b: np.ndarray, c: np.ndarray, unit: AngleUnit = AngleUnit.RADIANS) -> float:
    """
    Calculate the angle between points a, b, and c.

    Parameters:
    a: Array representing point a with dimension d.
    b: Array representing point b with dimension d.
    c: Array representing point c with dimension d.
    unit (AngleUnit, optional): The unit of the angle representation (degrees or radians).
            Defaults to AngleUnit.RADIANS.
    Returns:
        float: The angle between points ABC in the specified unit.

    Raises:
    ValueError: If the dimensions of a, b, or c are not equal.
    ValueError: If the unit is not 'radians' or 'degrees'.

    Example:
        a = np.array([1, 0])
        b = np.array([0, 0])
        c = np.array([0, 1])

        calculate_angle(a, b, c, unit=AngleUnit.RADIANS) = 1.5707963267948966
    """
    if a.shape != b.shape or b.shape != c.shape:
        raise ValueError("Dimensions of a, b, and c must be equal.")

    # Calculate vectors ab and bc
    ab = b - a
    bc = c - b

    # Calculate dot product of ab and bc
    dot_product = np.dot(ab, bc)

    # Calculate magnitudes of ab and bc
    magnitude_ab = np.linalg.norm(ab)
    magnitude_bc = np.linalg.norm(bc)

    # Calculate the angle using the dot product and magnitudes
    angle_rad = np.arccos(dot_product / (magnitude_ab * magnitude_bc))

    if unit == AngleUnit.DEGREES:
        angle = math.degrees(angle_rad)
    else:
        angle = angle_rad
    return angle

# a = np.array([1, 0])
# b = np.array([0, 0])
# c = np.array([0, 1])
# print(calculate_angle(a, b, c, unit='degrees'))
