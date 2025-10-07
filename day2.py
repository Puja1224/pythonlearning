# sum , difference , product and division of two numbers

#taking input from user
num1=float(input("enter first number - "))
num2=float(input("enter second number - "))

#performing operations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:   
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)" 

#displaying results
print("the sum of two numbers is - " , sum)
print("the difference of two numbers is - " , difference)
print("the product of two numbers is - " , product)
print("the division of two numbers is - ", division )