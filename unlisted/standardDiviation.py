import math
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
mean = sum(players) / len(players)
varienceSum = 0
counter = 0
for i in players:
    varience = (i - mean)**2
    varienceSum += varience
    stdiv = math.sqrt(varienceSum / len(players))
for j in players:
    if j < (mean + stdiv) and j > (mean - stdiv):
        counter += 1
print(f"\
        The MEAN:{mean}\n\
        The Standard Deviation:{stdiv}\n\
        Min Stdiv: {mean - stdiv}\n\
        Max StDiv: {mean + stdiv}\n\
        How Many fall into range: {counter}")