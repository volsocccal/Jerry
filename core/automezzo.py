from ..volcalenums import MezzoType

class Automezzo:
     def __init__(self, 
                    type: MezzoType, 
                    ID: str, 
                    targa: str):
        self.type = type
        self.ID = ID
        self.targa = targa
