print ("Version 3.2 of HOMEMADE CALCULATOR")
print ("Hi!")
repeat = "yes"
while repeat == "yes":
  x = int (input ("Type in the first number you want to caluculate:"))
  y = int (input ("Type in the second number that you want to calculate:"))
  sign = input ("Type in if you want to multiply, divide, add, or subtract the two numbers. * means multiplication, + means addition, / means division, and - means subtraction: ")
  if sign == "*":
   ans = x*y
   print ("The answer is " + str(ans))
  elif sign == "/":
   ans = x/y
   print ("The answer is " + str(ans))
  elif sign == "+":
   ans = x+y
   print ("The answer is " + str(ans))
  elif sign == "-":
    ans = x-y
    print ("The answer is " + str(ans))
  else:
   print ("Wrong operation. Please try again. Sorry!")
  repeat = input ("Do you want to use the calculator again? (Type yes or no ONLY)")  
print ("Okay, then. Goodbye!")
#Cool, right?