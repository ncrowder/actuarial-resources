from scipy.stats import uniform
from statistics import mean
from statistics import median
import matplotlib.pyplot as plt

Maxs = []
MeansMaxs = []
Mins = []
MeansMins = []
Medians = []
MeansMeds = []

print("This program finds the average lifespan of first and last fatality of a group of individuals whose remaining lifespans are modeled by a uniform distribution. \n\n")
number = int(input("Analyzing groups of what maximum size? "))
trials = int(input("How many trials do you want to simulate? "))
span = int(input("Input the life span, where remaining remaining life span of all members in the group will be uniform through this value: "))

for peeps in range(1, number+1):
    for num in range(trials):
        r = uniform.rvs(size=peeps, loc=0, scale=span)
        Maxs.append(max(r))
        Mins.append(min(r))
        Medians.append(median(r))
    MeansMaxs.append(round(mean(Maxs),1))
    MeansMins.append(round(mean(Mins),1))
    MeansMeds.append(round(mean(Medians),1))

print("Mean time of first fatality (position in list equals group size: \n", MeansMins)
print("Mean time of last survivor (position in list equals group size: \n", MeansMaxs)

for peeps in range(number):
    minpoints = zip(range(1,number+1),MeansMins)
    maxpoints = zip(range(1,number+1),MeansMaxs)
    
print(list(minpoints))
print(list(maxpoints))


x = plt.scatter(list(range(1,number+1)), MeansMins, color='r')
y = plt.scatter(list(range(1,number+1)), MeansMaxs, color='b')
plt.xlabel('Group size')
plt.ylabel('Time of survival')
title = 'First Fatality & Last Survivor, X ~ U[0,' + str(span) + ']'
plt.title(title)
plt.legend((x, y), ('First to go', 'Last to make it'), fontsize=8)
plt.show()

