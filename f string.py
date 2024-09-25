letter = "Hey My name is {1} and I am from {0}"
name = "Aryan"
country = "India"

print(letter.format(country, name))

print(f"Hey My name is {name} and I am from {country}")

print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price=40.09999
txt = f"For only {price:.2f} dollar!"
print(txt)
# print(txt.fromat())

print(type( f"{2*30}"))
