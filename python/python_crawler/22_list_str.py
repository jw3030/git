names = ["kyengrok", "nana", "mimi"]
print(names)

# 번호로 꺼내기
print(names[0]) # 인덱스는 0부터 시작
print(names[1])

names = ["kyengrok",
         "nana",
         "mimi",
         "mingming"
         ]
for name in names:
    print(name)

# printHello(name)
def printHello(name):
    message = "{} hello!".format(name)
    print(message)

printHello(names[0])
printHello(names[2])

for name in names:
    printHello(name)