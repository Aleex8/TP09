
class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : -
        POST : -
        RAISE : ZeroDivisionError si dénominateur = 0
                TypeError si type num et den sont bien int
                FractionNotUnderZero

        """
        #if num < 0 or den < 0:
            #raise FractionNotUnderZero
        if isinstance(num,int) != True or isinstance(den,int) != True:
            raise TypeError("Type num ou type den mauvais")
        if den != 0:
            self.__num = num
            self.__den = den
        else:
            raise ZeroDivisionError("Division par 0 impossible")
        den_temp = den
        pgcd = num
        while den_temp:
            pgcd, den_temp = den_temp, pgcd % den_temp
        if pgcd:
            self.__num = self.__num // pgcd
            self.__den = self.__den // pgcd

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : renvoie une chaîne de caractères expliquant la fraction
        """
        return f"{self.__num}/{self.__den}"

    def as_mixed_number(self, number):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : self.__num < self.__den et number est un nombre non flottant
        POST : renvoie la fraction propre + number
        """
        if self.__num < self.__den and isinstance(number, int):
            return number + (self.__num/self.__den)

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est une variable de type Fraction
         POST : renvoie l'addition de deux fractions
         """
        return ((self.__num/self.__den) + (other.__num/other.__den))

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la soustraction de deux fractions
        """
        #if ((self.__num / self.__den) - (other.__num / other.__den)) >= 0:
            #return ((self.__num / self.__den) - (other.__num / other.__den))
        #else:
            #raise FractionNotUnderZero()
        return ((self.__num / self.__den) - (other.__num / other.__den))

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la multiplication de deux fractions
        """
        return ((self.__num / self.__den) * (other.__num / other.__den))

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la division de deux fractions
        """
        if (other.__num / other.__den) == 0:
            raise ZeroDivisionError
        else:
            return ((self.__num / self.__den) / (other.__num / other.__den))

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie la première frction exposant la deuxième fraction
        """
        return ((self.__num / self.__den) ** (other.__num / other.__den))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est une variable de type Fraction
        POST : renvoie true si la première fraction est égale à la deuxième fraction

        """
        return (self.__num/self.__den) == (other.__num/other.__den)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : other est une variable de type Fraction
        POST : renvoie la fraction sous forme de nombre à décimale
        """
        return f"{self.__num/self.__den:.02f}"

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : -
        POST : renvoie true si la fraction est égal à 0
        """
        return (self.__num/self.__den) == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : renvoie True si la fraction est un nombre entier
        """
        return self.__num % self.__den == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : renvoie True si la valeur absolue de la fraction est plus petit que 1
        """
        return -1 < (self.__num/self.__den) < 1
    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : renvoie True si c'est une fraction unitaire
        """
        return self.__num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other est une variable de type Fraction
        POST : renvoie True si la différence des 2 fractions est plus petit ou égal à 0.5
        """
        difference = self - other
        return difference <= 0.5


if __name__ == "__main__":
    a = Fraction(2,4)
    b = Fraction(2,4)
    print(a*b)