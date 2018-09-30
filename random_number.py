import random

rval = random.randint(1,1000)
print(rval)

if random.randint(1,1000) < 19:
    print("value is less than 19")
elif rval > 19 and rval < 5000:
    print("value in 20-5000")
else:
    print("other range")

user = input("Enter your name:")

print(user.upper())
