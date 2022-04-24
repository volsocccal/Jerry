import datetime

from volcalenums import QualificaType

class Qualifica:
     def __init__(self, 
                    type: QualificaType, 
                    startDate: datetime.date, 
                    endDate: datetime.date = datetime.date(2099, 12, 31),
                    annotazioni: str = ''):
        if str( endDate ) == 'NaT':
            endDate = datetime.date(2099, 12, 31)
        if isinstance(startDate, datetime.datetime):
            startDate = startDate.date()
        if isinstance(endDate, datetime.datetime):
            startDate = endDate.date()
        if (startDate > endDate):
            raise Exception("Received qualifica has startDate after endDate")
        self.type = type
        self.startDate = startDate
        self.endDate = endDate
        self.annotazioni = annotazioni
        self.isActive = endDate > datetime.datetime.today().date()
