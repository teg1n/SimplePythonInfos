#map

def toplamaFunc(sayilar): #verilen listedeki sayılar üzerinde belirlenmis islemi yapıp yeni bir liste olusturur
    return sayilar / 2
sayilar =[10 , 20 , 30]

list(map(toplamaFunc , sayilar)) #[5 , 10 , 15] 

#filter

def kontrolStrings(string): #icerisinde ali gecen stringlerde 'true' değeri döndürür
    return "ali" in string

isimler= ["ali" , "ali köse" , "evsa", "taner"]

list(filter(kontrolStrings,isimler)) #[ali, ali köse]

