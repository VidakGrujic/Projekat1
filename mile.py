class Mile:
    def __init__(self, ime, plata):
        self.ime = ime
        self.plata = plata

    def __str__(self):
        return f"{self.ime} {self.plata}"

    def uvecaj_platu(self, iznos):
        self.plata += iznos

    def smanji_platu(self, iznos):
        self.plata -= iznos




mile = Mile("Mile", 20000)
print(mile)
mile.uvecaj_platu(20000)
print(mile)
mile.smanji_platu(10000)
print(mile)

