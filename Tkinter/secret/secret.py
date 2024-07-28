from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64



#Creating Screen
screen = Tk()
screen.title("Shhhh :)")
screen.minsize(300,550)
screen.config(padx=30 , pady=30)

#Adding logo    
screen.iconbitmap('Tkinter/secret/secret.ico')
icon = PhotoImage(file='Tkinter/secret/secret.png')
icon = icon.subsample(6,6)
iconLabel= Label(image=icon)
iconLabel.pack()


#Adding Functions
    #Creating File & Encrypt or Decrypt

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

    
def creatingfile():
    title = titleEntry.get() 
    text = secretText.get("1.0", END)
    master_key = masterKeyEntry.get()

    if title == "" or  master_key == "":
        messagebox.showwarning("Uyarı", "Tüm girişleri yapınız!")
        return 

    file_name = f"{title}.txt" 
    message_encrypted = encode(master_key, text)
    try:
        with open(file_name, 'w') as file:
            file.write(f"{title}\n{message_encrypted}")
        messagebox.showinfo("Başarı", f"Dosya başarıyla oluşturuldu: {file_name}")
    except Exception as e:
        messagebox.showerror("Hata", "Dosya oluşturulamadı")
    finally:
        titleEntry.delete(0,END)
        masterKeyEntry.delete(0,END)
        secretText.delete("1.0", END)

def readingfile():
    message_encrypted = secretText.get("1.0", END)
    masterKey= masterKeyEntry.get()
    if message_encrypted== "" or masterKey=="":
        messagebox.showerror("Hata", "Lütfen geçerli bilgiler giriniz!!!")
    else:
        try:
            decrypted_messeage = decode(masterKey, message_encrypted)
            secretText.delete("1.0", END)
            secretText.insert(1.0,decrypted_messeage)
        except:
            messagebox.showwarning("Hata","Lütfen işlemleri doğru yaptığınızdan emin olun.")
#Adding Input Layers
    #Title Label
titleLabel = Label(bg="red", font=("Helvetica", 8, "bold") , text="Başlığınızı giriniz (Başlığınız gizli olmayacak !!!) :")
titleLabel.pack() 
    #Title Input
titleEntry = Entry()
titleEntry.pack()
    #Secret Label
secretTextLabel = Label(text="Gizlemek istediğiniz içeriği girin: ")
secretTextLabel.pack()
    #Secret Input
secretText = Text(width=30 , height=19 )
secretText.pack()
    #Masterkey Label
masterKeyLabel = Label(text="Girdiğiniz bilgileri şifreleyin: ")
masterKeyLabel.pack()
    #MAsterkey Inout
masterKeyEntry = Entry()
masterKeyEntry.pack()

#Adding Buttons
    #Crypte Button
saveAndEncrypt = Button(text="Şifrele & Kaydet", command=creatingfile)
saveAndEncrypt.pack()
    #Decrypt Button
decrypt= Button(text="Çöz", command=readingfile)
decrypt.pack()


mainloop()