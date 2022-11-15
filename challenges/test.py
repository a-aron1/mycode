age = int (input( "How old are you?"))

if age >= 30:
    print ("You're in your thirties.")
elif age >= 40:
  print("You're older than forty.")
else:
    print("Pfft. Youngster!")


# Question 1
greeting = {
0:"Hello!",
1:"Good",
2:"morning,",
3:"and welcome",
4:"back to class.",
}
for i in range(len (greeting)):
    print(greeting[i], end="")