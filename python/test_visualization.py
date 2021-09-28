from scanviz.visualization import Visualization
import logging
import logging.config
import os

logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scanviz/logging.conf')
logging.config.fileConfig(logger_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

viz = Visualization()
viz.create_viz()