data = []

user_input = float(input("Enter data[0]: "))
data.append(user_input)

user_input = float(input("Enter data[1]: "))
data.append(user_input)

user_input = float(input("Enter data[2]: "))
data.append(user_input)

user_input = float(input("Enter data[3]: "))
data.append(user_input)

user_input = float(input("Enter data[4]: "))
data.append(user_input)

print(f"data = {data}")

data_sum = sum(data)
data_max = max(data)
data_min = min(data)
data_avg = data_sum / len(data)

print(f"Sum = {data_sum:.2f}")
print(f"Maximum = {data_max:.2f}")
print(f"Minimum = {data_min:.2f}")
print(f"Average = {data_avg:.2f}")
