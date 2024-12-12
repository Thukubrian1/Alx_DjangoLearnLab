# Advanced API Project


    ## Views Overview
    - **BookListView**: Lists all books with optional filtering by title or author.
    - **BookDetailView**: Retrieves a single book by its ID.
    - **BookCreateView**: Allows authenticated users to create a new book.
    - **BookUpdateView**: Allows authenticated users to update an existing book.
    - **BookDeleteView**: Allows authenticated users to delete a book.

    ## Endpoints
    - `/books/`: List all books.
    - `/books/<int:pk>/`: Retrieve a single book.
    - `/books/create/`: Create a new book (authenticated).
    - `/books/update/<int:pk>/`: Update an existing book (authenticated).
    - `/books/delete/<int:pk>/`: Delete a book (authenticated).

    ## Permissions
    - **Unauthenticated Users**: Read-only access to ListView and DetailView.
     - **Authenticated Users**: Full CRUD access.

    ## Testing
    Use tools like Postman or curl to verify endpoint functionality.

## Advanced Query Capabilities

    ### Filtering
    - Filter by title: `/books/?title=Example`
    - Filter by author name: `/books/?author__name=John+Doe`
    - Filter by publication year: `/books/?publication_year=2023`

    ### Searching
    - Search books by title or author: `/books/?search=example`

    ### Ordering
    - Order by title (ascending): `/books/?ordering=title`
    - Order by publication year (descending): `/books/?ordering=-publication_year`

    ### Notes
    - Combine features for more advanced queries.
    Example: `/books/?search=example&ordering=title`

## Testing

    ### Running Tests
    To execute the test suite, run the following command:
    ```bash
    python manage.py test api