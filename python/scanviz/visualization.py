import time
import logging
import logging.config
import os

import numpy as np
import scipy.signal as scipy
import matplotlib.pyplot as plt
from matplotlib import ticker, cm

logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(logger_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Visualization():
    """Tools for visualizing scanner data."""
    def __init__(self):
        """Instantiate visualization object"""
        pass

    def generate_mesh(self, resolution):
        """Generate pitch & yaw angles for scanning
        
        Parameters:
            resolution (int): Number of points to scan
        Returns:
            (list): List of lists outlining all the pitch values to scan.
            (list): List of lists outlining all the yaw values to scan.
        """
        if resolution > 60:
            raise ValueError("Resolution can't be higher than 180")
        pitch = np.linspace(-30, 30, resolution)
        yaw = np.linspace(-30, 30, resolution)
        pitch_mesh, yaw_mesh = np.meshgrid(pitch, yaw)
        return pitch_mesh, yaw_mesh

    def _moving_avg(self, data):
        window = np.ones((2, 2)) / 4
        return scipy.convolve2d(data, window, 'valid')
    
    def create_viz(self, pitch, yaw, radius):
        """Create a matplotlib graph to visualize the data."""
        smooth_radius = self._moving_avg(radius) 
        pitch_rad = [row[1:] for row in np.deg2rad(pitch)[1:,:]]
        yaw_rad = [row[1:] for row in np.deg2rad(yaw)[1:,:]]
        # Unfiltered Output
        # smooth_radius = radius
        # pitch_rad = np.deg2rad(pitch)
        # yaw_rad = np.deg2rad(yaw)
        x = smooth_radius * np.sin(yaw_rad) * np.cos(pitch_rad)
        y = smooth_radius * np.sin(pitch_rad)
        z = smooth_radius * np.cos(pitch_rad) * np.cos(yaw_rad)

        fig = plt.figure(figsize=plt.figaspect(2.))
        fig.suptitle('3D Scan')

        # 2D Contour
        ax_2D = fig.add_subplot(1, 2, 2)

        contour = ax_2D.contourf(x, y, z)
        ax_2D.set_aspect('equal', 'box')
        fig.colorbar(contour, ax=ax_2D, shrink=0.5)

        # 3D Render   
        ax_3D = fig.add_subplot(1, 2, 1, projection='3d')

        surf = ax_3D.scatter(
            x,
            z,
            y,
        )

        fig.tight_layout()
        plt.show()