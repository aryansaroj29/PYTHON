def calculateGmean(a , b):
  mean = (a * b) / (a + b)
  print(mean)

def isgreater(a ,b):
  if(a > b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def islesser(a , b): 
  pass               #NO ERROR IN PASS KEYWORD
    
a = 9
b = 8
isgreater(a , b)
# if(a > b):
#   print("First number is greater")
# else:
#   print("Second number is greater or equal")
# gmean1 = (a * b) / (a + b)
# print(gmean1)
calculateGmean (a , b)

c = 8
d = 74
isgreater(c , d)
# if(c > d):
#   print("First number is greater")
# else:
#   print("Second number is greater or equal")
# gmean2 = (c * d) / (c + d)
# print(gmean2)
calculateGmean (c , d)
