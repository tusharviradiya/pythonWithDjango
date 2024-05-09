# dict
# dict is class
# dict is iterable
# dict is mutable
# dict is not sequence
# dict is pair of key and value

# how to create dict
d1 = {"name": "tushar", "age": 21, "city": "pune"}
d2 = {}

print(d1);
print(d1.keys())
print(d1.values())
print(d1.items())

# dict comprehension
d3 = {k: v * 2 for k, v in d1.items()}
print(d3)