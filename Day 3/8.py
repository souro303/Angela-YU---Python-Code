height = int(input("Give your height in cm: "))
bill = 0
if height >= 120:
    age = int(input("Enter your age: "))
    if age<12:
        print("Your ticket price $5")
        bill+=5
    elif age<=18:
        print("Your ticket price $7")
        bill+=7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. You have a free ride!")
    else:
        print("Your ticket price $12")
        bill+=12
        
    wants_photo = input("Do you want a photo taken? Y & N: ")
    if wants_photo == "Y":
        bill+=3
    print(f"Your total bill is {bill}")
else:
    print("You can't ride.")
    