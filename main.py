# 1) Min_2_Sec()
# 2) Hours_2_Sec()
# 3) First_item()
# 4) Calculator()
# 5) Number_2_Binary()


#Minutes to seconds
def Min_2_Sec():
  min = int(input("Please enter the number of minutes: "))
  sec = min * 60
  print(sec, " Seconds")


#Hours to seconds
def Hours_2_Sec():
  hours = int(input("Please input the number of hours: "))
  print((hours * 60) * 60, " Seconds")


#Get first item from a list
def First_item():
  lst = input("Please enter a list seperated by a comma: ")
  lst = lst.split(",")
  print(lst)


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


#Number to binary
def num2bin():
  number = int(input("Please enter your number: "))
  if number > 255 or number < 0:
    print("Error")
    num2bin()

  binary = ''

  if number >= 128:
    number = number - 128
    binary = binary + '1'
  else:
    binary = binary + '0'

  if number >= 64:
    number = number - 64
    binary = binary + '1'
  else:
    binary = binary + '0'

  if number >= 32:
    number = number - 32
    binary = binary + '1'
  else:
    binary = binary + '0'

  if number >= 16:
    number = number - 16
    binary = binary + '1'
  else:
    binary = binary + '0'

  binary = binary + ' '

  if number >= 8:
    number = number - 8
    binary = binary + '1'
  else:
    binary = binary + '0'

  if number >= 4:
    number = number - 4
    binary = binary + '1'
  else:
    binary = binary + '0'

  if number >= 2:
    number = number - 2
    binary = binary + '1'
  else:
    binary = binary + '0'

  if number >= 1:
    number = number - 1
    binary = binary + '1'
  else:
    binary = binary + '0'

  print(binary)
