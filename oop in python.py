class Student :
    college_name = "Aryan college " 
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print ("adding new student in database")
    def hello (self):
        print ("hello student",self.name)

    def mark (self):
        print ("you got",self.marks,"marks")

s1 = Student("aryan",97)
s1.hello() 
s1.mark()
print ("from ",Student.college_name)
s2 = Student("kaku",97)
s2.hello()
s2.mark()
print ("from ",Student.college_name)

 
class Car:
    colour = "blue"
    brand = "mercedes"
car1 = Car()
car2 = Car()
print (car1.colour)
print (car1.brand)

#create student class that takes names & marks of 3 subjects as argument in constructor. then create a method to print average
class Students :
    college_name = "Aryan college"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks

    def get_avg(self):
        sum = 0
        for val in self.marks :
                sum+=val
        print ("hi",self.name,"your avg score is",sum/3)
        
s1 = Students("aryan",[99,98,97])
s1.get_avg()
s2 = Students("kaku",[99,96,97])
s2.get_avg()


#statics methods

class Students :
    college_name = "Aryan college"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
    
    @staticmethod
    def hello ():
        print ("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks :
                sum+=val
        print ("hi",self.name,"your avg score is",sum/3)
        
s1 = Students("aryan",[99,98,97])
s1.get_avg()
s1.hello() 

#abstraction
class Car :
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start (self):
        self.clutch = True
        self.acc = True
        print ("car started...")
car1 = Car()
car1.start()


#encapsulation
class Students :
    college_name = "Aryan college"
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks

    def get_avg(self):
        sum = 0
        for val in self.marks :
                sum+=val
        print ("hi",self.name,"your avg score is",sum/3)
        
s1 = Students("aryan",[99,98,97])
s1.get_avg()
s2 = Students("kaku",[99,96,97])
s2.get_avg()


#create account class 2 attributes - balance & account no.                                                                       create methods for debit , credit & printing the balance 
class Account :
    def __init__(self,balance,account):
        self.balance = balance
        self.account_no = account

    def debit (self,amount):
        self.balance -= amount
        print ("Rs.", amount,"was debited")
        print ("total balance =", self.end_balance())

    def credit (self,amount):
        self.balance+=amount
        print ("Rs.",amount,"was credited")
        print ("total balance =", self.end_balance())
    def end_balance (self):
        return self.balance
acc1 = Account(10000,"aryan123")
acc1.debit(100)
acc1.credit(10000)
  

#del keyword
class Student :
    def __init__(self,name):
        self.name = name 

s1 = Student("kaku")
print (s1.name)
del s1.name
print (s1.name)

#private and public attribute
class Acc :
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print (self.__acc_pass)

acc1 = Acc("123","321")
print (acc1.acc_no)
print (acc1.reset_pass())

class Person:
    __name = "Aryan"

    def __hello(self):
        print ("hello user")

    def Welcome (self):
        self.__hello()

p1 = Person ()
print (p1.Welcome())

# Inheritance
#single inheritance
class Car :
    @staticmethod
    def start ():
        print ("car started")
        

    @staticmethod
    def stop ():
        print ("car stoped")
        

class Toyota(Car):
    def __init__(self,name):
        self.name = name 
car1 = Toyota("fortuner")
car2 = Toyota("prius")
print (car1.name)
car1.start()
car1.stop()
print (car2.name)
car2.start ()
car2.stop()

#multi level inheritance
class Car :
    @staticmethod
    def start ():
        print ("car started")
        

    @staticmethod
    def stop ():
        print ("car stoped")
        

class Toyota(Car):
    def __init__(self,name):
        self.name = name
 
class Fortuner(Toyota):
    def __init__(self,type):
        self.type = type

car1 = Toyota("Fortuner")
print (car1.name)
car1 = Fortuner("diesel")
print ("type",car1.type)
car1.start()


#multiple inheritance

class A :
    a = "welcome to class A"

class B :
    b = "welcome to class B"

class C (A,B):
    c = "welcome to class c"

c1 = C()
print (c1.c)
print (c1.b)
print (c1.a)


# super method 
class Car :
    def __init__(self,type):
      self.type = type
    @staticmethod
    def start ():
       print ("car started...")
    @staticmethod
    def stop():
       print ("car stopped.")
class Toyota(Car):
    def __init__(self,name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = Toyota("fortuner","electric")
print (car1.type)
   

#class method 
class Student :
    name = "aryan"
    @classmethod
    def changename (cls, name ):
        cls.name = name
p1 = Student()
p1.changename("kaku")
print (p1.name)
print (Student.name)

#another method 
class Student :
    name = "aryan"
    
    def changename (self , name ):
        self.__class__.name = "kaku"
        Student.name = name
p1 = Student()
p1.changename("kaku")
print (p1.name)
print (Student.name)

#property
class Student :
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        @property
        def percentage (self):
            return str((self.chem+self.math+self.phy)/3)+"%"
student1 = Student(98,89,97)
print (student1.precentage,"%")
student1.phy = 89
print (student1.phy)
student1.percentage()
print (student1.precentage,"%")


#without property
class Student :
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.precentage = str((self.chem+self.math+self.phy)/3)+"%"

    def percentage (self):
         self.precentage = str((self.chem+self.math+self.phy)/3)+"%"
student1 = Student(98,89,97)
print (student1.precentage,"%")
student1.phy = 89
print (student1.phy)
student1.percentage()
print (student1.precentage,"%")

#polymorphism : operator overloading 

print (1+2)
print ("aryan"+"koundal")
print ([1,2,3]+[4,5,6])

#add dunder function
class Complex:
    def __init__(self,real,img):
     self.real = real
     self.img = img

    def show_number (self):
       print (self.real,"i+",self.img,"j")

    def __add__ (self,num):
       newreal = self.real + num.real
       newimg = self.img + num.img
       return Complex(newreal,newimg)

num1 = Complex(1,3)
num1.show_number()
num2 = Complex(4,8)
num2.show_number()
num3 = num1+num2
num3.show_number()

#without dunder function
class Complex:
    def __init__(self,real,img):
     self.real = real
     self.img = img

    def show_number (self):
       print (self.real,"i+",self.img,"j")

    def add (self,num):
       newreal = self.real + num.real
       newimg = self.img + num.img
       return Complex(newreal,newimg)

num1 = Complex(1,3)
num1.show_number()
num2 = Complex(4,8)
num2.show_number()
num3 = num1.add(num2)
num3.show_number()


#define a circle class to create with radius r using the constructor .define an area()method of the class which calculates the area of th circle. define a perimeter() method of the circle which allows you to calculates the perimeter of the circle.
class Circle :
    def __init__(self,radius):
      self.radius = radius 
    
    def area (self):
       return 3.14*self.radius**2

    def perimeter (self):
       return 2*3.14*self.radius
    
Circle1 = Circle(14)
print (Circle1.area())
print (Circle1.perimeter())

#define a employee class with attributes role , department & salary . this class also has a showDetail() method . create an engineer class that inherits that properties from employee & has additional attributes :name &age                                                                 

class Employee :
    def __init__(self, role , department , salary):
        self.role = role 
        self.department = department
        self.salary = salary
    
    def showDetail(self):
        print ("role =",self.role)
        print ("department =", self.department)
        print ("salary =",self.salary)

class Engineer (Employee):
    def __init__(self, name , age ):
        self.name = name 
        self.age = age 
        super().__init__("Engineer","head","$500")
    def showDetail(self):
        print ("Name =",self.name)
        print ("age=",self.age)
        super().showDetail()

e1 = Employee("head","3rd","$400")
print (e1.salary)
e1.showDetail()

e2 = Engineer("Aryan","18")
e2.showDetail()


#cereate a classs Order which stores item & its price . use dunder function __gt__() to convey that:                                        order1>oder if order1> price of order2
class Order :
    def __init__ (self,item,price):
        self.item = item
        self.price = price 

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order ("chips",20)
odr2 = Order("kurkure",50)
print (odr1>odr2)