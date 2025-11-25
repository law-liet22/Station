import json
from Config.logging import logging
from Config.filePath import jsonPath

try:
    f = open(jsonPath, "rt")
    all = f.read()
    datas = json.loads(all)
    logging.info("Ouverture et lecture du fichier station.json.")

    class Experiment:
        def __init__(self, name:str, energyRequired:float, oxygenRequired:float, duration:float, successProbability:float, sciencePoints:int, completed:bool=False):
            self._name = name
            self._energyRequired = energyRequired
            self._oxygenRequired = oxygenRequired
            self._duration = duration
            self._successProbability = successProbability
            self._sciencePoints = sciencePoints
            self._completed = completed

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, value: str):
            self._name = value

        @property
        def energyRequired(self) -> float:
            return self._energyRequired

        @energyRequired.setter
        def energyRequired(self, value:float):
            self._energyRequired = value

        @property
        def oxygenRequired(self) -> float:
            return self._oxygenRequired

        @oxygenRequired.setter
        def oxygenRequired(self, value: float):
            self._oxygenRequired = value

        @property
        def duration(self) -> float:
            return self._duration

        @duration.setter
        def duration(self, value: float):
            self._duration = value

        @property
        def successProbability(self) -> float:
            return self._successProbability

        @successProbability.setter
        def successProbability(self, value: float):
            self._successProbability = value

        @property
        def sciencePoints(self) -> int:
            return self._sciencePoints

        @sciencePoints.setter
        def sciencePoints(self, value: int):
            self._sciencePoints = value

        @property
        def completed(self) -> bool:
            return self._completed

        @completed.setter
        def completed(self, value: bool):
            self._completed = value

        def start():
            pass

        def progress():
            pass

        def isCompleted():
            pass

    f.close()

except FileNotFoundError as fnfe:
    logging.exception(f"Erreur lors de l'ouverture du fichier station.json : le fichier n'a pas été trouvé.")