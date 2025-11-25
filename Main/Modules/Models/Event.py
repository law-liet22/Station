import json
from Config.logging import logging

try:
    f = open("Trucs_random/Config/station.json", "rt")
    all = f.read()
    datas = json.loads(all)
    logging.info("Ouverture et lecture du fichier station.json.")
except FileNotFoundError as fnfe:
    logging.exception(f"Erreur lors de l'ouverture du fichier station.json : le fichier n'a pas été trouvé.")

class Event:
    def __init__(self, name:str, type:str, probability:float, targerModule:str, impactMagnitude:float):
        # store internal attributes as private
        self._name = name
        self._type = type
        self._probability = probability
        self._targetModule = targerModule
        self._impactMagnitude = impactMagnitude

    # properties to keep external API the same while backing with private attributes
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def probability(self) -> float:
        return self._probability

    @probability.setter
    def probability(self, value: float):
        self._probability = value

    @property
    def targetModule(self) -> str:
        return self._targetModule

    @targetModule.setter
    def targetModule(self, value: str):
        self._targetModule = value

    @property
    def impactMagnitude(self) -> float:
        return self._impactMagnitude

    @impactMagnitude.setter
    def impactMagnitude(self, value: float):
        self._impactMagnitude = value