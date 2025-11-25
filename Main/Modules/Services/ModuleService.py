from Config.logging import _logging
from Modules.Models.Station import *

class ModuleService:
    def __init__(self, station: Station | None = None, logger=_logging):
        self._station = station
        self._logger = logger

    def degradeModule(self, station:Station, deltaTime:float):
        pass

    def repairModule(self, station:Station, deltaTime:float):
        pass

    @property
    def station(self) -> Station | None:
        return self._station

    @station.setter
    def station(self, value: Station | None):
        self._station = value

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value