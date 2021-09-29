import time
import serial.tools.list_ports
import logging
import logging.config
import os

import serial

logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(logger_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Communication():
    """Infrastructure for serial communication with the Arduino."""

    EOM = "\r\n"
    SEND_MESSAGE_TYPES = ["M", "S", "T"]
    RECIEVE_MESSAGE_TYPES = ["M", "S","T"]

    def __init__(self, baudrate=115200, port=None):
        """Instantiate a Communication object.

        Parameters:
            baudrate (int): the baudrate of the serial port. This should match the
                baudrate set on the arduino.
            port (str): the serial port where the arduino is connected.
        """
        def port_sort(port):
            """Sort the list of serial ports. For use in sort function.

            Parameters:
                port (serial.tools.list_port): Serial port object.
            Returns:
                (int): 1 if A in port.device, 2 if Arduino in port.description,
                    0 otherwise.
            """
            if "Arduino" in port.description:
                return 2
            elif "A" in port.device:
                return 1
            else:
                return 0
        
        if isinstance(port, str):
            logger.info("Starting communication with Arduino...")
            self.arduino = serial.Serial(port=port, baudrate=baudrate, timeout=5)
        else:
            logger.info("Looking for Arduino...")
            serial_ports = [
                port
                for port in serial.tools.list_ports.comports()
                if "Arduino" in port.description or "ACM" in port.device
            ]
            if not serial_ports:
                raise IOError("No Arduino found.")
            serial_ports.sort(reverse=True, key=port_sort)
            arduino_ports = [port.device for port in serial_ports]
            if len(arduino_ports) > 1:
                logger.info(f"Multiple Arduinos found! Using the first: {arduino_ports[0]}")
            logger.info(f"Possible Arduino Found: {arduino_ports[0]}")
            logger.info("Attempting to connect...")
            self.arduino = serial.Serial(port=arduino_ports[0], baudrate=baudrate, timeout=5)

        time.sleep(5)
        self.arduino.flush()
        response = self.send_recieve("T","12345")
        if response["data"] == "12345":
            logger.info("Serial communication ready!")
        else:
            logger.info(f"ERROR: {response}")
   

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
        raw_data = self.arduino.read_until(bytes(self.EOM, 'utf-8')).decode("utf-8") 
        try:
            message_type = raw_data[0]
        except IndexError:
            return {
                "message_type": "ERROR",
                "data": "EMPTY",
                "error": 2,
            }
        if message_type in self.RECIEVE_MESSAGE_TYPES:
            data = raw_data.split("\n")[0].split("\r")[0][1:]
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
    
    def send_recieve(self, message_type, message_data):
        """Send data and expect a response.

        Parameters:
            message_type (str): the message type. Must be a type listed in the send
                message type list stored in the communications class.
            message_data (str): data to be send over the serial bus to the arduino.
        Returns:
            (dict): contains message type, processed data, and error value.
        """
        self.send(message_type, message_data)
        response = self.receive()
        if response["message_type"] != message_type:
            raise ValueError(f"Unexpected message type. Message: {response}")
        return response