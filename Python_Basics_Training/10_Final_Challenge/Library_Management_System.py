class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, category):
        book = Book(title, author, category)
        self.books.append({
            'title': book.title,
            'author': book.author,
            'category': book.category
        })
        print(f"Book '{title}' by {author} added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, search_term):
        found_books = []
        search_term = search_term.lower()
        
        for book in self.books:
            if (search_term in book['title'].lower() or 
                search_term in book['author'].lower()):
                found_books.append(book)
        
        if found_books:
            print("\nFound Books:")
            for book in found_books:
                print(f"Title: {book['title']}, Author: {book['author']}, "
                      f"Category: {book['category']}")
        else:
            print("No books found matching your search.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        
        print("\nLibrary Books:")
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, "
                  f"Category: {book['category']}")


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        category = input("Enter book category: ")
        library.add_book(title, author, category)
    
    elif choice == '2':
        title = input("Enter book title to remove: ")
        library.remove_book(title)
    
    elif choice == '3':
        search_term = input("Enter title or author to search: ")
        library.search_book(search_term)
    
    elif choice == '4':
        library.display_books()
    
    elif choice == '5':
        print("Thank you for using the Library Management System!")
        break
    
    else:
        print("Invalid choice. Please try again.")

