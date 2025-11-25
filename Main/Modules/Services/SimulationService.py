from Config.logging import _logging
from Modules.Models.Station import *

class SimulationService:
    def __init__(self, station: Station | None = None, running:bool=False, logger=_logging):
        self._station = station
        self._running = running
        self._logger = logger

    def runStep(self, station:Station, deltaTime:float):
        pass

    @property
    def station(self) -> Station | None:
        return self._station

    @station.setter
    def station(self, value: Station | None):
        self._station = value

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value: bool):
        self._running = value

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value