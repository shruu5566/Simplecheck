#calculator linked to vs code
#calculator using functions and loop
import math

def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if b!=0:
    return a/b
  else:
    return  "❌ Error: Division by zero is not allowed"


def power(a, b):
    return a ** b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "❌ Error: Cannot find square root of a negative number"

def get_two_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return None, None
def get_one_number():
    try:
        return float(input("Enter number: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        return None

while True:
    print("--- Simple Calculator---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    choice=input("Enter your choice(1-7):")

    if choice=="7":
      print("calculator closed")
      break

    if choice == "6":
        num = get_one_number()
        if num is None:
            continue
        print("Result:", square_root(num))
        continue

    if choice in["1","2","3","4","5","6"]:
        num1, num2 = get_two_numbers()
        if num1 is None:
            continue
        if num1 is None or num2 is None:
            continue
        

        if choice =="1":
          print("Result:", add(num1,num2))
        elif choice =="2":
          print("Result:", subtract(num1,num2))  
        elif choice =="3":
          print("Result:", multiply(num1,num2)) 
        elif choice =="4":
          print("Result:", divide(num1,num2))
        elif choice == "5":
          print("Result:", power(num1, num2))

    else:
        print("invalid choice. Please try again.")
        
          
        
    
