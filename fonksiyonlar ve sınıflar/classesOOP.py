class Person(): #büyük harfle yazılması önerilir ve Person class oluşturulur
    
    job = 'Öğrenci' #input alınarak değişilene kadar default değer oluşturur

    #method , initializer
    def __init__(self, name , age , gender): #self sınıf içerisinde ZORUNLU gruplandırma oluşturmak için kullanılır
        self.name = name
        self.age = age
        self.gender =gender

'''ali = Person() #verilen ismi Person olarak adlandırılmış classa ekledi'''

ali = Person("ali" , 20 , "male") #person class içerisinde bulunan ali değişkenin üzerine isim yaş ve cinsiyet ekler 

ali.age #Person class içerisine eklenmiş olan isimde class üzerine eklenmiş olan 'age'girdisini sorgular = 20