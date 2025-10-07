# calculator 

#input from user
num1=float(input("enter first number - "))
num2=float(input("enter second number - "))
operation=input("enter operation (+, -, *, /) - ")
#performing operations based on user input
if operation=='+':
    result=num1+num2
    print("the result is - ", result)       
elif operation=='-':
    result=num1-num2
    print("the result is - ", result)
elif operation=='*':
    result=num1*num2
    print("the result is - ", result)
elif operation=='/':
    if num2 != 0:   
        result=num1/num2
        print("the result is - ", result)
    else:
        print("error: division by zero is not allowed")


