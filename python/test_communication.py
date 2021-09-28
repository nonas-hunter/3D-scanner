from scanviz.communication import Communication
import logging
import logging.config
import os

logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scanviz/logging.conf')
logging.config.fileConfig(logger_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    comms = Communication()
    print(comms.send_recieve("M", "1"))
    print(comms.send_recieve("M", "2"))
    print(comms.send_recieve("M", "3"))
    print(comms.send_recieve("S", "1"))
    print(comms.send_recieve("S", "2"))
    print(comms.send_recieve("S", "3"))
    print(comms.send_recieve("M", "1"))
    print(comms.send_recieve("S", "2"))
    print(comms.send_recieve("M", "3"))
