DEFAULT ARGUMENTS :


def average(a=9, b=1):
  print("The average is", (a + b) /2)

average(b=9)

def name (fname, mname = "Amarjeet", sname = "Saroj"):
  print("Hello",fname, mname, sname)

name("Aryan")


KEYWORD ARGUMENTS :


def average(a=9, b=1):
  print("The average is", (a + b) /2)

average(b=9, a=21)

def name (fname ,mname, lname):
  print("Hello",fname, mname, lname)

name(lname="Saroj",fname= "Aryan",mname= "Amarjeet")

REQUIRED ARGUMENTS :


def average(a, b, c=1):
  print("The average is", (a + b + c) /2)

average(5, 6)

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")  #its wrong code  

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")

VARIABLE-LENGTH ARGUMENTS :


def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum / len(numbers))

average(5, 6, 4, 7)







