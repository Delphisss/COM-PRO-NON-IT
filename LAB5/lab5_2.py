books = [['Accounting', 'Psychology'], 
         ['John Lee', 'Jason Hart'], 
         [2019, 2020], [29.50, 19.99]]

# Get new book information from the user
new_title = input("Enter a new book's title: ")
new_author = input("Enter a new book's author: ")
new_year = int(input("Enter a new book's year: "))
new_price = float(input("Enter a new book's selling price: "))

# Add the new book information to the respective lists
books[0].append(new_title)
books[1].append(new_author)
books[2].append(new_year)
books[3].append(new_price)

# Display the updated books' information
print("Updated books' titles:")
print(books[0])

print("\nUpdated books' authors:")
print(books[1])

print("\nUpdated books' years:")
print(books[2])

print("\nUpdated books' selling prices:")
print(books[3])
