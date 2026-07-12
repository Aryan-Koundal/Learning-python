student = {
    "name" : input("entre your name"),
    "class" : input ("entre your class"),
    "roll no." :input ("entre your roll no."),
    "marks" : []
}
subject = ["maths","english","hindi","dbms","eco"]
for i in range(5) :
    mark = int(input(f"enter marks of {subject[i]} :"))
    student["marks"].append(mark)

print("Marks :", student["marks"])

student["name"]="aryan"
print (student["name"])
null =  {}
print (null)

student = {
    "name ": input("entre your name"),
    "class": input ("entre your class"),
    "roll no." : input ("entre your roll no."),
    "subjest": {
        "english": input ("entre marks of english"),
        "maths": input ("entre marks of math"),
        "econimics": input ("entre marks of economics")
    }
}
print (student["subjest"]["english"])
student = {
    "name ": "aryan" ,
    "class": 1,
    "roll no." : 50,
    "subjest": {
        "english": 88,
        "maths": 98,
        "econimics":88
    }
}
print (len (list(student.keys())))
print (student.values())
print (student.items())
pairs = list(student.items())
print (pairs[1])
print (student.get("name"))
student.update({"age":18})
print (student)