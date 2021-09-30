import scanviz as sv
import logging
import logging.config
import os

logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scanviz/logging.conf')
logging.config.fileConfig(logger_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

scanner = sv.Scanner()
scanner.set_position(0, 0)