from books.models.book_model import Book


class BookRepository:
    def find_all(self, order_by="id"):
        queryset = Book.objects.all()
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset

    def find_one(self, book_id) -> Book | None:
        # return Book.objects.get(pk=book_id) # throws exception
        return Book.objects.filter(pk=book_id).first()

    def create(self, data) -> Book:
        return Book.objects.create(**data)

    def update(self, book_id, data) -> Book:
        book = Book.objects.get(pk=book_id)
        for key, value in data.items():
            setattr(book, key, value)
        book.save()
        return book

    def delete(self, book_id) -> bool:
        book = Book.objects.filter(pk=book_id).first()
        if not book:
            return False
        book.delete()
        return True
