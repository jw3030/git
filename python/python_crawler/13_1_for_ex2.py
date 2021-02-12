for num in range(0, 10):
    print(num)

# 0, 1, 2, 3, 4 ...
# 1, 3, 5, 7, 9 ...
def printNum(num):
    print("fn=>", num * 2 + 1)

for num in range(0, 100):
    printNum(num)