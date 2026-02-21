from datetime import datetime

class Kimlik:
    def __init__(self, tc_no, isim, soyisim, dogum_tarihi):
        self.tc_no = tc_no
        self.isim = isim
        self.soyisim = soyisim
        self.dogum_tarihi = dogum_tarihi

class Personel(Kimlik):
    def __init__(self, tc_no, isim, soyisim, dogum_tarihi, departman, giris_tarihi, maas):
        super().__init__(tc_no, isim, soyisim, dogum_tarihi)
        self.__departman = departman
        self.__giris_tarihi = giris_tarihi
        self.__maas = maas

    def get_departman(self):
        return self.__departman
    
    def set_departman(self, departman):
        self.__departman = departman

    def get_giris_tarihi(self):
        return self.__giris_tarihi
    
    def set_giris_tarihi(self, giris_tarihi):
        self.__giris_tarihi = giris_tarihi

    def get_maas(self):
        return self.__maas
    
    def set_maas(self, maas):
        self.__maas = maas

    def __str__(self):
        return f"İsim: {self.isim} {self.soyisim}, Departmanı: {self.__departman}, Giriş Tarihi: {self.__giris_tarihi}, Maaşı: {self.__maas}"

    def id_olustur(self):
        # İşe giriş tarihinin gün ve ay bilgisini al
        gun_ay = self.__giris_tarihi.strftime("%d%m")
        # İsimden ilk iki karakteri al ve büyük harfe dönüştür
        isim_kisaltma = self.isim[:2].upper()
        # Departmandan son iki karakteri al ve büyük harfe dönüştür
        departman_kisaltma = self.__departman[-2:].upper()
        # Kimlik numarasını oluştur ve döndür
        return f"{isim_kisaltma}{departman_kisaltma}{gun_ay}"

def main():
    personel_listesi = []
    departman_maaslari = {}
    
    while True:
        tc_no = input("TC Kimlik No (çıkmak için 'H' girin): ")
        if tc_no.upper() == "H":
            break
        
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        dogum_tarihi_str = input("Doğum Tarihi (GG.AA.YYYY): ")
        dogum_tarihi = datetime.strptime(dogum_tarihi_str, "%d.%m.%Y")
        departman = input("Departman: ")
        giris_tarihi_str = input("İşe Giriş Tarihi (GG.AA.YYYY): ")
        giris_tarihi = datetime.strptime(giris_tarihi_str, "%d.%m.%Y")
        maas = float(input("Maaş: "))

        personel = Personel(tc_no, isim, soyisim, dogum_tarihi, departman, giris_tarihi, maas)
        personel_listesi.append(personel)

        personel_id = personel.id_olustur()
        if departman not in departman_maaslari:
            departman_maaslari[departman] = {"toplam_maas": maas, "personel_sayisi": 1, "en_yuksek_maas": maas, "en_dusuk_maas": maas}
        else:
            departman_maaslari[departman]["toplam_maas"] += maas
            departman_maaslari[departman]["personel_sayisi"] += 1
            if maas > departman_maaslari[departman]["en_yuksek_maas"]:
                departman_maaslari[departman]["en_yuksek_maas"] = maas
            if maas < departman_maaslari[departman]["en_dusuk_maas"]:
                departman_maaslari[departman]["en_dusuk_maas"] = maas

    toplam_maas = sum([personel.get_maas() for personel in personel_listesi])
    ortalama_maas = toplam_maas / len(personel_listesi)

    print("\nDepartman İstatistikleri:")
    for departman, istatistikler in departman_maaslari.items():
        print(f"\n{departman} Departmanı İstatistikleri:")
        print(f"Toplam Maaş: {istatistikler['toplam_maas']}")
        print(f"Personel Sayısı: {istatistikler['personel_sayisi']}")
        print(f"En Yüksek Maaş: {istatistikler['en_yuksek_maas']}")
        print(f"En Düşük Maaş: {istatistikler['en_dusuk_maas']}")

    print("\nŞirket İstatistikleri:")
    print(f"Toplam Maaş: {toplam_maas}")
    print(f"Ortalama Maaş: {ortalama_maas}")

if __name__ == "__main__":
    main()
