print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like ot give? 10, 12 or 15? "))
people = int(input("How many people? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = round((total_bill / people),2)
print(f"Each person should pay : {bill_per_person}")