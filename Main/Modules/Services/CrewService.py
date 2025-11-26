from Config.Logging import _logging
from Modules.Models.Crew import *
from Modules.Models.Module import *
from Modules.Models.Station import Station

class CrewService:
    def __init__(self, station: Station | None = None, logger=_logging):
        self._station = station
        self._logger = logger
    
    def updateCrewStatus(self, crew:Crew, deltaTime:float):
        pass
    def performTask(self, crew:Crew, task:str, module:Module):
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