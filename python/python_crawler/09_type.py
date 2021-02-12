val1 = 1 # 숫자형
print(val1)

val2 = "1" # 문자열
print(val2)

print(val1 + 20) #21
# print(val2 + 20) # 21? 에러
print(type(val2))
print(int(val2) + 20)

# 숫자형을 문자열로
print(val2 + str(20))
result = val2 + str(20)
print(result) #120
print(result + "40")
# 숫자형으로
print(int(result) + int("40"))