#expected probability of LMOA
import random
import matplotlib as plt
import matplot.mlab as mlab
turns = []
counts = 1
x = 10
for i in range(x):
    test = []
    while True:
        test.append(random.randint(1, 4))
        counts += 1
        print(counts)
        if len(set(test)) >= 4:
            turns.append(len(test))
            break
print(turns)
average = sum(turns)
average = average/x
print(average)
medcount=0
for t in turns:
    if t > 6:
        medcount+=1

print(medcount)
print(medcount/x)
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()