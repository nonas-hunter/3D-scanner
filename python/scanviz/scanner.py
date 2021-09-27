from scanviz.communication import Communication

class Scanner():
    """API for interfacing with the scanner"""

    def __init__(self):
        self.comms = Communication()

    def set_position(self, theta_1, theta_2):
        pass

    def get_distance(self):
        pass
