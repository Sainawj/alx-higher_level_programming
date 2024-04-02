class Square:
    def __init__(self, size):
        self.size = size

    def set_size(self, new_size):
        """Set the size of the square."""
        self.size = new_size

    def get_size(self):
        """Get the size of the square."""
        return self.size

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return 4 * self.size
