import requests as req
import tkinter as tk

#screen
screen = tk.Tk()
screen.title("Hava Durumu")
screen.minsize(500, 300)
screen.iconbitmap('my projects/weather apps/weather.ico')
font_options = ('Comic Sans Ms', 12, 'bold')
#Functions
def havadurumu(sehir , api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api}&units=metric"
    response = req.get(url)
    veri = response.json()
    return veri
def searchButton():
    if __name__ == "__main__":
        sehir = city_entry.get()
        api = "***(For Security)"
        try:
            weatherResult = havadurumu(sehir, api)

            for widget in screen.winfo_children():
                if isinstance(widget, tk.Label) and widget != welcome_label:
                    widget.destroy()
            
            cityLabel = tk.Label(text=f"{sehir} şehrinin hava durumu:  ")
            cityLabel.pack()
            cityTempLabel = tk.Label(text=f"Sıcaklık: {weatherResult['main']['temp']} °C")
            cityTempLabel.pack()
            cityHumidty = tk.Label(text=f"Nem oranı: {weatherResult['main']['humidity']}%")
            cityHumidty.pack()
            cityDescription= tk.Label(text=f"Açıklama: {weatherResult['weather'][0]['description']}")
            cityDescription.pack()

        except Exception :
            errorLabel = tk.Label(fg="red" , text=f"Hata! Sonuç Bulunamadı. ")
            errorLabel.pack()


#UI
welcome_label = tk.Label(text="Merhaba \n Lütfen hava durumunu öğrenmek istediğiniz şehri giriniz:", font=font_options)
welcome_label.pack()
city_entry = tk.Entry(width=40)
city_entry.pack()
search_button = tk.Button(text="Öğren🔎", width=33,command= searchButton)
search_button.pack()
screen.mainloop()

#describe sonucuna göre labelların altına resim eklenebilir.
#sonuçlar ve hata mesajı bildirim penceresinde gösterilebilir.