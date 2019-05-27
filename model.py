from random import choice

STEVILO_DOVOLJENIH_NAPAK = 10 
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'S'

class Igra:

    def __init__(self, beseda, crke = None):
        self.geslo = beseda
        if crke == None:
            self.crke = []
        else:
            self.crke = crke
    
    def napacne_crke(self):
        napacne_crke = []
        for crka in self.crke:
            if crka not in self.geslo:
                napacne_crke.append(crka)
        return napacne_crke

    def pravilne_crke(self):
        pravilne_crke = []
        for crka in self.crke:
            if crka in self.geslo:
                pravilne_crke.append(crka)
        return pravilne_crke

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.pravilne_crke():
                return False
        return True

    def poraz(self):
        if self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False

    def pravilni_del_gesla(self):
        pravilni_del = self.geslo
        for crka in self.geslo:
            if crka not in self.pravilne_crke():
                pravilni_del = pravilni_del.replace(crka, "_")
        return pravilni_del

    def nepravilni_ugibi(self):
        nepravilni_ugibi = ""
        for crka in self.napacne_crke():
            nepravilni_ugibi += " " + crka
        return nepravilni_ugibi

    def ugibaj(self, crka):
        velika_crka = crka.upper()
        if velika_crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke.append(velika_crka)
        if velika_crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        elif velika_crka not in self.geslo:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
            

with open("besede.txt", "r", encoding = "utf-8") as besede:
    bazen_besed = []
    for vrstica in besede:
        bazen_besed.append(vrstica.upper().strip())

def nova_igra():
    return Igra(choice(bazen_besed))

class Vislice:
    def __init__(self):
        self.igre = {}
    
    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def nova_igra(self):
        igra = nova_igra()
        id_igre = self.prost_id_igre()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre
    
    def ugibaj(self, id_igre, crka):
        igra = self.igre[id_igre][0]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)