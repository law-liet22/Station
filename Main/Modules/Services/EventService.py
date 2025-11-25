from Config.logging import _logging
from Modules.Models.Station import *
from Modules.Models.Event import *

class EventService:
    def __init__(self, station: Station | None = None, seed:int|None=None, logger=_logging):
        self._station = station
        self._seed = seed
        self._logger = logger

    def generateEvents(self, station: Station, deltaTime: float, seed: int) -> list[Event]:
        pass

    def applyEvents(self, station: Station, events: list[Event]):
        pass

    @property
    def station(self) -> Station | None:
        return self._station

    @station.setter
    def station(self, value: Station | None):
        self._station = value

    @property
    def seed(self) -> int | None:
        return self._seed

    @seed.setter
    def seed(self, value: int | None):
        self._seed = value

    @property
    def logger(self):
        return self._logger

    @logger.setter
    def logger(self, value):
        self._logger = value