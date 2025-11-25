import json, logging
from Modules.Models.Event import Event

logger = logging.basicConfig(format="\n%(levelname)s — %(asctime)s — %(name)s — %(message)s\n", 
                             filename="Trucs_random/Logs/app.log")
logger = logging.getLogger("App")

def operationFoireuse(valeur):
    if valeur < 0:
        raise ValueError("Valeur incorrecte : la valeur ne peut être négatif.")
    else:
        logging.info("Opération réussie")

try:
    val = int(input("Entrez une valeur : "))
    operationFoireuse(val)
except ValueError as ve:
    logging.exception(f"Exception : {str(ve)}")