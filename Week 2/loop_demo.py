


sum = 0
for i in range(2, 10):
    for j in range(i, 5):
        sum += j
print("DEMO 1: " + str(sum))


x = 10
while x < 30:
    x += 10
print("DEMO 2: " + str(x))


count = 0
for i in range(0,10,2):
    if(i%2 == 1):
        break
    elif(i == 6):
        continue
    count += 2
print("DEMO 3: " + str(count))



