# mypy: ignore-errors


# iterate through a list
l = [1, 2, 3, 6, 3423]
print("------------------")
print("LIST ITERATION")
for val in l:
    print(val)

# list comprehension
print("------------------")
print("LIST COMPREHENSION")
double = [2 * val for val in l]
for val in double:
    print(val)

print("------------------")
print("LIST ENUMERATION")

print("------------------")
print("TUPLES VS LISTS")
# tuples vs lists
t = (1, 3, 4)
# t.append(5) # this will throw an error!!!!
# t[1] = 0  # this will throw an error!!!
print(t[2])

print("------------------")
print("SPREAD OPERATOR")

t = (5, 6, 3, 2, 1, 54)
x1, x2, *x3, x4 = t
print(x1, x2, x3, x4)

print("------------------")
print("ENUMERATION")

for i, val in enumerate(t):
    print(i, val)


print("------------------")
print("DICTIONARIES")

d = {"BMW": "German", "Ford": "USA", "Toyata": "Japan"}
print("KEYS", d.keys())
print("VALUES", d.values())
print("LENGTH", len(d))
print("BMW", d["BMW"])
print(".get()", d.get("Mitsubishi", "default"))


print("------------------")
print("SETS")
s = {4, 65, 2, 1, 1, 1, 1, 1}
print(s)
s2 = {3}
print(s.union(s2))
# print(s[2]) # this will error!!!
print(3 in s)
print(3 in s2)
