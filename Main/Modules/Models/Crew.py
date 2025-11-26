import json

from Config.logging import logging
from Modules.Models.Module import *
from Modules.Models.Experiment import *
from Config.filePath import jsonPath

try:
    f = open(jsonPath, "rt")
    all = f.read()
    datas = json.loads(all)
    logging.info("Ouverture et lecture du fichier station.json.")

    class Crew:
        def __init__(self, stress:float, fatigue:float, morale:float, technicalSkill:float, scienceSkill:float, medicalSkill:float, health:int):
            # private attributes
            self._stress = stress
            self._fatigue = fatigue
            self._morale = morale
            self._technicalSkill = technicalSkill
            self._medicalSkill = medicalSkill
            self._scienceSkill = scienceSkill
            self._health = health

        # properties for public API
        @property
        def stress(self) -> float:
            return self._stress

        @stress.setter
        def stress(self, value: float):
            self._stress = value

        @property
        def fatigue(self) -> float:
            return self._fatigue

        @fatigue.setter
        def fatigue(self, value: float):
            self._fatigue = value

        @property
        def morale(self) -> float:
            return self._morale

        @morale.setter
        def morale(self, value: float):
            self._morale = value

        @property
        def technicalSkill(self) -> float:
            return self._technicalSkill

        @technicalSkill.setter
        def technicalSkill(self, value: float):
            self._technicalSkill = value

        @property
        def medicalSkill(self) -> float:
            return self._medicalSkill

        @medicalSkill.setter
        def medicalSkill(self, value: float):
            self._medicalSkill = value

        @property
        def scienceSkill(self) -> float:
            return self._scienceSkill

        @scienceSkill.setter
        def scienceSkill(self, value: float):
            self._scienceSkill = value

        @property
        def health(self) -> int:
            return self._health

        @health.setter
        def health(self, value: int):
            self._health = value
        
        def rest(hours:float):
            pass

        def performRepair(module:Module):
            pass

        def performResearch(exp: Experiment):
            pass

    f.close()

except FileNotFoundError as fnfe:
    logging.exception(f"Erreur lors de l'ouverture du fichier station.json : le fichier n'a pas été trouvé.")