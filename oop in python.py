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

