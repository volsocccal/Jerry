import datetime
import pandas as pd
from regex import D

from core.qualifica import Qualifica
from core.formazione import Formazione
from volcalenums import FormazioneType
from volcalenums.qualifiche import QualificaType
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
        self._age = computeAge(self.birthDate)
        self._squadra = squadra
        self._qualifiche = qualifiche
        self._formazione = formazione

    def hasQualifica(self, qualifica: QualificaType, allowForExpiredQualifica: bool = False) -> bool:
        for q in self._qualifiche:
            if q.type == qualifica:
                if allowForExpiredQualifica:
                    return True
                else: 
                    if q.isActive:
                        return True
        return False

    def hasFormazione(self, formazione: FormazioneType) -> bool:
        for f in self._formazione:
            if f.type == formazione:
                return True
        return False

    def toDictionary(self, printFullAnagraphic: bool = False, printQualifiche: bool = False, printFormazione: bool = False):
        volontarioDict = vars(self)
        if not printFullAnagraphic:
            del volontarioDict['birthDate']
            del volontarioDict['age']
            del volontarioDict['CF']
        if not printQualifiche:
            del volontarioDict['qualifiche']
        if not printFormazione:
            del volontarioDict['formazione']
        return volontarioDict 

    def toString(self, 
                    separator:str = '\n', 
                    printIntestation: bool = True, 
                    printFullAnagraphic: bool = False, 
                    printQualifiche: bool = False, 
                    printFormazione: bool = False) -> str:
        volontarioStr = ''
        volontarioDict = self.toDictionary(printFullAnagraphic, printQualifiche, printFormazione)
        for key in volontarioDict:
            if printIntestation:
                volontarioStr += key
            volontarioStr += volontarioDict[key] +  + separator

    def toCSV(self,
                printIntestation: bool = True, 
                printFullAnagraphic: bool = False, 
                printQualifiche: bool = False, 
                printFormazione: bool = False) -> str:
        return self.toString(';', printIntestation, printFullAnagraphic, printQualifiche, printFormazione)

    def toDF(self,
                getFullAnagraphic: bool = False, 
                getQualifiche: bool = False, 
                getFormazione: bool = False):
        volontarioDict = self.toDictionary(getFullAnagraphic, getQualifiche, getFormazione)
        return pd.DataFrame([volontarioDict])
    
    def printConsole(self):
        print(self.toString('\n', True, True, True, True))
