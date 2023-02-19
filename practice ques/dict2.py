# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# dict[1]=4

# print(dict)
# print(dict[1])
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], "sed": ["Steak","spanddy"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

c=order.values
print(c)
for i in order.keys():
    print(i)

#  .keys() to get keys () for the function 
#  to access we dont use indexing we use keys 
