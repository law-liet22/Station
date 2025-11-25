import logging as _logging

# configure the standard logging module
_logging.basicConfig(
    format="\n%(levelname)s — %(asctime)s — %(name)s — %(message)s\n",
    filename="Trucs_random/Logs/app.log",
)

# create the application logger
logger = _logging.getLogger("App")

# expose the logger object under the name `logging` so importing
# `from Config.logging import logging` returns a usable logger instance
logging = logger

__all__ = ["logging", "logger"]