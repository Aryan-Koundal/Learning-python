# age = int(input ("entre your age"))
# if (age >= 18):
#  print("can vote & apply for license")
# else :
#    if(age<18):
#     print ("you cannot vote & apply for license")
# #code for traffic light wiht conditions 
# light = "red "
# if (light == "green"):
#   print ("you can go now")
# elif (light == "yello"):
#   print ("wait for a moment")
# elif ("light == red"):
#   print ("stop")
# else:
#   print ("the light is broken")

# print ("end of code")


# #code for grading marks
# marks = int(input("entre your marks"))
# if ( marks>=90):
#   print ("you got A+")
# elif(marks>=80):
#   print ("you got A")
# elif(marks>=70):
#   print ("you got B+")  
# elif(marks>=60):
#   print ("you got B")
# elif (marks >=50):
#   print ("you got C+")
# elif(marks>=40):
#  print("you got c")
# else :
#  print("you got failed")

# #nesting
# age = int(input("entre your age"))
# if (age>=18):
#     if (age >=80):
#      print ("you cannot drive")
# else:
#     print ("you can drive")

# # to find weather it is a even or odd no.
# number = int (input("entre your number"))
# if (number % 2==0):
#   print ("this is a even no.")
# else :
#   print(" this is a odd no.")

# # to find the greatest of three numbers
# a = int (input ("entre first numbers"))
# b= int (input ("entre second number"))
# c = int (input ("entre third number"))
# if (a>=b and a>=c):
#     print ("a is the greatest number")
# elif (b>=c):
#   print ("b is the greatest number")
# else :
#    print ("c is the greatest number")

# # to check weather it is a multiple of a no. or not
# number = int(input("entre a number"))
# if (number % 5 == 0):
#     print ("this number is multiply of 5")
# else :
#     print ("not a multiply of 5")
    
class Solution:
    def fizzBuzz(self, n: int):
        bucket = []
        for i in range (1,n+1):
             if (i%3==0)and(i%5==0):
                 bucket.append("FizzBuzz")
             elif (i%3==0):
                 bucket.append("Fizz")
             elif (i%5==0):
                 bucket.append("Buzz")
             else:
                a = str(i)
                bucket.append(a)
        return(bucket)
Solution.fizzBuzz()