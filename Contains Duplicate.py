nums=[1,2,3,4,5,8,9,1,2]

seen=[]

for i in nums:
  if i in seen:
    print("true")
  else:
    seen.append(i)
    print("false")

print(seen)