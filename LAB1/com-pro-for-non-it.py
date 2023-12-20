books = [['Accounting','Psychology'],['John Lee','Jason Hart'],[2019,2020],[29.50,19.99]]
a = input("Enter a new book's title: ")
b = input("Enter a new book's author: ")
c = int(input("Enter a new book's year: "))
d = float(input("Enter a new book's selling price: "))

books[0].append(a)
books[1].append(b)
books[2].append(c)
books[3].append(d)

print('\nUpdated books'' titles:')
print(books[0],"\n")
print('Updated books'' authors:')
print(books[1],"\n")
print('Updated books'' years:')
print(books[2],"\n")
print('Updated books'' selling price:')
print(books[3])

print("\nbooks titles\n",books[0])
sold = input("\nEnter sold book's title:")

index_sold = books[0].index(sold)

books[0].pop(index_sold)
books[1].pop(index_sold)
books[2].pop(index_sold)
books[3].pop(index_sold)

print('\nUpdated books','title: ')
print(books[0],'\n')
print('\nUpdated books','author: ')
print(books[1],'\n')
print('\nUpdated books','years: ')
print(books[2],'\n')
print('\nUpdated books','selling price: ')
print(books[3])