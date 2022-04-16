import datetime

from ..volcalenums import FormazioneType

class Formazione:
     def __init__(self, 
                    type: FormazioneType, 
                    startDate: datetime, 
                    endDate: datetime = (2099, 12, 31)):
        if (startDate > endDate):
            raise Exception("Received formazione has startDate after endDate")
        self.type = type
        self.startDate = startDate
        self.endDate = endDate
        self.isActive = endDate > datetime.datetime.today()
