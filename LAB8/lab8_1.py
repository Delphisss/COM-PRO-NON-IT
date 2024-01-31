def minimum(numbers):
    return min(numbers)

def maximum(numbers):
    return max(numbers)

def main():
    data = []
    i = 0
    print("Enter numbers below. Enter -1 to finish inserting numbers.")
    while True:
        value = float(input(f"data[{i}] =  "))
        i = i+1
        if value == -1:
            break
        
        data.append(value)

    if data:
        min_num = minimum(data)
        max_num = maximum(data)
        
        print(f"Minimum number: {min_num}")
        print(f"Maximum number: {max_num}") 
    else:
        print("No data entered.")

main()
