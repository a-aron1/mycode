secret_num = 42

guess = int(input("What is the magic number?"))

if secret_num == guess:
    print("Correct!")
elif secret_num-5 < guess < secret_num+5:
    print("Close!")

else:
    print("Sorry, youre out of luck today!")
