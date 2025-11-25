import json
from Modules import *
from Config.logging import _logging
# from Modules.Utils.clearTerminal import clearTerminal

play = True

o1 = RessourcesService()

while play:
    try:
        _logging.info("Programme lancé.")
        print(
"""----------------------------
        Menu Principal
1. Démarrer la simulation
2. Charger une partie
3. Options
4. Quitter
----------------------------""")
    
        choice = input("Choisissez une option (1-4) : ")
        clearTerminal()


    except KeyboardInterrupt as ki:
        _logging.info("Arrêt forcé du programme par l'utilisateur.")
        play = False