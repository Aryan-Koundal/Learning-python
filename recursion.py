def show (n):
    if (n==0):
        return
    print (n)
    show (n-1)
show (5)


n= int(input("entre a number"))
i = 1
fact = 1 
for i in range (1,n+1):
    i*=1
    fact*=i
    print(fact) 


def fact(n):
    if (n==1 or n==0):
     return 1
    return fact (n-1)*n
number= (5)
print (fact(number))
    
#write a recrusive function to calculate the sum of first n natural no.
def sum (n):
    if (n==1 or n==1):
        return 1
    return sum(n-1)+n
print (sum (5))

# #write a recrusive function to print all elements in a list [hint : use list & index as parameter]
def element (list , idx):
    if (idx ==len(list)):
        return 
    print (list[idx])
    element (list , idx +1)
number = [1,2,3,4,5,6]
element(number,0)

# #write a recursive function to calculate the sum of all elements in a list 
def element (n):
    if (n==0):
        return 
      