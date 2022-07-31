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
        self._name = name
        self._surname = surname
        self._CF = CF
        self._ID = ID
        self._birthDate = birthdate
        self._age = computeAge(self._birthDate)
        self._squadra = squadra
        self._qualifiche = qualifiche
        self._formazione = formazione

    def toString(self, separator:str = '\n') -> str:
        return 'name:' + self._name + separator \
            + 'surname: ' + self._surname + separator \
                + 'CF: ' + self._CF + separator \
                    + 'ID: ' + self._ID + separator \
                        + 'birthdate: ' + str(self._birthDate) + separator \
                            + 'age: ' + str(self._age) + separator \
                                + 'squadra: ' + str(self._squadra) + separator

    def toCSV(self) -> str:
        return self.toString(';')
    
    def printConsole(self):
        print(self.toString())

    def hasQualifica(self, q: Qualifica) -> bool:
        return q in self._qualifiche

    def hasFormazione(self, f: Formazione) -> bool:
        return f in self._formazione
