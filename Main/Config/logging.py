import logging 
# configure the standard logging module
logging.basicConfig(
    format="\n%(levelname)s — %(asctime)s — %(name)s — %(message)s\n",
    filename="Main/Logs/app.log",
)

# create the application logger
logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)

# expose the logger object under the name `logging` so importing
# `from Config.logging import logging` returns a usable logger instance
_logging = logger

__all__ = ["logging", "logger"]