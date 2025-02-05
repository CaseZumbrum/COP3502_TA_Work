# # voids
# def print_with_exclamations(str):
#     print(str + "!!!!")


# print_with_exclamations("test")

# print(print_with_exclamations("hmm"))


# # ------------------------
# # returns
# def exponentiate(base, exponent):
#     return base**exponent


# print(exponentiate(2, 3))

# # ------------------------
# # vars dont change (copied)
# def add_one_pt_2(x):
#     x = x + 1


# x = 4
# print(add_one_pt_2(x))
# print(x)

# # ------------------------
# # functions as variables
# def func(x):
#     return 2 * x


# x = func
# print(x(3))

# # ------------------------
# # returning several things
# def tup_func(x):
#     return x, -1 * x


# print(tup_func(3))

# # ------------------------
# # defaults
# def default_func(x, y, z = 3):
#     return x + y + z

# print(default_func(1,2))
# print(default_func(1, y=2, z=4))
# print(default_func(x = 1, 3, 3))


# # arguments
# def argument_func(*args, **kwargs):
#     for k, v in kwargs.items():
#         print(f"{v}: {k}")
#     for arg in args:
#         print(arg)


# argument_func(1, 2, 3, x=2, y=3)
