def calculate_sum(a,b):
    sum = a+b
    return sum
print(calculate_sum(2,3))
print (calculate_sum(4,5))


def cal_sum (a,b):
    return a+b
print(cal_sum(2,33))

print(cal_sum(33,4))


def print_hello():
  print ("hello")
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

def aryan (a,b):
    sum= a+b
    return sum
print (aryan(2,3))

def avg (a,b,c):
    sum = a+ b + c
    avg = sum/3 
    return avg 
result =avg (1,2,3)
print (result)

print ("aryan",end=" ")
print ("koundal" )

def number(a,b):
  sum = a*b
  return sum 
numb = int (input ("entre your 1st no."))
numb2 = int (input ("entre your 2nd no."))
print (number(numb,numb2))

#print the lenght of a list (list is  the parameter)
name  = ["aryan", "koundal", "kaku", "anku", "harsh"]
heros = ["thor","hulk","ironman"]
def aryan(list):
   print (len(list))
aryan (name )
aryan (heros)

# print the elements of a list in a single line (list is the parameter)
name  = ["aryan","koundal", "kaku", "anku", "harsh"]
print (name [0],end = " ")
print (name[1],end = " ")
print (name[2])
def list_name (list):
    for item in list :
     print ( item , end=" ")
list_name(name)

#find the factorial of n (n is the parameter)
def cal_fact(n):
      fact = 1 
      for i in range (1,n+1):
       fact *= i
      print (fact)
cal_fact(int(input("entre your no.")))


#convert USD to INR
def converter (USD):
    INR = USD *93 
    return INR
USD =(int (input("entre how much USD you want to convert into INR")))
INR = converter(USD)
print (USD, "USD=",INR,"INR")


def converter(USD):
    INR = USD * 93
    print(USD, "USD =", INR, "INR")

usd = int(input("Enter how much USD you want to convert into INR: "))
converter(usd)

#find odd and even no.
def number(a):
    if (a % 2==0):
        print ("this is a even no.")
    else :
     print("this is a odd no.")
numb = int (input ("entre a nuber"))
number(numb)

