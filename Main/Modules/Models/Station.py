import json
from Config.Logging import logging
from Config.filePath import jsonPath
from Modules.Models.Crew import *
from Modules.Models.Module import *

try:
    f = open(jsonPath, "rt")
    all = f.read()
    datas = json.loads(all)
    logging.info("Ouverture et lecture du fichier station.json.")

    class Station:
        def __init__(self, velocity:float=datas["initialVelocity"], 
                     fuel:float=        datas["initialFuel"],
                     energy:float=      datas["initialEnergy"], 
                     maxEnergy:float=   datas["maxEnergy"], 
                     oxygen:float=      datas["initialOxygen"], 
                     maxOxygen:float=   datas["maxOxygen"],
                     water:float=       datas["initialWater"], 
                     maxWater:float=    datas["maxWater"], 
                     temperature:float= datas["initialTemperature"], 
                     modules:list[Module]=[], crew:list[Crew]=[], 
                     alertLevel:int=    datas["initialAlertLevel"], 
                     integrity:float=   datas["initialIntegrity"], 
                     maxFuel:float=     datas["maxFuel"], 
                     name:str=          datas["name"], 
                     altitude:float=    datas["initialAltitude"]):

            try:
                if velocity<0 or velocity<6.8 or velocity>8.2:
                    raise ValueError(f"La vélocité ne peut pas être négative, inférieure à 6.8km/s ou supérieure à 8.2km/s. Valeur entrée : '{velocity}'")
                
                elif altitude<300 or altitude>900:
                    raise ValueError(f"L'altitude doit être comprise entre 300 et 900km.")
                
                elif maxFuel<fuel:
                    raise ValueError(f"Il ne peut pas y avoir plus de carburant que la capacité maximale.")
                
                self._velocity = velocity
                self._fuel = fuel
                self._energy = energy
                self._maxEnergy = maxEnergy
                self._oxygen = oxygen
                self._maxOxygen = maxOxygen
                self._water = water
                self._maxWater = maxWater
                self._temperature = temperature
                self._alertLevel = alertLevel
                self._integrity = integrity
                self._maxFuel = maxFuel
                self._name = name
                self._altitude = altitude
                self._modules = modules
                self._crew = crew

            except ValueError as ve:
                logging.error(f"Valeur incorrecte lors de l'initialisation de la station : {str(ve)}")

            except Exception as e:
                logging.error(f"Erreur lors de l'initialisation de la station : {str(e)}")

        @property
        def velocity(self) -> float:
            return self._velocity

        @velocity.setter
        def velocity(self, value: float):
            self._velocity = value

        @property
        def fuel(self) -> float:
            return self._fuel

        @fuel.setter
        def fuel(self, value: float):
            self._fuel = value

        @property
        def energy(self) -> float:
            return self._energy

        @energy.setter
        def energy(self, value: float):
            self._energy = value

        @property
        def maxEnergy(self) -> float:
            return self._maxEnergy

        @maxEnergy.setter
        def maxEnergy(self, value: float):
            self._maxEnergy = value

        @property
        def oxygen(self) -> float:
            return self._oxygen

        @oxygen.setter
        def oxygen(self, value: float):
            self._oxygen = value

        @property
        def maxOxygen(self) -> float:
            return self._maxOxygen

        @maxOxygen.setter
        def maxOxygen(self, value: float):
            self._maxOxygen = value

        @property
        def water(self) -> float:
            return self._water

        @water.setter
        def water(self, value: float):
            self._water = value

        @property
        def maxWater(self) -> float:
            return self._maxWater

        @maxWater.setter
        def maxWater(self, value: float):
            self._maxWater = value

        @property
        def temperature(self) -> float:
            return self._temperature

        @temperature.setter
        def temperature(self, value: float):
            self._temperature = value

        @property
        def alertLevel(self) -> int:
            return self._alertLevel

        @alertLevel.setter
        def alertLevel(self, value: int):
            self._alertLevel = value

        @property
        def integrity(self) -> float:
            return self._integrity

        @integrity.setter
        def integrity(self, value: float):
            self._integrity = value

        @property
        def maxFuel(self) -> float:
            return self._maxFuel

        @maxFuel.setter
        def maxFuel(self, value: float):
            self._maxFuel = value

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, value: str):
            self._name = value

        @property
        def altitude(self) -> float:
            return self._altitude

        @altitude.setter
        def altitude(self, value: float):
            self._altitude = value

        @property
        def modules(self) -> list:
            return self._modules

        @modules.setter
        def modules(self, value: list):
            self._modules = value

        @property
        def crew(self) -> list:
            return self._crew

        @crew.setter
        def crew(self, value: list):
            self._crew = value

    def setRessources():
        pass

    def setTemperature(temp: float):
        pass

    def setIntegrity(integrity:float):
        pass

    f.close()

except FileNotFoundError as fnfe:
    logging.exception(f"Erreur lors de l'ouverture du fichier station.json : le fichier n'a pas été trouvé.")
