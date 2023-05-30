import numpy as np
from typing import Optional


class FrameRepresentation:
    """
    A class representing a frame representation with knee and ankle attributes.
    """

    def __init__(
            self,
            right_knee_angle: Optional[float] = None,
            left_knee_angle: Optional[float] = None,
            knee_distance: Optional[float] = None,
            ankle_distance: Optional[float] = None
    ):
        """
        Initializes a FrameRepresentation instance.

        Args:
            right_knee_angle (float, optional): The angle of the right knee. Defaults to None.
            left_knee_angle (float, optional): The angle of the left knee. Defaults to None.
            knee_distance (float, optional): The distance between the knees. Defaults to None.
            ankle_distance (float, optional): The distance between the ankles. Defaults to None.
        """
        self.right_knee_angle = right_knee_angle
        self.left_knee_angle = left_knee_angle
        self.knee_distance = knee_distance
        self.ankle_distance = ankle_distance

    def to_numpy_vector(self):
        """
        Converts the attributes of the FrameRepresentation instance into a numpy vector.

        Returns:
            numpy.ndarray: A 1-dimensional numpy vector containing the attributes.
        """
        attributes = []

        # Retrieve all the attributes dynamically
        for attr_name, attr_value in self.__dict__.items():
            attributes.append(attr_value)

        return np.array(attributes)
