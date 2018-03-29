def add (x, y):
  return x + y

def subtract (x, y):
  return x - y 
  
def multiple (x, y):
  return x * y

def divide (x, y):
  return x / y
  
def start():
  print ('Enter a number to go to that option')
  print ('Please select an option.')
  print ('')
  print ('1) Addition')
  print ('2) Subtraction')
  print ('3) Multiplication')
  print ('4) Division')
  choice = input ('Enter choice (1/2/3/4)')
  
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  
  if choice == '1':
     print(num1,"+",num2,"=", add(num1,num2))
  
  elif choice == '2':
     print(num1,"-",num2,"=", subtract(num1,num2))
  
  elif choice == '3':
     print(num1,"*",num2,"=", multiple(num1,num2))
  
  elif choice == '4':
     print(num1,"/",num2,"=", divide(num1,num2))
  else:
     print("Invalid input")
     
  choice2 = input('Wanna go back to menu or quit?')
  if choice2 == 'menu':
    start()
  else:
    print('Okay goodbye!')
start()