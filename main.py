#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
final_bill = input("What is your final bill? ")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
bill_split = input("How many people to split the bill? ")
percentage_tip_amount = (float(percentage_tip) / 100) * float(final_bill)
bill_split_amount = int(bill_split)
pay =  (float(final_bill) + percentage_tip_amount) / bill_split_amount
final_pay = "{:.3f}".format(pay)

print(f"Each person should pay {final_pay}")
