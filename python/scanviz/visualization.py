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
    
    def create_viz(self):
        """Create a matplotlib graph to visualize the data."""
        pitch, yaw = np.linspace(-(np.pi / 2), (np.pi / 2), 40), np.linspace(-(np.pi / 2), (np.pi / 2), 40)
        meshgrid_pitch, meshgrid_yaw = np.meshgrid(pitch, yaw)
        print(meshgrid_pitch[:,0])
        r = meshgrid_pitch/meshgrid_pitch
        x = r * np.sin(meshgrid_yaw) * np.cos(meshgrid_pitch)
        y = r * np.sin(meshgrid_pitch)
        z = r * np.cos(meshgrid_pitch) * np.cos(meshgrid_yaw)

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