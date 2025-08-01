class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation of the Book instance"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
        
    
    