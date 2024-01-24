result = dict()
subject = ["CHEM", "AB", "BC"]

for each in subject:
    result[each] = list()

print(result)
chemList = ["우영", "환민", "대주", "예성", "윤재"]
# result['CHEM'].append("우영")
for each in chemList:
    result["CHEM"].append(each)

print(result)

for each in result["CHEM"]:
    print(each)