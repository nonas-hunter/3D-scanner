import serial
import time

class Communication():
    """Infrastructure for serial communication with the Arduino"""

    EOM = "\n"

    def __init__(self, port='/dev/ttyACM0', baudrate=115200):
        """Instantiate a Communication object.

        Parameters:
            port (str): The serial port where the arduino is connected.
            baudrate (int): The baudrate of the serial port. This should match the
                baudrate set on the arduino.
        """
        self.arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)

    def send(self, message_type, message_data):
        """Send data to the arduino
        """
        message = f"{message_type}{message_data}{self.EOM}"
        self.arduino.write(bytes(message, 'utf-8'))
        
    def receive(self):
        """Receive data from the arduino
        """
        data = self.arduino.readline()
        return data

# Systems Test
if __name__ == "__main__":
    comms = Communication()
    while True:
        message = comms.receive()
        print(type(message))
        print(message)
        time.sleep(0.5)