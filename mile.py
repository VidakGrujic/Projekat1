class Mile:
    def __init__(self, ime):
        self.ime = ime


    def __str__(self):
        return f"{self.ime}"



mile = Mile("Mile")
print(mile)

