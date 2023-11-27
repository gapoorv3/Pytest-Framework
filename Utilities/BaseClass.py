import inspect
import logging

import pytest


@pytest.mark.usefixtures("setupLogin")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        # logging pyTest file with name
        logger = logging.getLogger(loggerName)

        # Filehandler use to handle all the log files to report on this specific file
        FileHandler = logging.FileHandler('logFile.log')
        # Filehandler object
        logger.addHandler(FileHandler)

        # Format
        Formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
        # linking this format with Filehandler to give to Logger.Filehandler
        FileHandler.setFormatter(Formatter)

        # setting level, from where it will print
        logger.setLevel(logging.DEBUG)

        return logger

