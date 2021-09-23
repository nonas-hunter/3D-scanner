import serial
import time

class Communication():
    """Infrastructure for serial communication with the Arduino."""

    EOM = "\r\n"
    SEND_MESSAGE_TYPES = ["M", "S"]
    RECIEVE_MESSAGE_TYPES = ["R"]

    def __init__(self, port='/dev/ttyACM0', baudrate=115200, timeout=1):
        """Instantiate a Communication object.

        Parameters:
            port (str): the serial port where the arduino is connected.
            baudrate (int): the baudrate of the serial port. This should match the
                baudrate set on the arduino.
        """
        self.arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)

    def send(self, message_type, message_data):
        """Send data to the arduino.

        Parameters:
            message_type (str): the message type. Must be a type listed in the send
                message type list stored in the communications class.
            message_data (str): data to be send over the serial bus to the arduino.
        
        Raises:
            ValueError: when the message type does not match a message type listed
                in the SEND_MESSAGE_TYPES list.
        """
        if message_type not in self.SEND_MESSAGE_TYPES:
            raise ValueError(f"Incorrect message type: {message_type}")
        message = f"{message_type}{message_data}{self.EOM}"
        self.arduino.write(bytes(message, 'utf-8'))
        
    def receive(self):
        """Receive data from the arduino.

        Returns:
            (dict): contains message type, processed data, and error value.
        """
        raw_data = self.arduino.readline()
        message_type = raw_data[0]
        if message_type in self.RECIEVE_MESSAGE_TYPES:
            data = raw_data.split["\n"][0].split["\r"][0][1:]
            return {
                "message_type": message_type,
                "data": data,
                "error": 0,
            }
        else:
            return {
                "message_type": "ERROR",
                "data": raw_data,
                "error": 1,
            }

# Systems Test
if __name__ == "__main__":
    comms = Communication()
    while True:
        message = comms.receive()
        print(type(message))
        print(message)
        time.sleep(0.5)