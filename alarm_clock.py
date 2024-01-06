from datetime import datetime, timedelta
import time
import winsound


# alarm sesli uyaranı
def beep_alarm():
    print("ALAAAARM!")
    winsound.Beep(500, 100)


# alarm çalma
def alarm(alarm_saati):
    # aldığımız alarm saatiyle şimdiyi karşılaştır
    while datetime.now() < alarm_saati:  # True
        time.sleep(60)  # 1 dk uyut
    # False
    beep_alarm()


# girilen değerlerin kontrolü
# saat
def get_valid_hour():
    # en altta get_valid_hour() yapmasaydım burada while True da kullanılabilirdi
    # hata çıkabilecek yer saati aldığımız kısım
    try:
        # saat'le sayısal işlemler olacak o nedenle değer int olmalı
        hour = int(input("Alarm saati girin(0-23): "))

        # kontrolü sağla
        if not 0 <= hour <= 23:
            raise ValueError("Saat değeri 0-23 aralığında olmalı!")
        # eğer bu aralıktaysa saati dön
        return hour
    except:
        get_valid_hour()


# dakika
def get_valid_minute():
    try:
        minute = int(input("Alarm dakikası girin(0-59): "))
        if not 0 <= minute <= 59:
            raise ValueError("Dakika değeri 0-59 aralığında olmalı!")
        return minute
    except:
        get_valid_minute()


# erteleme
def get_valid_delay():
    try:
        delay_ = int(input("Erteleme için dakika girin(0-5): "))
        if not 0 <= delay_ <= 5:
            raise ValueError("Erteleme değeri 0-5 aralığında olmalı!")
        return delay_
    except:
        get_valid_delay()


#  erteleme için fonksiyon
# erteleme için eski alarm saatinin özellikle dakikasına belli bir dakika eklemem lazım
def delay(alarm_saati, dk):
    yeni_alarm_saati = alarm_saati + timedelta(minutes=dk)
    print(f"Alarm {dk} ertelendi!\nYeni alarm saati:{yeni_alarm_saati:%H:%M}")
    # bu yeni saati kullanabilmek için değeri döndürüyorum
    return yeni_alarm_saati


#  ne kadar süre kaldı
def ne_kadar_var(alarm_saati):
    kalan_saat = datetime.now().hour - alarm_saati.hour
    kalan_dakika = datetime.now().minute - alarm_saati.minute
    print(f"Alarm için {kalan_saat} saat {kalan_dakika} dakika kaldı")


# ana fonksiyon her şey burada olacak
def set_alarm():
    saat = get_valid_hour()
    dakika = get_valid_minute()

    alarm_saati = datetime.now().replace(hour=saat, minute=dakika, second=0, microsecond=0)
    print(f"Alarm saati:{alarm_saati:%H:%M}")

    nott = input("Alarm notu eklensin mi(y/n): ")

    if nott.lower() == "y":
      nott_ = input()

    ne_kadar_var(alarm_saati)
    print(nott_)

    to_delay = input("Alarmı ertelemek istiyor musun(y/n): ")

    if to_delay.lower() == "y":
        # erteleme için belli bir dakika almam lazım
        delay_dk = get_valid_delay()
        # şimdi aldığım dakikayı eski saate ekleyerek daha önceki alarm saatini güncellemeliyim
        alarm_saati = delay(alarm_saati, delay_dk)
        ne_kadar_var(alarm_saati)

    # alarm saatini ertelediğimde yeni bir alarm kuruldu bu durumda alarmı baştan çalıştırmalıyım
    # ya da ertelemek istemiyorsa zaten if bloğuna girmez ve yine direkt alarm karşılaştırmasına gider
    alarm(alarm_saati)

set_alarm()