print("Hello!!")
print("What is your name? ")
myName = input()
print("It is very nice to meet you, " + myName)
print("How old are you " + myName + "?")
myAge = input()
print("WOW! You are " + myAge + " years old!")
print("Your name is this long :")
print(len(myName))

print("What is your favorite food?")
userinput = input()
print("I like " + userinput + " as well!! YUMMY!")

if int(myAge) < 20:
    print("I like that you are young! Wanna go on a date?")
else:
    print("Wanna date? Youre old enough right?")
