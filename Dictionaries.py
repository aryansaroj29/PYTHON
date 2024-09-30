dic = {
  567 : "Aryan",
  123 : "Yash",
  456 : "Chinmay"
}
print(dic[567])



info = {"Name": "Aryan", "Age": 20, "Eligible": True}
print(info)
print(info["Name"])
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value of correspondence of the key {key} is {info[key]}")



# Accessing single values:

info = {'name': "Aryan", 'age': 20, 'eligible': True}
print(info)
print(info['name'])
print(info.get('eligible'))

# Accessing multiple values:

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# Accessing keys:

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# Accessing key-value pairs:

info = {"Name": "Aryan", "Age": 20, "Eligible": True}
print(info.items())
for keys, value in info.items():
  print(f"The value of corresponding to the key {keys} is {value}")
