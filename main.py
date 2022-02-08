
bill = float(input("What is the total bill? $"))
rate = float(input("What percent tip will you like to give? "))
num = int(input("How many members you want to split? "))

each_pay = (bill / num) * (1+(rate/100))

print("Each person should pay: $", round(each_pay,2))