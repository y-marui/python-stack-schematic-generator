from collections.abc import Sequence

import matplotlib.patches as patches
import numpy as np


class Coordinate:
    """
    Represents a coordinate system for drawing stack layers.
    Manages the positions and rotation of the current layer.
    """

    def __init__(
        self,
        x_left: float = 0,
        y_left: float = 0,
        x_right: float = 1,
        y_right: float = 0,
    ) -> None:
        """
        Initialize a Coordinate object.

        Args:
            x_left (float, optional): x-coordinate of the bottom left. Defaults to 0.
            y_left (float, optional): y-coordinate of the bottom left. Defaults to 0.
            x_right (float, optional): x-coordinate of the bottom right. Defaults to 1.
            y_right (float, optional): y-coordinate of the bottom right. Defaults to 0.
        """
        self.x_left: float = x_left
        self.y_left: float = y_left
        self.x_right: float = x_right
        self.y_right: float = y_right
        self.x_center: float = (self.x_right + self.x_left) / 2
        self.y_center: float = (self.y_right + self.y_left) / 2
        self.rotation: float = 0

    def get_polygon(self, layer, delta_figsize: Sequence[float]) -> patches.Polygon:
        """
        Generate a matplotlib Polygon object for the given layer.

        Args:
            layer (Layer): The layer object containing height, slope, and color.
            delta_figsize (list): Figure size scaling factors [width, height].

        Returns:
            patches.Polygon: The polygon representing the layer.
        """
        top_right_y = self.y_right + layer.height + layer.slope
        p = patches.Polygon(
            xy=[
                (self.x_left, self.y_left),
                (self.x_right, self.y_right),
                (self.x_right, top_right_y),
                (self.x_left, self.y_left + layer.height),
            ],
            fc=layer.color,
            fill=True,
            ec="black",
        )

        self.x_center = (self.x_right + self.x_left) / 2
        y_mid = self.y_right + self.y_left + layer.height + layer.slope / 2
        self.y_center = y_mid / 2

        delta_x = (self.x_right - self.x_left) * delta_figsize[0]
        delta_y = (self.y_right - self.y_left + layer.slope / 2) * delta_figsize[1]
        self.rotation = np.atan(delta_y / delta_x) * 180 / np.pi

        self.y_right += layer.height + layer.slope
        self.y_left += layer.height

        return p

    def get_x_max(self):
        """
        Get the maximum x-coordinate.

        Returns:
            float: The maximum x-coordinate.
        """
        return self.x_right

    def get_y_max(self):
        """
        Get the maximum y-coordinate.

        Returns:
            float: The maximum y-coordinate.
        """
        return np.max([self.y_left, self.y_right])
