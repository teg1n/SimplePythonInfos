import requests

def hava_durumu_ögren(sehir , api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api}&units=metric"
    response = requests.get(url)
    veri = response.json()
    return veri

if __name__ == "__main__":
    sehir= input("Lütfen hava durumunu öğrenmek istediğiniz şehrin adını girin: ")
    api = "***(For Security)"

    