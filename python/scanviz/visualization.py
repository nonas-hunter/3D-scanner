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
        """
        pitch = np.linspace(-(np.pi / 2), (np.pi / 2), resolution)
        yaw = np.linspace(-(np.pi / 2), (np.pi / 2), resolution)
        pitch_mesh, yaw_mesh = np.meshgrid(pitch, yaw)
        return pitch_mesh, yaw_mesh

    def create_viz(self, pitch, yaw, radius):
        """Create a matplotlib graph to visualize the data."""
        x = radius * np.sin(yaw) * np.cos(pitch)
        y = radius * np.sin(pitch)
        z = radius * np.cos(pitch) * np.cos(yaw)

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