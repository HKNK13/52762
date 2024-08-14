import time 
import calendar
print("Hoşgeldiniz.\nLütfen havalimanları seçinizi yapınız. ")
havalimanlari={ 
    1:"Ankara Esenboğa Havalimanı",
    2:"İstanbul Sabiha Gökçen Havalimanı",
    3:"Van Ferit Melen Havalimanı",
    4:"Izmir Adnan Menderes Havalimanı",
    5:"Fraport Tav Antalya Havalimanı"}
time.sleep(1)
print("Havalimanları:")
for key,value in havalimanlari.items():
    print(f"{key}:{value}")
while True:
    try:
        kalkış_seçimi=int(input("Kalkış Havalimanı numarasını giriniz:"))
        kalkış_havalimanı=havalimanlari[kalkış_seçimi]
        print("Kalkış havalimanı :" ,kalkış_havalimanı)
        print("Şimdi varış havalimanını seçiniz")
        time.sleep(1)
        break
    except KeyError:
        print("Yanlış seçim yaptınız.Lütfen varış havalimaını tekrar seçiniz.")
del(havalimanlari[kalkış_seçimi])
for key,value in havalimanlari.items():
    print(f"{key}:{value}")  
while True:
    try:
        varış_seçimi=int(input("Varış Havalimanı numarasını giriniz:"))
        varış_havalimanı=havalimanlari[varış_seçimi]
        print("Varış  Havalimanı:",varış_havalimanı)
        break
    except KeyError:
        print("Yanlış seçim yaptınız.Lütfen tekrar varış havalimanını seçiniz.")
        time.sleep(1)
time.sleep(1)
print(f"{kalkış_havalimanı}-{varış_havalimanı} arası uçuşunuz için lütfen diğer işlemlere devam ediniz")
time.sleep(1)
print("Lütfen tarih seçiniz")
yıl=int(input("İşlem yapmak istediğiniz yılı seçiniz:"))
aylar={
        "ocak":1,"şubat":2,"mart":3,"nisan":4,"mayıs":5,"haziran":6,
        "temmuz":7,"ağustos":8,"eylül":9,"ekim":10,"kasım":11,"aralık":12# tarih hatası!!!
        }
ay=str(input("İşlem yapmak istediğiniz ayı yazınız:")).lower()
ayı=aylar[f"{ay}"]
b=calendar.TextCalendar(calendar.MONDAY)
c=b.formatmonth(yıl,ayı)
print(c)
gün=int(input("İşlem yapmak istediğiniz günü giriniz:")) 
if yıl%4==0 and ay=="şubat":
    if gün<=29:
        print(f"Tarih seçiminiz:{yıl}-{ayı}-{gün}")
    else:
        print("Tarih seçerken hata yaptınız.Lütfen başa döünüz.")
        exit()
elif yıl%4!=0 and ay=="şubat":
        if gün<=28:
            print(f"Tarih seçiminiz:{yıl}-{ayı}-{gün}")
        else:
            print("Tarih seçerken hata yaptınız.Lütfen başa döünüz.")
            exit()
elif (ay=="ocak" or ay=="mart" or ay=="mayıs" or ay=="temmuz" or
          ay=="ağustos" or ay=="kasım") :
        if gün<=31:
            print(f"Tarih seçiminiz:{yıl}-{ayı}-{gün}")
        else:
            print("Tarih seçerken hata yaptınız.Lütfen başa döünüz.")
            exit()
else: 
    if gün<=30:
        print(f"Tarih seçiminiz:{yıl}-{ayı}-{gün}")
    else:
        print("Tarih seçerken hata yaptınız.Lütfen başa döünüz.")
        exit()
time.sleep(1)
havalimanlari_listesi=["Ankara Esenboğa Havalimanı","İstanbul Sabiha Gökçen Havalimanı","Van Ferit Melen Havalimanı",
                            "Izmir Adnan Menderes Havalimanı","Fraport Tav Antalya Havalimanı"]

if kalkış_havalimanı==havalimanlari_listesi[0]:
    if varış_havalimanı==havalimanlari_listesi[1]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:               
            print("Yanlış seçim yaptınız.Başa dönünüz.")
    elif varış_havalimanı==havalimanlari_listesi[2]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[3]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[4]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
elif kalkış_havalimanı==havalimanlari_listesi[1]:
    if varış_havalimanı==havalimanlari_listesi[0]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:               
            print("Yanlış seçim yaptınız.Başa dönünüz.")
    elif varış_havalimanı==havalimanlari_listesi[2]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[3]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[4]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
elif kalkış_havalimanı==havalimanlari_listesi[2]:
    if varış_havalimanı==havalimanlari_listesi[1]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:               
            print("Yanlış seçim yaptınız.Başa dönünüz.")
    elif varış_havalimanı==havalimanlari_listesi[0]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[3]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[4]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
elif kalkış_havalimanı==havalimanlari_listesi[3]:
    if varış_havalimanı==havalimanlari_listesi[1]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:               
            print("Yanlış seçim yaptınız.Başa dönünüz.")
    elif varış_havalimanı==havalimanlari_listesi[0]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[2]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[4]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
elif kalkış_havalimanı==havalimanlari_listesi[4]:
    if varış_havalimanı==havalimanlari_listesi[1]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:               
            print("Yanlış seçim yaptınız.Başa dönünüz.")
    elif varış_havalimanı==havalimanlari_listesi[2]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[3]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
    elif varış_havalimanı==havalimanlari_listesi[0]:
        try:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş saatine uygun uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuşunuz:{gün}-{ay}-{yıl} saat {uçuş}")
        except KeyError:
            print("Yanlış seçim yaptınız.Başa dönünüz.") 
time.sleep(1)
class Sınıf:
    def __init__(self, bilet_türü=None, koltuk_sınıfı=None):
        self.bilet_türü = bilet_türü
        self.koltuk_sınıfı = koltuk_sınıfı

    def biletTürü(self):
        print("Bilet türleri:")
        bilet_türleri = {
            "Yetişkin": "Tam bilet",
            "Çocuk": "18 yaş altı çocuklar için %25 indirimli bilet"
        }
        for key, value in bilet_türleri.items():
            print(f"{key}: {value}")
        bilet_seç = str(input("Almak istediğiniz bilet türünü seçiniz: ")).capitalize()
        if bilet_seç in bilet_türleri:
            self.bilet_türü = bilet_seç
            print("Bilet türünüz: " + bilet_seç + " (" + bilet_türleri[bilet_seç] + ")")
        else:
            print("Geçersiz seçim. Lütfen doğru bir bilet türü seçiniz.")
    def koltukSınıfı(self):
        print("Sınıf türleri ve hakları:")
        sınıf_türleri = {
            "Ekonomi": "15 kg bagaj hakkı - 8 kg el bagajı hakkı - 500 mil puanı",
            "Prime": "25 kg bagaj hakkı - 8 kg el bagajı hakkı - 1000 mil puanı - ikram - bilet fiyatının 1.5 katı"
        }
        for key, value in sınıf_türleri.items():
            print(f"{key}: {value}")
        sınıf_seç = str(input("Almak istediğiniz bilet sınıfını seçiniz: ")).capitalize()
        if sınıf_seç in sınıf_türleri:
            self.koltuk_sınıfı = sınıf_seç
            print("Bilet sınıfınız: " + sınıf_seç)
        else:
            print("Geçersiz seçim. Lütfen doğru bir bilet sınıfı seçiniz.")
class Fiyat(Sınıf):
    def __init__(self, bilet_türü=None, koltuk_sınıfı=None, fiyat=2000):
        super().__init__(bilet_türü, koltuk_sınıfı)
        self.fiyat = fiyat

    def bilet_fiyat(self):
        if self.koltuk_sınıfı == "Ekonomi" and self.bilet_türü == "Yetişkin":
            print(f"Fiyat: {self.fiyat} TL")
        elif self.koltuk_sınıfı == "Ekonomi" and self.bilet_türü == "Çocuk":
            print(f"Fiyat: {self.fiyat * 0.75} TL")
        elif self.koltuk_sınıfı == "Prime" and self.bilet_türü == "Yetişkin":
            print(f"Fiyat: {self.fiyat * 1.5} TL")
        elif self.koltuk_sınıfı == "Prime" and self.bilet_türü == "Çocuk":
            print(f"Fiyat: {self.fiyat * 1.5 * 0.75} TL")
        else:
            print("Bilet türü veya koltuk sınıfı hatalı.")
bilet = Sınıf()
bilet.biletTürü()
bilet.koltukSınıfı()
bilet_fiyatı = Fiyat(bilet.bilet_türü, bilet.koltuk_sınıfı)
bilet_fiyatı.bilet_fiyat()
 








     



            


            


           


