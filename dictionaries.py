dict= {
    "name":"shahid",
    "age":"21",
    "roll":1
}
print(dict)
print(dict["name"])   #if key is not in dict show error
print(dict.get("name"))   # if key is not in dict show none nor error
print(dict.keys())       # show all the keys
print(dict.values())       # show all the values


for key in dict.keys():  #showing  all the values
    print(dict[key])


for key in dict.keys():    #show key and values both
    print(f"the value corresponding to the key {key} is {dict[key]}")


print(dict.items())
for key, value in dict.items():
    print(f"the value corresponding to the key {key} is {value}")
