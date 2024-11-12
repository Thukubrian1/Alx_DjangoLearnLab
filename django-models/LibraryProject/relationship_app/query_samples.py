from models import  Author, Book, Library, Librarian
DATABASE_URL = 'sqlite:///your_database.db'  



def query_books_by_author(author_name):
    author = (Author).filter(Author.name == author_name).first()
    if author:
        books = (Book).filter(Book.author_id == author.id).all()
        for book in books:
            print(f"Book Title: {book.title}, Author: {author.name}")
    else:
        print(f"No author found with name {author_name}")


def query_books_in_library(library_name):
    library = (Library).filter(Library.name == library_name).first()
    if library:
        books = (Book).filter(Book.library_id == library.id).all()
        if books:
            for book in books:
                print(f"Book Title: {book.title}")
        else:
            print(f"No books found in the library '{library_name}'.")
    else:
        print(f"No library found with name {library_name}")


def query_librarian_for_library(library_name):
    library = (Library).filter(Library.name == library_name).first()
    if library:
        librarian = (Librarian).filter(Librarian.library_id == library.id).first()
        if librarian:
            print(f"The librarian for the library '{library_name}' is {librarian.name}")
        else:
            print(f"No librarian assigned to the library '{library_name}'.")
    else:
        print(f"No library found with name {library_name}")


if __name__ == "__main__":

    print("Query 1: Books by a specific author (e.g., 'J.K. Rowling')")
    query_books_by_author('J.K. Rowling')

    print("\nQuery 2: List all books in a specific library (e.g., 'Central Library')")
    query_books_in_library('Central Library')

    print("\nQuery 3: Retrieve librarian for a specific library (e.g., 'Central Library')")
    query_librarian_for_library('Central Library')