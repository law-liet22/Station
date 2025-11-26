from Config.Logging import _logging
from Modules.Models.Station import *


class PersistenceService:
    def __init__(self, station: Station | None = None, savePath: str | None = None, logger=_logging):
        self._station = station
        self._savePath = savePath
        self._logger = logger

    def saveStation(self, station:Station):
        pass

    def loadStation(self, scenarioFile:str) -> Station:
        pass

    def exportLogCSV(self, station:Station, fileName:str):
        pass

    @property
    def station(self) -> Station | None:
        return self._station

    @station.setter
    def station(self, value: Station | None):
        self._station = value

    @property
    def savePath(self) -> str | None:
        return self._savePath

    @savePath.setter
    def savePath(self, value: str | None):
        self._savePath = value

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value