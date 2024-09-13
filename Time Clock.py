time = int(input("Enter the time:"))

if(time <= 12):
  print("Good Morning")

elif(time > 12 and time <= 17):
  print("Good Afternoon")

elif(time >17 and time <=20):
  print("Good Evening")
  
elif(time >20 and time <=24):
  print("Good Night")
  
else:
  print("Invalid Time")
