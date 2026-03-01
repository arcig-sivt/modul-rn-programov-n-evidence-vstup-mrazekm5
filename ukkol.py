from datetime import datetime


studenti: dict[str,str] = {"123": "Jan Novak", "456": "Petr Svoboda", "789": "Eva Kralova"}

ve_skole: list[str] = []

log: dict[str, list[tuple[datetime, str]]] = {}

def cipnuti(ID: str)-> None:
    if ID in studenti:
        if ID not in ve_skole:
            ve_skole.append(ID)
            print(f"{studenti[ID]} prisel.")
            if ID not in log:
                log[ID] = []
            log[ID].append((datetime.now(), "prisel"))
        else:
            ve_skole.remove(ID)
            print(f"{studenti[ID]} odesel.")
            log[ID].append((datetime.now(), "odesel"))
    else:
        print("Neznámé ID.")
