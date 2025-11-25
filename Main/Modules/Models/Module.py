import json
from Config.logging import logging
from Config.filePath import jsonPath

try:
    f = open(jsonPath, "rt")
    all = f.read()
    datas = json.loads(all)
    logging.info("Ouverture et lecture du fichier station.json.")
except FileNotFoundError as fnfe:
    logging.exception(f"Erreur lors de l'ouverture du fichier station.json : le fichier n'a pas été trouvé.")
    print("non")

class Module:
    def __init__(self, name:str, moduleType:str, functional:bool, wear:float, efficiency:float, energyConsumption:float, oxygenProduction:float, waterRecycling:float):
        self._name = name
        self._moduleType = moduleType
        self._functional = functional
        self._wear = wear
        self._efficiency = efficiency
        self._energyConsumption = energyConsumption
        self._oxygenProduction = oxygenProduction
        self._waterRecycling = waterRecycling

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def moduleType(self) -> str:
        return self._moduleType

    @moduleType.setter
    def moduleType(self, value: str):
        self._moduleType = value

    @property
    def functional(self) -> bool:
        return self._functional

    @functional.setter
    def functional(self, value: bool):
        self._functional = value

    @property
    def wear(self) -> float:
        return self._wear

    @wear.setter
    def wear(self, value: float):
        self._wear = value

    @property
    def efficiency(self) -> float:
        return self._efficiency

    @efficiency.setter
    def efficiency(self, value: float):
        self._efficiency = value

    @property
    def energyConsumption(self) -> float:
        return self._energyConsumption

    @energyConsumption.setter
    def energyConsumption(self, value: float):
        self._energyConsumption = value

    @property
    def oxygenProduction(self) -> float:
        return self._oxygenProduction

    @oxygenProduction.setter
    def oxygenProduction(self, value: float):
        self._oxygenProduction = value

    @property
    def waterRecycling(self) -> float:
        return self._waterRecycling

    @waterRecycling.setter
    def waterRecycling(self, value: float):
        self._waterRecycling = value

    def degrade(amount:float):
        pass

    def repair(repairPoint:float):
        pass
    
f.close()