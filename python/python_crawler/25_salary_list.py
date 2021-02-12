# 연봉 = 연차 * 900만원
def getSalary(year):
    return year * 9_000_000

years = [7, 3, 4, 6,1] # => 63, 29, 36, 54

def getResult(year):
    salaryList = []
    for year in years:
        salary = getSalary(year)
        salaryList.append(salary)
    return(salaryList)


result = getResult(years)
print(result)