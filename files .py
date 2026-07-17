f =open ("dectionary.py","r")
data = f.read() 
print (data)
print (type(data))
f.close()

#readline
f = open ("dectionary.py","r")
data = f.read()
line1 = f.readline()
print (line1) 
line2 = f.readline()
print (line2)

#writing file
f= open ("nothing","a")
f.write("\nthis is a new line")
f.close()

#to change a specfic line
f = open ("nothing","r")
line =f.readlines()
f.close()
line[2]="i am from HP \n"
f = open ("nothing","w")
f.writelines(line)
f.close()

#r+
with open("nothing","r+") as f:
    f.write ("HELLO")
f.close   

#w+
with open ("nothing","w+") as f :
    f.write ("HELLO\nmy name is aryan\ni am from HP\n kangra dist\ni'm curently studying in bca 1st semester\ni have started my coding journey from 09/07/2026\nnow i am learning python\nthis is a new line ")

    f.seek(0)
    print (f.read())
f.close()

#a+
with open("nothing","a+") as f:
    f.write("\n bye bye ")
    f.seek(0)
    print (f.read())
f.close

import os
os.remove("sample.py")

#create a new file using python. add the following data in it:             hi everyone                           we are learning file i/o           using python                           i like programming in python.

with open ("sample.txt","w") as f:
    f.write("hi everyone\nwe are learning file i/o\nusing python\ni like programming in python.")



#replace all occurrences of Java with python in                               hi everyone                           we are learning file i/o                using Java                             i like programming in Java.

with open("sample.txt","r") as f :
    data = f.read()
    new_data =data.replace("Java","python")
print (new_data)
with open ("sample.txt","w") as f:
    f.write(new_data)


#search if the word "learning" exists in the file or not 
word = "learning"
with open ("sample.txt","r") as f:
    data =f.read()
    position=data.find(word)
    if position != -1:
        print ("found at index",position) 
    else :
        print ("not found")


word = "learning"

with open("sample.txt", "r") as f:
    data = f.read()

if word in data:
    print("Found")
else:
    print("Not found")


#find in which linne of the file does the word "learning" occur first. print -1 if not found
word = "learning"
with open ("sample.txt","r") as f:
    for line_no , line in enumerate(f,start =1):
        if word in line :
            print (" word found on line",line_no)


word = "learning"
data = True
line_no = 1
with open ("sample.txt","r") as f:
    while data :
        data = f.readline()
        if (word in data):
            print (line_no)
            break
        line_no+=1
    else :
        print ("-1")


#find in which linne of the file does the word "learning" all occurances. print -1 if not found


word = "learning"
data = True
found = False
line_no = 1
with open ("sample.txt","r") as f:
    while data :
        data = f.readline()
        if (word in data):
            print (line_no)
            found = True
        line_no+=1
    if not found :
        print ("-1")
       

#from a file conataining numbers separated by comma , print the count of even numbers .
count = 0
with open ("numbers", "r") as f:
    data = f.read()
    numbers = data.split(",")
    for i in numbers :
        num = int(i)
        if (num % 2 == 0) :
         count += 1
print (count )


 # to print no.
with open ("numbers", "r") as f:
    data = f.read()
    print (data) 

    num = ""
    for i in range (len(data)):
        if (data[i] == ","):
            print (int (num ))
            num=""
        else :
            num +=data[i]