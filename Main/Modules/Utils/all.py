import os
from pathlib import Path

def verifyFileAndCreateIfNotFound(path: str) -> str:
    p = Path(path)
    if p.exists():
        return path
    else:
        p = Path.touch(path)
        return p

def clearTerminal():
    """Efface le terminal en fonction du système d'exploitation."""
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour Linux et MacOS
        os.system('clear')