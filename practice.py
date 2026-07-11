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