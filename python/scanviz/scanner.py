import time
import logging
import logging.config
import os

import numpy as np
from scanviz.communication import Communication
from scanviz.visualization import Visualization

logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(logger_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Scanner():
    """API for interfacing with the scanner"""

    def __init__(self):
        self.comms = Communication()
        self.viz = Visualization()

    def set_position(self, pitch, yaw):
        """Send a message to the Arduino to set the pitch and roll of the Scanner.

        Parameters:
            pitch (float): Representing the desired pitch angle.
            yaw (float): Representing the desired yaw angle.
        """
        if pitch > 180 or yaw > 180:
            raise ValueError("Cannot send motor angles greater than 180 deg.")
        logger.debug(
            "Setting servo positions to (pitch)"
            f" {int(round(pitch))}, (yaw) {int(round(yaw))}."
        )
        message = f"{int(round(pitch)):03d}+{int(round(yaw)):03d}"
        response = self.comms.send_recieve("M", message)
        if int(response["data"]) == 0:
            raise ValueError("Servo did not respond. Stopping program.")
        else:
            time.sleep(int(response["data"]))
        logger.debug("Servo positions have been set.")

    def get_distance(self):
        """Send a message to Arduino to send three distance measurements over serial.

        Returns:
            (float): Calibrated output from distance sensor in inches.
        """
        logger.debug("Getting measured sensor distance.")
        response = self.comms.send_recieve("S", "GET")
        logger.debug(f"Information recieved: {response['data']}")
        raw_data = response["data"].split(",")
        output = []
        for data in raw_data:
            output += [48.7 - (0.15 * int(data)) + (0.000134 * (int(data)**2))]
        logger.debug(f"Measured Value: {min(output)}")
        return min(output)

    def sweep(self, resolution):
        """Sweep over a set of pitch and yaw values and collect distance data.
        
        Parameters:
            resolution (int): Determines the number of measurements taken by the
                sensor. The number of measurements equals (2*(resolution**2)).
        """
        pitch_mesh, yaw_mesh = self.viz.generate_mesh(resolution)
        radius_mesh = []
        for row in range(len(pitch_mesh)):
            radius_mesh_row = []
            for col in range(len(pitch_mesh[row])):
                self.set_position(pitch_mesh[row][col], yaw_mesh[row][col])
                radius_mesh_row += [self.get_distance()]
            radius_mesh += [radius_mesh_row]
        self.viz.create_viz(pitch_mesh, yaw_mesh, radius_mesh)