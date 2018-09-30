

def is_mod_3(x):
    if x % 3:
        return False
    else:
        return True

def is_mod_5(x):
    #print(x%5)
    if x % 5:
        return False
    else:  
        return True

while True:
    try:
        inputval = int(input("Enter a number\n"))
        break
    except ValueError:
        print("invalid entry, re-enter")

print("Checking mod on your number:",inputval)

if is_mod_3(inputval) and is_mod_5(inputval):
    print("mod3 and mod5")
elif is_mod_5(inputval):
    print("mod5")
elif is_mod_3(inputval):
    print("mod3")
