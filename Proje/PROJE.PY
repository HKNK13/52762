import time 
import calendar
#print("Tek yön\n""Gidiş-Dönüş")
#yön_seçim=input("Yön seçiminizi yapınız(Tek yön için 1'e basınız.Gidiş-Dönüş için ise 2'e basınız2):")
havalimanlari={ 
    1:"Ankara Esenboğa Havalimanı",
    2:"İstanbul Sabiha Gökçen Havalimanı",
    3:"Van Ferit Melen Havalimanı",
    4:"Izmir Adnan Menderes Havalimanı",
    5:"Fraport Tav Antalya Havalimanı"}
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
ay=str(input("İşlem yapmak istediğiniz ayı yazınız:"))
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
#print(f"{yıl}-{ayı}-{gün} tarihindeki uçuşlarımız")
time.sleep(1)
def uçuş_seçim():
    havalimanlari_listesi=["Ankara Esenboğa Havalimanı","İstanbul Sabiha Gökçen Havalimanı","Van Ferit Melen Havalimanı",
                            "Izmir Adnan Menderes Havalimanı","Fraport Tav Antalya Havalimanı"]
    if kalkış_havalimanı==havalimanlari_listesi[0]:
        if varış_havalimanı==havalimanlari_listesi[1]:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"{yıl}-{ay}-{gün}-{uçuş}")
        elif varış_havalimanı==havalimanlari_listesi[2]:
            uçuş_saatleri={1:"09.00",2:"11.00"}
            for key,value in uçuş_saatleri.items():
                print(f"{key}:{value}")
            uçuş_seç=int(input("İstediğiniz uçuş numarasını girin:"))
            uçuş=uçuş_saatleri[uçuş_seç]
            print(f"Uçuş bilgileriniz:{yıl}-{ay}-{gün}-{uçuş}")
uçuş_seçim() 