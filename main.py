# Take the necessary inputs
print("Welcome to Tip Calculaor!")
bill = float(input("What is the total bill? $"))
rate = float(input("What percent tip will you like to give? "))
num = int(input("How many members you want to split? "))

#Calculate the pay for each person, round off to 2 decimal places
each_pay = (bill / num) * (1+(rate/100))
final_amt = round(each_pay, 2) 

#Print amount with 2 decimal places on each case
print("Each person should pay: ${:.2f}".format(each_pay))
