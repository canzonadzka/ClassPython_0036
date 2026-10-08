class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width cannot be 0 or negative!")
        self.length = length
        self.width = width