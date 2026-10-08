class Rectangle:
    """Persegi panjang dengan properti length (panjang) dan width (lebar)."""

    def __init__(self, length, width):
        # Nilai input tidak boleh 0 (atau negatif)
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar tidak boleh 0 atau negatif!")
        self.length = length
        self.width = width

    def circumference(self):
        """Keliling = 2 x (panjang + lebar)"""
        return 2 * (self.length + self.width)

    def area(self):
        """Luas = panjang x lebar"""
        return self.length * self.width

    def __str__(self):
        return f"Persegi panjang, panjang {self.length} cm dan lebar {self.width} cm"


def read_positive_number(prompt):
    """Terus meminta input sampai pengguna memasukkan angka yang bukan 0."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Nilai tidak boleh 0 atau negatif. Coba lagi.")
                continue
            return value
        except ValueError:
            print("Masukkan angka yang valid.")


def main():
    length = read_positive_number("Masukkan panjang (cm): ")
    width = read_positive_number("Masukkan lebar (cm): ")

    rect = Rectangle(length, width)

    print(rect)  # memanggil __str__ secara otomatis

    # Cara 1: objek.method()
    print(f"Keliling: {rect.circumference()} cm")
    print(f"Luas: {rect.area()} cm2")

    # Cara 2: Class.method(objek) 
    print(f"Keliling (Class.method): {Rectangle.circumference(rect)} cm")
    print(f"Luas (Class.method): {Rectangle.area(rect)} cm2")


if __name__ == "__main__":
    main()