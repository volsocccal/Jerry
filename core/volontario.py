import datetime

from core.qualifica import Qualifica
from core.formazione import Formazione
from volcalenums.squadre import SquadraType
from utilities.dateHandler import computeAge
from utilities.dateHandler import computeYearsOfService

class Volontario:
    "This is a Volontario class"
    def __init__(self, 
                name: str, 
                surname: str,
                CF: str, 
                ID: int,
                birthdate: datetime, 
                squadra: SquadraType,
                qualifiche: list[Qualifica],
                formazione: list[Formazione]):
        self.name = name
        self.surname = surname
        self.CF = CF
        self.ID = ID
        self.birthDate = birthdate
        self.age = computeAge(self.birthDate)
        self.squadra = squadra
        self.qualifiche = qualifiche
        self.formazione = formazione

    def toString(self, separator:str = '\n') -> str:
        return 'name:' + self.name + separator \
            + 'surname: ' + self.surname + separator \
                + 'CF: ' + self.CF + separator \
                    + 'ID: ' + self.ID + separator \
                        + 'birthdate: ' + str(self.birthDate) + separator \
                            + 'age: ' + str(self.age) + separator \
                                + 'squadra: ' + str(self.squadra) + separator

    def toCSV(self) -> str:
        return self.toString(';')
    
    def printConsole(self):
        print(self.toString())