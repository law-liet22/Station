import json
from Modules import *
from Config.logging import _logging
from Modules.Utils.effacerTerminal import effacerTerminal

s1 = Station(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, [], [])
print(s1)

play = True

while play:
    try:
        print(
"""----------------------------
        Menu Principal
1. Démarrer la simulation
2. Charger une partie
3. Options
4. Quitter
----------------------------""")
    
        choice = input("Choisissez une option (1-4) : ")
        effacerTerminal()


    except KeyboardInterrupt as ki:
        _logging.info("Arrêt du programme par l'utilisateur.")
        play = False