# getSalary() 연봉구하기 -> 연차 * 900만원
# getVAT() 부가가치세 -> money * 0.1
# 내 연봉에 대한 부가가치세가 얼마인지?
def getSalary(year):
    return year * 9_00_000

def getVAT(money):
    return money * 0.1

mysalary = getSalary(7)
myVAT= getVAT(mysalary)
print(myVAT)

# g o f () -> getVAT o getSalary(7)
print(getSalary(7))
