from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        """
        Initialize test data and test client
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

        # Create some sample books
        self.book1 = Book.objects.create(title="Book One", author="Author", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author", publication_year=2021)

        # URLs
        self.list_url = '/api/books/'
        self.detail_url = f'/api/books/{self.book1.id}/'

    def test_list_books(self):
        """
        Test retrieving the list of books
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_retrieve_book_detail(self):
        """
        Test retrieving a single book detail
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        """
        Test creating a new book as an authenticated user
        """
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """
        Test creating a new book as an unauthenticated user
        """
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2022}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """
        Test updating an existing book
        """
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        """
        Test deleting a book
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """
        Test filtering books by title
        """
        response = self.client.get(self.list_url, {'title': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books(self):
        """
        Test searching books by title or author
        """
        response = self.client.get(self.list_url, {'search': 'Author Two'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author Two')

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year
        """
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[1]['publication_year'], 2021)