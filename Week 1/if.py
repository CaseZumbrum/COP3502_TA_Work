t = True
f = False
x = 1
y = 2



# general syntax
if t:
    print("since t is true, this is printed")


if f:
    print("since f is false, this will never be printed")


# equality
if x == 1:
    print("since x is 1, this will be printed")


# not equal
if y != 10000:
    print("y is not 1000, so this is printed")

# parentheses are a choice
if (t):
    print("we can use parantheses to make code clear sometimes!!")


# else if structure
if(True): # we can use immediates here
    print("wow the first statement was true!!!")
elif(False):
    print("wow the second statement was true!!!")
else:
    print("neither statement was true :(")


# in line
print("the inline if statement was true!!") if y > x else print("the inline if was false")


# Nesting!
if x % 2 == 1: # what is this really saying???
    if y % 2 == 1:
        print("wow both levels were true")
    else:
        print("only the outer was true, but the inner was false")


# Boolean operators

print("True and False == True") if (True and False) else print("True and False == False")

print("not False == True") if (not False) else print("not False == False")