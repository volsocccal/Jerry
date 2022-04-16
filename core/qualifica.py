import datetime

from ..volcalenums import QualificaType

class Qualifica:
     def __init__(self, 
                    type: QualificaType, 
                    startDate: datetime, 
                    endDate: datetime = (2099, 12, 31)):
        if (startDate > endDate):
            raise Exception("Received qualifica has startDate after endDate")
        self.type = type
        self.startDate = startDate
        self.endDate = endDate
        self.isActive = endDate > datetime.datetime.today()
