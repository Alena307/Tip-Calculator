
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator of Alena! :-)")
input1 = input("What was the total bill?")
print(input1)
input2 = input("How much tip would you like to give? 10, 12, or 15?")
print(input2)
input3 = input("How many people to split the bill?")
print(input3)
input4 = float(input1) * float(input2) / 100
input5 = ((float(input1) + float(input4)) / float(input3))
result = round(input5,2)
print("Everyone should pay " + str(result) + " Euros.")

