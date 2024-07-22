import requests

def hava_durumu_ögren(sehir , api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api}&units=metric"
    response = requests.get(url)
    veri = response.json()
    return veri

if __name__ == "__main__":
    sehir= input("Lütfen hava durumunu öğrenmek istediğiniz şehrin adını girin: ")
    api = "1a3b293bc841634ab69adf4a6a2b3a91"

    try:
        hava_durumu = hava_durumu_ögren(sehir,api)
        print(f"{sehir} şehrinin hava durumu: ")
        print(f"Sıcaklık: {hava_durumu['main']['temp']} °C")
        print(f"Nem oranı: {hava_durumu['main']['humidity']}%")
        print(f"Açıklama: {hava_durumu['weather'][0]['description']}")
    except Exception as ex:
        print(f"Hata oluştu: {ex}")