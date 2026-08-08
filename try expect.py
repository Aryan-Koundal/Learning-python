try:
  x = int(input("entre a integer"))
  print(x)
except ValueError:
  print("That is not an integer, entre a valid integer")
else:
  print("nothing is wrong")
finally:
  print("checked evrrything")