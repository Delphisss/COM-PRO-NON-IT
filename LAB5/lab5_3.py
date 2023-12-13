books = [['Accounting', 'Psychology', 'Harry Potter'], 
         ['John Lee', 'Jason Hart', 'J. K. Rowling'], 
         [2019, 2020, 2021], [29.50, 19.99, 50.25]]

print("Books' titles:")
print(books[0])

sold_book_title = input("Enter sold book's title: ")
index = books[0].index(sold_book_title)
books[0].pop(index)  # Remove title
books[1].pop(index)  # Remove author
books[2].pop(index)  # Remove year
books[3].pop(index)  # Remove price

print("\nUpdated books' titles:")
print(books[0])

print("\nUpdated books' authors:")
print(books[1])

print("\nUpdated books' years:")
print(books[2])

print("\nUpdated books' selling prices:")
print(books[3])
