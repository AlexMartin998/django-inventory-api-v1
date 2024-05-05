from books.models.book_model import Book
from books.serializers.book_serializers import BookSerializer


class BookRepository:
    def find_all(self, order_by='id'):
        queryset = Book.objects.all()
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset

    def find_one(self, book_id):
        return Book.objects.get(pk=book_id)

    def create(self, data):
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def update(self, book_id, data):
        book = Book.objects.get(pk=book_id)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def delete(self, book_id):
        book = Book.objects.get(pk=book_id)
        book.delete()
        return True
