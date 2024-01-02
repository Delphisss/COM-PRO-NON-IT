number=0
data=[number]
i=0
while(number!=-1):
  number = int(input("data[{}]".format(i)))
  if(number==-1):
    data.append(float(input("data[{}]:".format(i))))
  i+=1
print(data)
print("Total sum: {a:.2f}".format(a=sum(data)))
print("Average : {a:.2f}".format(a=(sum(data)/len(data))))