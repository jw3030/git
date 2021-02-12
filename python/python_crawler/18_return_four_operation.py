def plus(val1, val2):
    return val1 + val2

print(plus(10,20))

def minus(val1, val2):
    return val1 - val2

print(minus(10,20))

def multiple(val1, val2):
    return val1 * val2

print(multiple(10,20))

def divide(val1, val2):
    return val1 / val2

print(divide(10,20))

# (10 + 20) - ((30 * 40) / 50)
result1 = multiple(30,40)
result2 = divide(result1, 50)
result3 = plus(10,20)
finResult = result3 - result2
print(finResult)
