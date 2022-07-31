from volcalenums.qualifiche import QualificaType
from utilities.writeExcel import write_excel

def getAllVolontariWithQualifica(dictVolontari, qualifica: QualificaType):
    for matr in dictVolontari:
        volontario = dictVolontari[matr]
        if volontario.hasQualifica(qualifica):
            volontarioDf = volontario.toDF()
            write_excel(volontarioDf, 'output_path', 'filename', 'title', 'sheet_name', True, True, False)


