'''
    CS 5001, 
    Fall 2023
    HW7 - SimpleFraction
    Kayser Raei
'''

class SimpleFraction:
    # Initialize with given numerator & denominator
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.validate() # Validate the inputs

    def get_numerator(self):
        # Return the numerator of the fraction
        return self.numerator

    def get_denominator(self):
        # Return the denominator of the fraction
        return self.denominator

    def make_reciprocal(self):
        # Return a new SimpleFraction reciprocal
        return SimpleFraction(self.denominator, self.numerator)

    def validate(self):
        # Check if numerator and denominator/integers
        if not isinstance(self.numerator, int) or \
           not isinstance(self.denominator, int):
            raise ValueError("Numerator & denominator must be integers")
        # Check for a zero denominator
        if self.denominator == 0:
            raise ValueError("Denominator cannot be zero")

    def multiply(self, other):
        # Multiply the fraction by another SimpleFraction/integer
        if isinstance(other, SimpleFraction):
            new_numerator = self.numerator * other.get_numerator()
            new_denominator = self.denominator * other.get_denominator()
        elif isinstance(other, int):
            new_numerator = self.numerator * other
            new_denominator = self.denominator
        else:
            raise ValueError("Can only multiply SF/integer")
        return SimpleFraction(new_numerator, new_denominator)

    def divide(self, other):
        # Divide the fraction by another SimpleFraction/integer
        if isinstance(other, SimpleFraction):
            new_numerator = self.numerator * other.get_denominator()
            new_denominator = self.denominator * other.get_numerator()
        elif isinstance(other, int):
            new_numerator = self.numerator
            new_denominator = self.denominator * other
        else:
            raise ValueError("Can only divide by SF/integer")
        return SimpleFraction(new_numerator, new_denominator)

    def __str__(self):
        # Return the string representation of the fraction
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        # Check if two fractions are equal
        if not isinstance(other, SimpleFraction):
            return False
        return (self.numerator * other.get_denominator() ==
                self.denominator * other.get_numerator())