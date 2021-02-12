def f(x):
    return x + 1
def g(x):
    return x / 2
# g o f(X)
# g o f(10) = ?

resF = f(10)
resG = g(resF)
print(resG)

result = g(f(10))