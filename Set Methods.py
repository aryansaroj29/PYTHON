s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s2.union(s1))
s1.update(s2)
print(s1,s2)

# union() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

# update() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)

# intersection() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

# intersection_update() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

# symmetric_difference() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# symmetric_difference_update() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

# difference() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

# difference_update() -

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))

# isdisjoint():

cities1 = {"Mumbai", "Delhi", "Bangalore", "Chennai"}
cities2 = {"Delhi1", "Kolkata", "Hyderabad", "Mumbai1" }
print(cities1.isdisjoint(cities2))

# issuperset():

cities  = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA" }
cities2 = {"KOLKATA", "HYDREABAD", "CHENNAI"}
print(cities.issuperset(cities2))
citites3 = {"MUMBAI", "DELHI", "BANGLORE"}
print(cities.issuperset(citites3))

# issubset():

cities  = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
cities2 = {"KOLKATA", "HYDREABAD", "CHENNAI"}
print(cities.issubset(cities2))
cities3 = {"MUMBAI", "DELHI", "BANGLORE",}
print(cities3.issubset(cities))

# add():

cities  = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
cities.add("CHENNAI")
print(cities)

# update():

cities  = {"MUMBAI", "DELHI", "BANGLORE"}
cities2 = {"KOLKATA", "HYDREABAD", "CHENNAI"}
cities.update(cities2)
print(cities)

# remove():

cities  = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
cities.remove("MUMBAI")
print(cities)

# discard():

cities  = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
cities.discard("MUMBAI12")
print(cities)

# pop():

cities  = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
item= cities.pop()
print(cities)
print(item)

# del():

cities   = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
cities2  = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
del cities
print(cities2)

# clear():

cities   = {"MUMBAI", "DELHI", "BANGLORE", "KOLKATA"}
cities.clear()
print(cities)

# Check if item exists:

info = {"Aryan", 19 , False, 19.5}
if "Aryan" in info:
  print("Aryan is present")
else:
  print("Aryan is absent")
  
