#calculator linked to vs code
#calculator using functions and loop
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
def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        return None, None
while True:
    print("--- Simple Calculator---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=input("Enter your choice(1-5):")

    if choice=="5":
      print("calculator closed")
      break
    if choice in["1","2","3","4"]:
        num1, num2 = get_numbers()
        if num1 is None:
            continue

        
        if choice =="1":
          print("Result:", add(num1,num2))
        elif choice =="2":
          print("Result:", subtract(num1,num2))  
        elif choice =="3":
          print("Result:", multiply(num1,num2)) 
        elif choice =="4":
          print("Result:", divide(num1,num2))
    else:
        print("invalid choice. Please try again.")
        
          
        
    
