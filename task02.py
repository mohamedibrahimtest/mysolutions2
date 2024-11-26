# List to represent the borrowing data
borrowings = [
    "The Lord of the Rings - 10",
    "Pride and Prejudice - 7",
    "The Hobbit - 8",
    "Pride and Prejudice - 5"
]

# Dictionaries and sets to store results
book_counts = {}
unique_books = set()

# Iterate over each borrowing
for borrowing in borrowings:
    # Split the borrowing string into book title and days
    book, days = borrowing.split(' - ')
    days = int(days)

    # Add the book to the set of unique books
    unique_books.add(book)

    # Update the book's count in the dictionary
    if book in book_counts:
        book_counts[book] += days
    else:
        book_counts[book] = days

# Find the most and least borrowed books
most_borrowed_book = max(book_counts, key=book_counts.get)
least_borrowed_book = min(book_counts, key=book_counts.get)

# Calculate the average borrowing time
total_days = sum(book_counts.values())
average_days = total_days / len(unique_books)

# Sort books by borrowing duration
sorted_books = sorted(book_counts.items(), key=lambda x: x[1], reverse=True)

# Print the results
print("Most borrowed book:", most_borrowed_book)
print("Least borrowed book:", least_borrowed_book)
print("Average borrowing time:", average_days)
print("Unique book titles:", unique_books)
print("Books sorted by borrowing duration:", sorted_books)