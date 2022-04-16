import datetime

from qualifica import Qualifica
from formazione import Formazione
from ..volcalenums import SquadraType
from ..utilities import computeAge
from ..utilities import computeYearsOfService

class Volontario:
    "This is a Volontario class"
    def __init__(self, 
                name: str, 
                surname: str, 
                ID: int,
                birthdate: datetime, 
                admissionDate: datetime, 
                squadra: SquadraType,
                qualifiche: list[Qualifica],
                formazione: list[Formazione]):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.birthDate = birthdate
        self.age = computeAge(self.birthdate)
        self.admissionDate = admissionDate
        self.yearsOfService = computeYearsOfService(self.admissionDate)
        self.squadra = squadra
        self.qualifiche = qualifiche
        self.formazione = formazione

    def toString(self, separator:str = '\n') -> str:
        return 'name:' + self.name + separator \
            + 'surname: ' + self.surname + separator \
                + 'ID: ' + self.ID + separator \
                    + 'birthdate: ' + str(self.birthDate) + separator \
                        + 'age: ' + str(self.age) + separator \
                            + 'admissionDate: ' + str(self.admissionDate) + separator \
                                + 'yearsOfService: ' + str(self.yearsOfService) + separator \
                                    + 'squadra: ' + str(self.squadra) + separator
    
    def printConsole(self):
        print(self.toString())


vol = Volontario('Francesco', 'Saporito')
vol.printConsole()