from django.core.management.base import BaseCommand
from book.models import Book

class Command(BaseCommand):
    help = "Load famous books into the bookstore"

    def handle(self, *args, **kwargs):
        books_data = [
            ("To Kill a Mockingbird", "Harper Lee", 399, 10),
            ("1984", "George Orwell", 349, 15),
            ("Pride and Prejudice", "Jane Austen", 299, 12),
            ("The Great Gatsby", "F. Scott Fitzgerald", 320, 8),
            ("The Catcher in the Rye", "J.D. Salinger", 275, 9),
            ("The Alchemist", "Paulo Coelho", 350, 10),
            ("Harry Potter and the Philosopher’s Stone", "J.K. Rowling", 450, 20),
            ("The Lord of the Rings", "J.R.R. Tolkien", 699, 5),
            ("Animal Farm", "George Orwell", 199, 14),
            ("The Hobbit", "J.R.R. Tolkien", 399, 8),
            ("A Tale of Two Cities", "Charles Dickens", 299, 6),
            ("The Book Thief", "Markus Zusak", 375, 10),
            ("The Fault in Our Stars", "John Green", 325, 13),
            ("The Kite Runner", "Khaled Hosseini", 340, 11),
            ("The Da Vinci Code", "Dan Brown", 430, 9),
            ("Angels & Demons", "Dan Brown", 420, 7),
            ("Thinking, Fast and Slow", "Daniel Kahneman", 520, 5),
            ("Sapiens", "Yuval Noah Harari", 499, 6),
            ("Becoming", "Michelle Obama", 480, 4),
            ("Atomic Habits", "James Clear", 450, 8),
            ("Rich Dad Poor Dad", "Robert Kiyosaki", 399, 10),
            ("The Power of Habit", "Charles Duhigg", 375, 6),
            ("Ikigai", "Hector Garcia, Francesc Miralles", 299, 9),
            ("Man’s Search for Meaning", "Viktor E. Frankl", 310, 7),
        ]

        for title, author, price, qty in books_data:
            Book.objects.get_or_create(title=title, defaults={
                'author': author,
                'price': price,
                'available_quantity': qty
            })

        self.stdout.write(self.style.SUCCESS("✅ Famous books loaded successfully."))
