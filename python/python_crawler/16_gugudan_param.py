# n단
def printNDan(dan):
    for num in range(1, 9 + 1):
        st = "{} * {} = {}".format(dan, num, dan * num)
        print(st)
    print("------")
printNDan(3)
printNDan(4)
printNDan(5)

# 100단
for dan in range(2, 100 + 1):
    printNDan(dan)