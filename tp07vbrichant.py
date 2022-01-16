class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num and den are int
        POST : initialization of a new Fraction object for which
        the values of num and den are those defined during
         initialization or those by default
        RAISE : if den = 0 => ZeroDivisionError
                if num and den are not int => TypeError
        """

        assert isinstance(num, int)
        self.__num = num
        assert isinstance(den, int)
        self.__den = den
        if self.__den == 0:
            raise ZeroDivisionError("denominator cannot equals 0")

    @property
    def numerator(self):
        """
            :rtype: int
        """
        return self.__num

    @property
    def denominator(self):
        """
            :rtype: int
        """
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : /
        POST : Return a textual representation of the reduced fraction
        """
        gcd = self.__greatest_common_divisor()
        num = self.__num / gcd
        den = self.__den / gcd
        new_str = str(int(num)) + " / " + str(int(den))
        return new_str

    def as_mixed_number(self):
        """Return a textual representation of the reduced form
         of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : /
        POST : Return a textual representation
        of the reduced form of the fraction as a mixed number
        """
        if self.__num % self.__den == 0:
            return str(int(self.__num / self.__den))
        if self.__num == -1:
            return str(self)
        # simplification de la fraction
        gcd = self.__greatest_common_divisor()
        num = self.__num / gcd
        den = self.__den / gcd
        if (num // den) != 0:
            div = (num // den)
            # test de si la fraction est négative
            # si elle l'est : div +1 pour avoir la bonne valeur et - num pour avoir le bon modulo
            if num < 0:
                div += 1
                num = -num
            modulo = num % den
            new_str = str(str(int(div)) + " + " + str(int(modulo))) + " / " + str(int(den))
            return new_str
        new_str = str(int(num % den)) + " / " + str(int(den))
        return new_str

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : /
         POST : returns the fraction that has been added to other
         RAISES : if other is not Int or Fraction => TypeError
         """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self + Fraction(other, 1)
        # creation of variable
        num1 = self.__num
        den1 = self.__den
        num2 = other.numerator
        den2 = other.denominator

        # put has the same denominator of the 2 fractions (den1 * den2)
        num1 *= den2
        den1 *= den2
        num2 *= self.__den

        # add of the 2 num
        num1 += num2
        return Fraction(num1, den1)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : /
        POST : return the subtraction of other on the fraction
        RAISES : if other is not Int or Fraction => TypeError
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid type, other must be int or Fraction")
        if isinstance(other, int):
            return self - Fraction(other, 1)
        # creation of variable
        num1 = self.__num
        num2 = other.numerator
        den1 = self.__den
        den2 = other.denominator

        # put has the same denominator of the 2 fractions(den1 * den2)
        num1 *= den2
        den1 *= den2
        num2 *= self.__den

        # subtraction of the 2 num
        num1 -= num2
        return Fraction(num1, den1)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : /
        POST : return the fraction multiplied by other
        RAISES : if other is not Int or Fraction => TypeError
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self * Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.__num * other.numerator
            den = self.__den * other.denominator
            return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : /
        POST : return the fraction divided by other
        RAISES : if other is not Int or Fraction => TypeError
        and if other == 0 => ZeroDivisionError
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if other.numerator == 0:
            raise ZeroDivisionError
        if isinstance(other, int):
            return self.__truediv__(Fraction(other, 1))
        return self * Fraction(other.denominator, other.numerator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : /
        POST : return the fraction with num and den power of by other
        RAISES : if other is not Int => TypeError
        """
        if not isinstance(other, int):
            raise TypeError("Invalid arg type, other must be int")
        is_negative_exponent = False
        if other < 0:
            other = - other
            is_negative_exponent = True
        num = self.__num ** other
        den = self.__den ** other
        if is_negative_exponent:
            return Fraction(den, num)
        return Fraction(num, den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : /
        POST : return if 2 fraction are equals or not
        RAISES : if other is not int or Fraction => TypeError
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self == Fraction(other, 1)
        if isinstance(other, Fraction):
            # simplification
            gcd1 = self.__greatest_common_divisor()
            gcd2 = other.__greatest_common_divisor()
            num = self.__num / gcd1
            den = self.__den / gcd1
            num_other = other.numerator / gcd2
            den_other = other.denominator / gcd2

            return num == num_other and den == den_other

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : /
        POST : Returns the decimal value of the fraction
        """
        result = float(self.__num / self.__den)
        return result

    def __greatest_common_divisor(self):
        """Returns the greatest common divisor

        PRE: /
        POST: returns the greatest common divisor of num and den

        """
        num = self.__num
        den = self.__den
        while den != 0:
            memory_value = den
            den = num % den
            num = memory_value
        return num

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : /
        POST : return if numerator value is 0 or not
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : returns if a fraction is an integer or not
        """
        return (self.__num % self.__den) == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : /
        POST : returns if the absolute value of the fraction is under 1
        """
        return abs(self.__num / self.__den) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : returns if the fraction's numerator equals one in reduced form
        """
        gcd = self.__greatest_common_divisor()
        return self.__num / gcd == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : /
        POST : returns if the two fractions are adjacent or not
        RAISES : TypeError if other is not int or Fraction
        """
        if not isinstance(other, int) and not isinstance(other, Fraction):
            raise TypeError("Invalid arg type, other must be int or Fraction")
        if isinstance(other, int):
            return self.is_adjacent_to(Fraction(other, 1))
        res = self - other
        return abs(res.numerator) == 1
