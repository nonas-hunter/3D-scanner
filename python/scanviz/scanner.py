import time
import logging
import logging.config
import os

from scanviz.communication import Communication

logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(logger_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Scanner():
    """API for interfacing with the scanner"""

    def __init__(self):
        self.comms = Communication()

    def set_position(self, pitch, yaw):
        """Send a message to the Arduino to set the pitch and roll of the Scanner.

        Parameters:
            pitch (int): An integer representing the desired pitch angle.
            yaw (int): An integer representing the desired yaw angle.
        """
        if pitch > 999 or yaw > 999:
            raise ValueError("Cannot send motor angles greater than 180 deg.")
        logger.debug(f"Setting servo positions to (pitch) {pitch}, (yaw) {yaw}.")
        message = f"{pitch:03d}+{yaw:03d}"
        response = self.comms.send_recieve("M", message)
        if int(response["data"]) == 0:
            raise ValueError("Servo did not respond. Stopping program.")
        else:
            time.sleep(int(response["data"]))
        logger.debug("Servo positions have been set.")

    def get_distance(self):
        logger.debug("Getting measured sensor distance.")
        response = self.comms.send_recieve("S", "GET")
        logger.debug(f"Information recieved: {response['data']}")
        raw_data = int(response["data"])
        output = 48.7 - (0.15 * raw_data) + (0.000134 * (raw_data**2))
        logger.debug(f"Measured Value: {output}")
        return output

    def sweep(self):
        pass