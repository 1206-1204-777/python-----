import random
import datetime
ALP = ["A","B","C","D","E","F","G"]
r = random.choice(ALP)
st = datetime.datetime.now()
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)

ans = input("抜けているのは？")
if ans == r:
    print("Correct")
    et = datetime.datetime.now()
    print(str((et-st).seconds)+ "秒でした")
else:
    print("no")