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

