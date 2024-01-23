height = int(input("Give your height in cm: "))

if height >= 120:
    age = int(input("Enter your age: "))
    if age<12:
        print("Your ticket price $5")
    elif age<=18:
        print("Your ticket price $7")
    else:
        print("Your ticket price $12")
else:
    print("You can't ride.")
    