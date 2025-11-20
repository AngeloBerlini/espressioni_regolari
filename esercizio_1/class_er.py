import re # Importa il modulo delle espressioni regolari

class EsprReg:# Definizione della classe EsprReg
    def __init__(self):
        self.pattern = ""

    def set_pattern(self, pattern: str):#Definizione del metodo set_pattern
        
        self.pattern = pattern

    def validate(self, string: str) -> str:# Definizione del metodo validate
        if re.match(self.pattern, string):# Controlla se la stringa corrisponde al pattern
            return "match"
        else:
            return "mismatch"


    