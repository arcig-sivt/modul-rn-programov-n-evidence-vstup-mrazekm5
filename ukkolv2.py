from dataclasses import dataclass
from datetime import datetime

type ID_karty = str


@dataclass
class Student:
    ID: ID_karty
    jmeno: str
    
@dataclass
class LogEntry:
    cas: datetime
    akce: str

class Skola:
    studenti: dict[ID_karty, Student]
    ve_skole: list[ID_karty]
    log: dict[ID_karty, list[LogEntry]]

    def cipnuti(self, ID: ID_karty) -> None:
        if ID in self.studenti:

            if ID not in self.ve_skole:
                self.ve_skole.append(ID)
                print(f"{self.studenti[ID].jmeno} prisel.")
            
                if ID not in self.log:
                    self.log[ID] = []
                self.log[ID].append(LogEntry(datetime.now(), "prisel"))

            else:
                self.ve_skole.remove(ID)
                print(f"{self.studenti[ID].jmeno} odesel.")
                self.log[ID].append(LogEntry(datetime.now(), "odesel"))
                
        else:
            print("Neznámé ID.")


