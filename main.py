# Take the necessary inputs
print("Welcome to Tip Calculaor!")
bill = float(input("What is the total bill? $"))
rate = float(input("What percent tip will you like to give? "))
num = int(input("How many members you want to split? "))

#Calculate the pay for each person
each_pay = (bill / num) * (1+(rate/100))

#Print amount rounded off with 2 decimals
print("Each person should pay: $", round(each_pay,2))
