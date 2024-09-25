class Book:
    def __init__(self, title, page_count):
        """Initializes a Book instance with a title and page count."""
        self.title = title
        self.page_count = page_count  # This will call the page_count setter method

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def turn_page(self):
        """Simulates turning a page in the book."""
        print("Flipping the page...wow, you read fast!")
