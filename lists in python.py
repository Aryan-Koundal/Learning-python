marks = [87,89,33]
print (marks)
print(len(marks))
print (marks[0])
student = ["aryan",17,"himachal pradesh",176001]
student[0]="kaku"
print(student)
print (student[1:3])
student.append("got 84.4%")
print (student)

#sorting
marks = [8,2,5,7,4,2,0,9,6,5]
marks.sort()
print (marks)
marks.sort(reverse=True)
print (marks)

#reverse
marks=[2,4,6,2,4,5]
marks.reverse()
print (marks)

#insert
marks = [1,2,4,5,7,]
marks.insert(1,8)
print (marks)

#pop
marks = [1,2,3,4]
marks.pop(2)
print (marks)

#remove 
marks = [5,6,8,2,6,8]
marks.remove(6)
print (marks)