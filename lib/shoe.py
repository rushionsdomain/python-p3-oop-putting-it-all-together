class Shoe:
    def __init__(self, brand, size):
        """Initializes a Shoe instance with a brand and size."""
        self.brand = brand
        self.size = size  # This will call the size setter method

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        self._size = value

    def cobble(self):
        """Repairs the shoe and sets its condition to 'New'."""
        self.condition = "New"
        print("Your shoe is as good as new!")
