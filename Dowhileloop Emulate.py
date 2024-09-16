i = 0
while True:
  print (i)
  i = i + 1
  if(i%100 == 0):
    break

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
