# Django Blog Post Management

    ## Features
    - **List Posts:** View all blog posts at `/`.
    - **View Post Details:** Click on a post title to view the full content.
    - **Create Post:** Authenticated users can create a new post at `/posts/new/`.
    - **Edit Post:** Post authors can edit their posts at `/posts/<id>/edit/`.
    - **Delete Post:** Post authors can delete their posts at `/posts/<id>/delete/`.

    ## Setup Instructions
    1. Run migrations: `python manage.py makemigrations && python manage.py migrate`.
    2. Start the server: `python manage.py runserver`.
    3. Access the app at `http://127.0.0.1:8000/`.

    ## Permissions
    - List and detail views are accessible to all users.
    - Create, edit, and delete views are restricted to authenticated users.
    - Only post authors can edit or delete their own posts.

    ## Testing
    - Test CRUD operations for functionality and security.
    - Verify that unauthorized users cannot modify others' posts.