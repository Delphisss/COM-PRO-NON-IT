data = []
i = 0
num = float(input("data[{}] = ".format(i)))
data.append(num)

while num != -1:
    i += 1
    num = float(input("data[{}] = ".format(i)))
    data.append(num)

data.pop()
print("{}".format(data))
print("Totla sum: {}".format(sum(data)))
print("Average: {}".format(sum(data)/len(data))) 