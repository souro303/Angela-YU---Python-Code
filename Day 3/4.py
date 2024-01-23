height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in m: "))

bmi = round(weight/height ** 2)

if bmi < 18.5:
    print(f"your bmi are {bmi}, Your are under weight.")
elif bmi < 25:
    print(f"your bmi are {bmi}, Your have a normal weight.")
elif bmi < 30:
    print(f"your bmi are {bmi}, Your are over weight.")
elif bmi < 35:
    print(f"your bmi are {bmi}, Your are obese.")
else:
    print(f"your bmi are {bmi}, Your are clinically obese.")
