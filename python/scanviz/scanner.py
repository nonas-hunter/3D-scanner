from scanviz.communication import Communication

class Scanner():
    """API for interfacing with the scanner"""

    def __init__(self):
        self.comms = Communication()

    def set_position(self, theta_1, theta_2):
        if theta_1 > 999 or theta_2 > 999:
            raise ValueError("Cannot send motor angles greater than 180 deg.")
        message = f"{theta_1:03d}+{theta_2:03d}"
        print(message)
        self.comms.send_recieve("M", message)

    def get_distance(self):
        pass

if __name__ == "__main__":
    scanner = Scanner()
    scanner.set_position(1000,1000)