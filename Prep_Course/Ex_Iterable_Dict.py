books = {
    '1984': 'George Orwell',
    'Brave New World': 'Aldous Huxley',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}

print(books['1984'])  # Output: George Orwell

books['The Great Gatsby'] = 'Francis Scott Fitzgerald'
print(books['The Great Gatsby'])

#new book
books['Moby Dick'] = 'Herman Melville'
print(books)

#Use the get() method to try to access the author of "To Kill a Mockingbird".
print(books.get('To Kill a Mockingbird'))

books.pop("Brave New World")
print(books)
