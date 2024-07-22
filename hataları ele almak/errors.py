#kodların içerisindeki hataların uygulamayı çökertmesini engellemek için kullanılabilecek methodlar

age = input("Lütfen yaşınızı giriniz:")
int(age)*2

# try - except = Böylelikle olası hata mesajları ve uygulama çökmelerine karşı önlem almış oluruz

while True:
    try:
        myAge = int(input("Lütfen yaşınızı giriniz: "))
        print(myAge *2)
        break
    except : #except "Error = özellikle belirli hata tiplerini de girebiliriz
        print("Lütfen yaşınızı doğru giriniz: ")