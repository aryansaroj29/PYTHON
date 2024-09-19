POSITIVE INDEX - 
marks = [3, 5, 6, "Aryan", True]     #List Function any Datatupes use str, int, boolean
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

NEGATIVE INDEX - 
print(marks[-3]) # Negative index
print(marks[len(marks)-3])  # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

Check whether an item in present in the list?
if "Aryan" in marks:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
if "rya" in "Aryan":
  print("Yes")
else:
  print("No")

All elements check or not 
print(marks)
print(marks[:])
print(marks[1:8])
print(marks[1:8:2])

List Comprehension - 
  
lst = [i*i for i in range (10)]
print(lst)

lst =[i*i for i in range (10) if i%2==0]
print(lst)
