import time
import logging
import logging.config
import os

import numpy as np
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
        yaw = np.linspace(-60, 60, resolution*2)
        pitch_mesh, yaw_mesh = np.meshgrid(pitch, yaw)
        return pitch_mesh, yaw_mesh

    def create_viz(self, pitch, yaw, radius):
        """Create a matplotlib graph to visualize the data."""
        pitch_rad = np.deg2rad(pitch)
        yaw_rad = np.deg2rad(yaw)
        x = radius * np.sin(yaw_rad) * np.cos(pitch_rad)
        y = radius * np.sin(pitch_rad)
        z = radius * np.cos(pitch_rad) * np.cos(yaw_rad)

        # 2D Contour
        fig = plt.figure(figsize=plt.figaspect(2.))
        fig.suptitle('3D Scan')

        ax_2D = fig.add_subplot(1, 2, 2)

        contour = ax_2D.contourf(x, y, z)
        ax_2D.set_aspect('equal', 'box')
        fig.colorbar(contour, ax=ax_2D, shrink=0.5)

        # 3D Render   
        ax_3D = fig.add_subplot(1, 2, 1, projection='3d')

        surf = ax_3D.plot_surface(
            x,
            z,
            y,
            rstride=1,
            cstride=1,
            cmap=plt.get_cmap('jet'),
            linewidth=0,
            antialiased=False,
            alpha=0.5,
        )

        fig.tight_layout()
        plt.show()