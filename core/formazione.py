import datetime

from volcalenums import FormazioneType

class Formazione:
     def __init__(self, 
                    type: FormazioneType, 
                    startDate: datetime, 
                    annotazioni: str = ''):
        self.type = type
        self.startDate = startDate
        self.annotazioni = annotazioni
