from models import  Author, Book, Library, Librarian
DATABASE_URL = 'sqlite:///your_database.db'  
from relationship_app.models import Author, Book, Library, Librarian 



def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    :param author_name: The name of the author.
    :return: List of books by the given author.
    """
    try:
        author = Author.objects.get(name=author_name)
        Author.objects.filter(author=author)
        books = author.books.all()  #
        return books
    except Author.DoesNotExist:
        return f"No author found with name {author_name}"

def query_all_books_in_library(library_name):
    """
    List all books in a specific library.
    :param library_name: The name of the library.
    :return: List of books in the library.
    """
    try:
        library = Library.objects.get(name=library_name)  
        books = library.books.all()  
        return books
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"

def query_librarian_for_library(librarian_name):
    """
    Retrieve the librarian for a specific library.
    :param library_name: The name of the library.
    :return: The librarian of the library.
    """
    try:
        librarian = Librarian.objects.get(library="")  
        librarian = librarian.librarian  
    except Library.DoesNotExist:
        return f"No library found with name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library {librarian_name}"

if __name__ == "__main__":

    author_name = "J.K. Rowling"
    books_by_author = query_books_by_author(author_name)
    print(f"Books by {author_name}: {books_by_author}")

    library_name = "Central Library"
    books_in_library = query_all_books_in_library(library_name)
    print(f"Books in {library_name}: {books_in_library}")

    librarian = query_librarian_for_library(library_name)
    print(f"Librarian for {library_name}: {librarian}")