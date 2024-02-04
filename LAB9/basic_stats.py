# basic_stats.py
import math

def average(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    return s / len(x)

def std(x):
    avg = average(x)
    s = 0
    for i in range(len(x)):
        s += math.pow(x[i] - avg, 2)
    return math.sqrt(s / len(x)) 