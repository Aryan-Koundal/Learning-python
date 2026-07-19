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
