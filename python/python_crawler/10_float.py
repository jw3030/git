# float 소수점
val1 = 0.1
val2 = 0.2
print(type(val1), type(val2))
print(type(1), type(2)) # 정수 integer

def divide(val1, val2):
    print("=>", type(val1), type(val2))
    result = val1 / val2
    print(result, type(result))
divide(10,20)