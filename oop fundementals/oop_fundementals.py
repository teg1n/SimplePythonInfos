#OBJE ODAKLI PROGRAMLAMA

# 1- Inheritance -> bir class'dan kalıtım almak ve kalıtım alınan class'a ek değerler oluşturabiliriz 

class Musician():

    def __init__(self):
        print("Musician class")
    
    def test1(self):
        print("test1")

    def test2(self):
        print("test2")


class MusicianPlus(Musician): # (tıpkı discordda kullanıcılara verilen roller gibi)

    def __init__(self):
        Musician.__init__(self)
        print("Musician Plus")

# 2- Polymorphism -> Birbirinden farklı classların ortak methodlarını kullanmayı sağlar (Konuyla alakalı son komut satırında örneği verildi)

class Banana():
    def __init__(self,name):
        self.name = name

    def info(self):
        return f"100 calories {self.name}"

class Apple():
    def __init__(self,name):
        self.name = name

    def info(self):
        return f"150 calories {self.name}"

banana = Banana("banana")
apple = Apple("apple")

fruitList = [banana,apple]

for fruit in fruitList:
    fruit.info() 
'''
Output : 100 Calories banana 
         150 Calories apple
'''

# 3- Encapsulation -> Yazılan kodda belirli değişkenlerin değiştirilmemesi için kullanılır

class Phone():

    def __init__(self,name,price):
        self.name = name 
        self.__price = price # Bu kullanım input ile bilgi değişiminin önüne geçer eğer bilinçli bir şekilde korumalı değişim yapılmak isteniyorsa : 

    def changePrice(self,price):
        self.__price = price #Bu sayede kullanıcı belirli bir methodla erişim engeli olan bilginin değişimini sağlayabilir (gta oyunlarında belirli şifrelerle hile kullanmak gibi)

    def info(self):
        print(f"{self.name} price is {self.price}")

iphone = Phone("IPhone 14",500)

iphone.info # output : IPhone 14 price is 500

# 4- Abstraction -> Bir kalıp oluşturmak ve kalıbın yapısını farklı yerlerde kullanmak

from abc import ABC , abstractclassmethod

class Car(ABC):
    @abstractclassmethod
    def maxSpeed(Self):
        pass

class Tesla(Car):
   
    def maxSpeed(self): #girilmesi zorunlu oldu çünkü kalıba alındı
        print("250 kmh")

tesla = Tesla()

#Extra -> pythonda dahili olan methodları değiştirmek mümkün (pythonun dahili methodları class için özel olarak atanmadığında hata verir)

class Fruit():
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return f"{self.name: {self.calories} calories}"