import json, time
from Modules import *
from Config.logging import _logging
# from Modules.Utils.clearTerminal import clearTerminal

exitKey = '0'
paramsKey = '3'

def __main__():
    play = True

    while play:
        try:
            _logging.info("Programme lancé.")
            print(f"""
    ----------------------------
            Menu Principal
    1. Démarrer la simulation
    2. Charger une partie
    {paramsKey}. Options
    {exitKey}. Quitter
    ----------------------------""")

            choice = input("Choisissez une option (1-4) : ")
            clearTerminal()

            if choice == '1':
                clearTerminal()
                print("Démarrage de la simulation", end="")
                for i in range(3):
                    print(".", end="", flush=True)
                    time.sleep(1)
                clearTerminal()
                return

            elif choice == '2':
                clearTerminal()
                pass

            elif choice == paramsKey:
                clearTerminal()
                pass

            elif choice == exitKey:
                print("Fermeture du programme", end="")
                for i in range(3):
                    print(".", end="", flush=True)
                    time.sleep(1)
                clearTerminal()
                play = False
                _logging.info("Programme arrêté par l'utilisateur.")
                return
        except KeyboardInterrupt as ki:
            _logging.info("Arrêt forcé du programme par l'utilisateur.")
            play = False
            return

if __name__ == "__main__":
    __main__()