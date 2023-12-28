import random as r
cnumber=r.randrange(1,101)
userinput=int(input("enter your number :"))
print("computer number", cnumber)
if userinput>cnumber:
  print("your guess number is high", userinput)
elif userinput<cnumber:
  print("computer guess number is high", cnumber)
else:
  print("your number us equal")
