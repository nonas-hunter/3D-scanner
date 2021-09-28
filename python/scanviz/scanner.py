import time

from scanviz.communication import Communication

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
        print(f"Setting servo positions to (pitch) {pitch}, (yaw) {yaw}.")
        message = f"{pitch:03d}+{yaw:03d}"
        response = self.comms.send_recieve("M", message)
        if int(response["data"]) == 0:
            raise ValueError("Servo did not respond. Stopping program.")
        else:
            time.sleep(int(response["data"]))
        print("Servo positions have been set.")

    def get_distance(self):
        pass