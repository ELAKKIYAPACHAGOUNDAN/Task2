def addition(first,second):
    print("Result for Addition: ")
    return first + second
def subtraction(first,second):
    print("Result for Subtraction: ")
    return first - second
def multiplication(first,second):
    print("Result for Multiplication: ")
    return first * second
def division(first,second):
    if second == 0:
        print("Cannot Divide")
    else:
        print("Result for Division: ")
        return first / second
n1 = int(input("First Number: "))
n2 = int(input("Second Number: "))
print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
choice = input("Select your Choice: ")
if choice == "1":
    add = addition(n1,n2)
    print(add)
elif choice == "2":
    sub = subtraction(n1,n2)
    print(sub)
elif choice == "3":
    mul = multiplication(n1,n2)
    print(mul)
elif choice == "4":
    div = division(n1,n2)
    print(div)
else:
    print("Select the correct choice")
    
