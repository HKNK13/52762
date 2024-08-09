import time 
import calendar
#print("Tek yön\n""Gidiş-Dönüş")
#yön_seçim=input("Yön seçiminizi yapınız(Tek yön için 1'e basınız.Gidiş-Dönüş için ise 2'e basınız2):")
havalimanlari={ 
    1:"Ankara Esenboğa Havalimanı ",
    2:"İstanbul Sabiha Gökçen Havalimanı",
    3:"Van Ferit Melen Havalimanı",
    4:"Izmir Adnan Menderes Havalimanı ",
    5:"Fraport Tav Antalya Havalimanı "}
for key,value in havalimanlari.items():
    print(f"{key}:{value}")
try:
    kalkış_seçimi=int(input("Kalkış Havalimanı numarasını giriniz:"))
    kalkış_havalimanı=havalimanlari[kalkış_seçimi]
    print("Kalkış havalimanı :" ,kalkış_havalimanı)
except KeyError:
    print("Yanlış seçim yaptınız.Yalnızca [1,2,3,4,5] rakamlarından birini seçebilirsiniz.\n"
          "Tekrar deneyiniz")
    exit()
del(havalimanlari[kalkış_seçimi])
for key,value in havalimanlari.items():
    print(f"{key}:{value}")  
try:
    varış_seçimi=int(input("Varış Havalimanı numarasını giriniz:"))
    varış_havalimanı=havalimanlari[varış_seçimi]
    print("Varış  Havalimanı:",varış_havalimanı)
except KeyError:
    print("Yanlış seçim yaptınız")
    exit()
time.sleep(1)
print(f"{kalkış_havalimanı}-{varış_havalimanı}arası uçuşunuz için lütfen diğer işlemlere devam ediniz")
print("Lütfen tarih seçiniz")
time.sleep(1)

yıl=int(input("İşlem yapmak istediğiniz yılı seçiniz:"))
aylar={
        "ocak":1,"şubat":2,"mart":3,"nisan":4,"mayıs":5,"haziran":6,
        "temmuz":7,"ağustos":8,"eylül":9,"ekim":10,"kasım":11,"aralık":12# tarih hatası!!!
        }
ay=str(input("İşlem yapmak istediğiniz ayı seçiniz:"))
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

 
