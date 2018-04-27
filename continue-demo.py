values = [1, 4, 0, 8, 0]

data = 1

for x in values:
    if x == 0:
        # If x is zero stop this iteration and continue with next
        continue
    data = data * x

print("Result is ", data)
