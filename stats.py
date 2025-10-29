import matplotlib.pyplot as plt
import statistics
def average(ls):
    count = len(ls)
    total = 0 
    for hr in ls:
        total = total + hr 
    return total/count
def above(ls,x):
    count = 0
    for hr in ls:
        if hr > x:
            count += 1
    return count/len(ls)
def median(ls):
    l = len(ls)
    if l % 2 == 0:
        mr = ls[l//2]
        ml = ls[mr-1]
        median = (mr-ml)/2
    else:
        median = ls[l//2]
    return median
fhand = open('StudentExercise.csv')
hrs= []
for line in fhand:
    words = line.split(",")
    try:
        hr = float(words[0])
    except:
        continue
    hrs.append(hr)
hrs.sort()
print(hrs)
plt.hist(hrs, bins = 6)
plt.ylabel("Count")
plt.xlabel("Hours")
plt.title("Hours of Exercise")
plt.show()
print(average(hrs))
print(above(hrs,average(hrs)))
print(median(hrs))
