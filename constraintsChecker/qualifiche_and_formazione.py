from volcalenums.formazione import FormazioneType
from volcalenums.qualifiche import QualificaType
from utilities.writeExcel import write_excel

def getAllVolontariWithFormazione(dictVolontari, formazione: FormazioneType):
    """Get all Volontari with given Formazione"""
    dictVolontariWithFormazione = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasFormazione(formazione):
            dictVolontariWithFormazione[matr] = volontario
    return dictVolontariWithFormazione

def getAllVolontariWithoutFormazione(dictVolontari, formazione: FormazioneType):
    """Get all Volontari without given Formazione"""
    dictVolontariWithFormazione = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if not volontario.hasFormazione(formazione):
            dictVolontariWithFormazione[matr] = volontario
    return dictVolontariWithFormazione

def getAllVolontariWithFormazione1AndFormazione2(dictVolontari, formazione1: FormazioneType, formazione2: FormazioneType):
    """Get all Volontari with both Formazione1 and Formazione2"""
    dictVolontariWithFormazione = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasFormazione(formazione1):
            if volontario.hasFormazione(formazione2):
                dictVolontariWithFormazione[matr] = volontario
    return dictVolontariWithFormazione

def getAllVolontariWithFormazione1WithoutFormazione2(dictVolontari, formazione1: FormazioneType, formazione2: FormazioneType):
    """Get all Volontari with Formazione1 but without Formazione2"""
    dictVolontariWithFormazione = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasFormazione(formazione1):
            if not volontario.hasFormazione(formazione2):
                dictVolontariWithFormazione[matr] = volontario
    return dictVolontariWithFormazione




def getAllVolontariWithQualifica(dictVolontari, qualifica: QualificaType):
    """Get all Volontari with given Qualifica"""
    dictVolontariWithQualifica = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasQualifica(qualifica):
            dictVolontariWithQualifica[matr] = volontario
    return dictVolontariWithQualifica

def getAllVolontariWithoutQualifica(dictVolontari, qualifica: QualificaType):
    """Get all Volontari without given Qualifica"""
    dictVolontariWithQualifica = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if not volontario.hasQualifica(qualifica):
            dictVolontariWithQualifica[matr] = volontario
    return dictVolontariWithQualifica

def getAllVolontariWithQualifica1AndQualifica2(dictVolontari, qualifica1: QualificaType, qualifica2: QualificaType):
    """Get all Volontari with both Qualifica1 and Qualifica2"""
    dictVolontariWithQualifica = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasQualifica(qualifica1):
            if volontario.hasQualifica(qualifica2):
                dictVolontariWithQualifica[matr] = volontario
    return dictVolontariWithQualifica

def getAllVolontariWithQualifica1WithoutQualifica2(dictVolontari, qualifica1: QualificaType, qualifica2: QualificaType):
    """Get all Volontari with Qualifica1 but without Qualifica2"""
    dictVolontariWithQualifica = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasQualifica(qualifica1):
            if not volontario.hasQualifica(qualifica2):
                dictVolontariWithQualifica[matr] = volontario
    return dictVolontariWithQualifica



def getAllVolontariWithQualifica1AndFormazione1(dictVolontari, qualifica1: QualificaType, formazione1: FormazioneType):
    """Get all Volontari with both Qualifica1 and Formazione2"""
    dictVolontariWithQualifica = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasQualifica(qualifica1):
            if volontario.hasFormazione(formazione1):
                dictVolontariWithQualifica[matr] = volontario
    return dictVolontariWithQualifica

def getAllVolontariWithQualifica1AndWithoutFormazione1(dictVolontari, qualifica1: QualificaType, formazione1: FormazioneType):
    """Get all Volontari with given Qualifica but without given Formazione"""
    dictVolontariWithQualifica = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasQualifica(qualifica1):
            if not volontario.hasFormazione(formazione1):
                dictVolontariWithQualifica[matr] = volontario
    return dictVolontariWithQualifica

def getAllVolontariWithoutQualifica1AndWithFormazione1(dictVolontari, qualifica1: QualificaType, formazione1: FormazioneType):
    """Get all Volontari without given Qualifica but with given Formazione"""
    dictVolontariWithQualifica = []
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if not volontario.hasQualifica(qualifica1):
            if volontario.hasFormazione(formazione1):
                dictVolontariWithQualifica[matr] = volontario
    return dictVolontariWithQualifica



