
rent = int(input("Enter your hostel/flat rent: "))
food = int (input("Enter the amount of food ordered: "))
electricity_spend  = int( input ("Enter the total of electricity spend: "))
charge_per_unit = int(input("Enter the number of persons per unit : "))
persons = int(input ("Enter the number of persons living in  room/flat: "))

total_bill = electricity_spend * charge_per_unit


out_put = (rent + food + total_bill)  // persons


print (f"Each persons will pay {out_put}")