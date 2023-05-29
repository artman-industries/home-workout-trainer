import numpy as np

def calculate_angle(a: np.ndarray, b: np.ndarray, c: np.ndarray, unit: str = 'radians') -> float:
    """
    Calculate the angle between points a, b, and c.

    Parameters:
    a: Array representing point a with dimension d.
    b: Array representing point b with dimension d.
    c: Array representing point c with dimension d.
    unit: The unit of the angle to be returned. Possible values: 'radians' (default) or 'degrees'.

    Returns:
    The angle between points a, b, and c. By default, it returns the angle in radians.
    If unit='degrees', it returns the angle in degrees.

    Raises:
    ValueError: If the dimensions of a, b, or c are not equal.
    ValueError: If the unit is not 'radians' or 'degrees'.

    Example:
    >>> a = np.array([1, 0])
    >>> b = np.array([0, 0])
    >>> c = np.array([0, 1])
    >>> calculate_angle(a, b, c)
    1.5707963267948966
    >>> calculate_angle(a, b, c, unit='degrees')
    90.0
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

    if unit == 'degrees':
        angle_deg = np.degrees(angle_rad)
        return float(angle_deg)
    elif unit == 'radians':
        return angle_rad
    else:
        raise ValueError("Invalid unit. Please choose 'radians' or 'degrees'.")


# a = np.array([1, 0])
# b = np.array([0, 0])
# c = np.array([0, 1])
# print(calculate_angle(a, b, c, unit='degrees'))