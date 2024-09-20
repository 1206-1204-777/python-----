import random

pl_pos = 1
com_pos = 1
def banmen():
    print("・"*(pl_pos-1) + "P" + "・"*(30-pl_pos)  + "Goal")
    print("・"*(com_pos-1) + "C" + "・"*(30-com_pos) + "Goal")

banmen()
print("Start!!")

while True:
    input("enterでPが前進します")
    pl_pos = pl_pos + random.randint(1,6)
    if pl_pos > 30:
        pl_pos = 30
    banmen()
    if pl_pos == 30:
        print("Victory!")
        break
    input("enterでCが前進します")
    
    com_pos = com_pos + random.randint(1,6)
    if com_pos > 30:
        com_pos = 30
    banmen()
    if com_pos == 30:
        print("Loser")
        break
    