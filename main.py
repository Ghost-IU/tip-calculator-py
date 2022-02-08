#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What is the total bill? $"))
rate = float(input("What percent tip will you like to give? "))
num = int(input("How many members you want to split? "))

each_pay = (bill / num) * (1+(rate/100))

print("Each person should pay: $", round(each_pay,2))