# plus minus multiple divide 을 return하는 함수
def getFourOperations(val1, val2):
    plusResult = val1 + val2
    minusResult = val1 - val2
    multipleResult = val1 * val2
    divideResult = val1 / val2
    return {"plus":plusResult, "minus":minusResult,
            "multiple":multipleResult, "divide":divideResult}


result = getFourOperations(10,20)
print(result)