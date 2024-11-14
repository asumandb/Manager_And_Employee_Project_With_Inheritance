class Calisan:
    def __init__(self, isim, departman, maas):
        self.isim = isim
        self.departman = departman
        self.maas = maas

    def bilgileri_goster(self):
        print(f"Çalışan: {self.isim}, Departman: {self.departman}, Maaş: {self.maas} TL")

class Yonetici(Calisan):
    def __init__(self, isim, departman, maas, bonus):
        super().__init__(isim, departman, maas)
        self.bonus = bonus

    def toplam_maas_hesapla(self):
        return self.maas + self.bonus

    def bilgileri_goster(self):
        print(f"Yönetici: {self.isim}, Departman: {self.departman}, Maaş:{self.maas} TL, Bonus:{self.bonus} TL ")
        print(f"Toplam Maaş: {self.toplam_maas_hesapla()} TL")


calisan1 = Calisan("Ayşe", "Pazarlama", 5000)
yonetici1 = Yonetici("Mehmet", "Satış", 8000, 2000)

calisan1.bilgileri_goster()
yonetici1.bilgileri_goster()
