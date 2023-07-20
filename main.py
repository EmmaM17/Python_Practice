#Minutes to seconds
def Min_2_Sec():
  min = int(input("Please enter the number of minutes: "))
  sec = min * 60
  print(sec, " Seconds")


#Hours to seconds
def Hours_2_Sec():
  hours = int(input("Please input the number of hours: "))
  print((hours * 60) * 60, " Seconds")


#A basic calculator
def calculator():
  num1 = int(input("Please enter your first number: "))
  operator = input("Please enter your operator (* / + -): ")
  num2 = int(input("Please enter your second number: "))

  if operator == '*':
    answer = num1 * num2
  elif operator == '/':
    answer = num1 / num2
  elif operator == '+':
    answer = num1 + num2
  elif operator == '-':
    answer = num1 - num2
  else:
    answer = 'error'
  print(answer)
