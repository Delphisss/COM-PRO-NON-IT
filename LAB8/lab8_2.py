def your_graphic(w, c1, c2):
    for i in range(int(w)):
        for j in range(int(w)):
            if i == 0 or i == int(w) - 1 or j == 0 or j == int(w) - 1:
                print(c1, end='')
            else:
                print(c2, end='')
        print()

size = input('Enter your graphic size:')
g1 = input('Enter first character:')
g2 = input('Enter second character:')

your_graphic(size, g1, g2)
