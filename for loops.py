nums = "aryan"
for char in nums:
    if (char=='n'):
     print("n found")
     break
      
    else:
       print("end")

#print the elements of the following list using loop [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print (i)


#search for a number x =36 in this tuple using loop [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
x=36
idx=0
for i in nums :
    if (i==x):
        print ("found x at index",idx)
    idx+=1
    
     
