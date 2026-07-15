a=float(input("entre a value"))
b=float(input("entre a value"))
print (a>=b)
name = (input ("entre your name"))
print ("welcome:",name )
print ("lenght of your name is",len(name))

fav_movies = []
fav_movie1 = (input("entre your fav movie"))
fav_movie2 = (input("entre your fav movie"))
fav_movie3= (input("entre your fav movie"))
fav_movies.append(fav_movie1)
fav_movies.append(fav_movie2)
fav_movies.append(fav_movie3)
fav_movies.sort()
print (fav_movies)

list = [1,2,1]
list2 = list.copy()
list2.reverse()
if(list2==list):
    print ("palindrome")
else:
    print ("not a palindrome")

grade= ['A','B','B','C','A','C','D','B','A']
print(grade.count("A"))
print (grade)

student = {
    "name": input("entre your name"),
    "age":int (input("entre your age")),
    "class": input ("entre your class"),
    "marks" :[]
}
subject = ["english","maths","economics","business studies","accountancy"]
for a in range (5) :
    marks = int(input(f"entre your marks of {subject[a]:}"))
    student["marks"].append(marks)
print (student["name"])
print("Marks :", student["marks"])
student = {
    "name": input("entre your name "),
    "age": int(input("entre your age")),
    "class": input("entre your class"),
    "marks": []
}
subject = ["eco", "maths", "english", "business", "computer"]
for i in range(5):
    marks = int(input(f"entre your marks of {subject[i]}"))
    student["marks"].append(marks)
print("marks", student["marks"])


dictionary= {
    "cat":"a small type pokemon",
    "table" : ["a piece of furniture","list of facts &figures"]
}
print (dictionary)

subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}
print (len(subjects))


subject={}
a=int(input("entre your english marks"))
b=int(input("entre your maths marks"))
c=int(input("entre your computer marks"))

subject.update({"english": a ,
                "maths": b,
                "computer":c})
for key , value in subject .items ():
    print (f"{key}:{value}/100")

values = {
    ("float",9.0),
    ("int",9)
}
print (values)


n = int(input("Enter the numbers whose sum you want to find"))
sum = 0
count = 1
while count<=5:
    count+=1
    sum +=n
print ("first 5 sum of",n,"is",sum)

sum = 0
count = 1 
while count <=5:
    num = int (input ("entre a number"))
    sum +=num
    count +=1
    print ("sum=",sum)

n=int (input ("entre your no."))
sum = 0 
i=1 
for i in range (n):
    i+=1
    sum+=n
    

    print (sum)


n=int (input ("entre your no."))
sum = 0 
i=1 
for i in range (n):
    i+=1
    sum+=n

    print (sum)

    
n=int(input("entre your number"))
fact = 1
i = 1
for i in range (1,n+1):
    i *=1
    fact *= i
    print (fact)

n= int(input("entre a number"))
i = 1
fact = 1 
for i in range (1,n+1):
    i*=1
    fact*=i
    print(fact) 