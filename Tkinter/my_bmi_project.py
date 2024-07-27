from tkinter import *

#screen created (Ekran şablonu)
screen = Tk()
screen.title("Boy-Kilo Endeksi")
screen.minsize(350 , 150)

#calculating function (işlem fonksiyonu)
def calculate():
    try:
        
        weight= float(weight_entry.get())
        height= float(height_entr.get())
        heightm= height/100

        bmi= weight / (heightm**2)
        if bmi <= 18.4:
            bmi_label.config(text=f"Boy-Kilo endeks sonucunuz: {bmi:.2f}. Çok zayıfsınız.")
        elif 18.5 <= bmi <24.9: 
            bmi_label.config(text=f"Boy-Kilo endeks sonucunuz: {bmi:.2f}. Normal kilodasınız.")
        elif 25.0 <= bmi < 39.9:
            bmi_label.config(text=f"Boy-Kilo endeks sonucunuz: {bmi:.2f}. Kilolusunuz.")
        else: 
            bmi_label.config(text=f"Boy-Kilo endeks sonucunuz: {bmi:.2f}. Obezsiniz.")

    except ValueError:
     errorlabel.config(text="Lütfen geçerli bir değer giriniz.")

#error label (Hatalı 'str' tuşlama sonucunda gösterilecek metin)
errorlabel = Label(text="", fg="red")
errorlabel.pack()

#inputs (Kullanıcıdan bilgi alma)
weight_label = Label(text="Lütfen kilonuzu giriniz (kg):")
weight_label.pack()
weight_entry = Entry()
weight_entry.pack()
height_label = Label(text="Lütfen boyunuzu giriniz (cm): ")
height_label.pack()
height_entr= Entry()
height_entr.pack()

#calculating button ('hesaplama' tuşunun eklenmesi)
buton= Button(text="Hesapla", command=calculate)
buton.pack()

#result label (Sonucun kullanıcıya bildirilmesi)
bmi_label = Label(text=f"")
bmi_label.pack()


mainloop()