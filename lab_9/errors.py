try:
    l = []
    print(l[21923712])
except IndexError as e:
    print("Index Error",e)
except Exception as e:
    print("Default Exception", e)
    
    
def ln(x):
    from math import log
    assert x > 0, "Error: ln only exists across (0,inf)"
    return log(x)

try:
    print(ln(32312))
    ln(-1)
except AssertionError as e:
    print(e)