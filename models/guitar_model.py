# This is subject to change, basic layout will suffice for the time being
class Guitar:
    def __init__(self):
        self.year : int
        self.brand : str
        self.model : str
        self.num_frets : int
        self.ss_frets : bool
        self.wood : {
            "body" : str,
            "neck" : str,
            "fretboard" : str
        }
        self.locking_tuners : bool
