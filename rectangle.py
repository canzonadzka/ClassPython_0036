class Rectangle:
    """A rectangle with length and width properties."""

    def __init__(self, length, width):
        # Input value cannot be 0 (or negative)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width cannot be 0 or negative!")
        self.length = length
        self.width = width

    def circumference(self):
        """Circumference (perimeter) = 2 x (length + width)"""
        return 2 * (self.length + self.width)

    def area(self):
        """Area = length x width"""
        return self.length * self.width

    def __str__(self):
        return f"Rectangle, {self.length} cm long, and {self.width} cm wide"