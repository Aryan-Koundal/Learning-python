count = 1 
while count <= 5:
    print ("hello", count)
    count += 1 
    print (count)


i =  0
while i<=10 : 
    print (i)
    i+=1


i = 5
while i >= 0 :
    print (i)
    i-=1

 # print numbers from 0 - 100
i = 0
while i <=100 :
    print(i)
    i +=1

# #print numbers form 100 - 0
i = 100
while i >=0:
    print (i)
    i-=1

# #table of 3
i = 1
while i <=10:
    print ("3*",(i),"=" ,(3*i))
    i+=1

# #print the elements of the following list using loop[1,2,3,4,5,6,7,8,9,0]
num = [1,2,3,4,5,6,7,8,9,0]
i= 0
while i < len(num):
    print (num[i])
    i += 1

# #print the elements in revers of the following list using loop[1,2,3,4,5,6,7,8,9,0]
num = [1,2,3,4,5,6,7,8,9,0]
i= len(num) -1
while i >=0:
    print (num[i])
    i -= 1

#find the x no.
num=(1,2,3,4,5,5,22,6,7,8,9,0)
x=6
i=0
while i<len(num):
    if (num[i]== x):
        print ("found at idx",i)
    i+=1


#break
i=1
while i<=5 :
    print (i)
    if(i==3):
        break
    i+=1

#continue 
i = 0
while i<=10:
     if ( i%2 !=0):
        i+=1
        continue
     print(i)
     i+=1