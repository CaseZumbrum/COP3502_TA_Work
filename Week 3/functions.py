def print_with_exclamations(str):
    print(str + "!!!!")


print_with_exclamations("test")

# print(print_with_exclamations("hmm"))


def add_one(x):
    return x + 1


print(add_one(3))


def exponentiate(base, exponent):
    return base**exponent


print(exponentiate(2, 3))


def add_one_pt_2(x):
    x = x + 1


x = 4
print(add_one_pt_2(x))
print(x)
