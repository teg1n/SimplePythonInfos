"""
class Dog():
    
    year = 7 #humanage hesaplamasında direkt sayı yerine değişken yapılabilir mi diye test ediyoruz

    def __init__(self , age):
        self.age = age
    def humanAge(self): # bu method init altına da eklenebilir 
        return self.age * Dog.year #self.year -> Dog.year (Dog class altında atama yaptığımız için iki kullanım da doğrudur)

myDog = Dog(3) # myDog.age = 3

myDog.humanAge #myDog.humanAge = 21

print(myDog.humanAge)
"""
#example
class Cars:
    def __init__(self, countries , brands , models, year , price):
        self.countries = countries
        self.brands = brands
        self.models = models
        self.year = year
        self.price = price
    def gettingInfo():
        gotBrands = input("Lütfen aracınızın modelini giriniz: ") 

Countries = ("alman", "japon", "amerikan")
gotBrands = []
while True :
    userCountryInput = input("Lütfen aracınızın uyruğunu giriniz: (Ör: amerikan , japon , alman)").lower()
    if userCountryInput in Countries :
        Cars.append(userCountryInput)
        break
    else:
        input("Lütfen geçerli bir ülke girin: ")

