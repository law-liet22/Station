import os

def clearTerminal():
    """Efface le terminal en fonction du système d'exploitation."""
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour Linux et MacOS
        os.system('clear')