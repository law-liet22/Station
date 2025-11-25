import json
from Modules.Models.Event import *
from Modules.Models.Crew import *
from Modules.Models.Module import *
from Modules.Models.Experiment import *
from Modules.Models.Station import *
from Config.logging import logging

def operationFoireuse(valeur):
    if valeur < 0:
        raise ValueError("Valeur incorrecte : le nombre ne peut être négatif.")
    
    else:
        logging.info("Opération réussie")

try:
    val = input("Entrez une valeur : ")

    if val.isdigit() == False:
        raise ValueError("Valeur incorrecte : seuls les chiffres sont acceptés.")
    
    valeur = int(val)
    operationFoireuse(val)

except ValueError as ve:
    logging.exception(f"Exception : {str(ve)}")