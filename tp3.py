class Product:
    """Class representing a product and his attribute

        Author : V. Brichant
        Date : Janvier 2022
        """

    def __init__(self, name="nom de test", price_euro=1, price_dollar=1.2):
        """This builds a fraction based on some numerator and denominator.

                PRE : name is str and price is int
                POST : initialization of a new Product object for which
                the name is defined during initialization
                RAISE :
                """
        self.__name = name
        self.__price_dollar = price_dollar
        self.__price_euro = price_euro
        self.taut_de_change = 1.2
        self.ingredient = []

    def __str__(self):
        texte = "Product(name=" + self.name + ")"
        if self.price_euro != 0 and self.price_euro is not None:
            texte += "Prix (euros): " + str(self.price_euro) + " € \n"
        if self.price_dollar != 0 and self.price_dollar is not None:
            texte += "Prix (dollars) : " + str(self.price_dollar) + " $ \n"
        if self.ingredient:
            texte += "Ingrédients : \n"
            for i in self.ingredient:
                texte += str(i) + " \n"
        return texte

    def __getitem__(self, item):
        liste_ingredient = self.get_sorted_ingredients()
        return liste_ingredient[item]

    @property
    def name(self):
        return self.__name

    @property
    def price_dollar(self):
        return self.__price_dollar

    @property
    def price_euro(self):
        return self.__price_euro

    @price_dollar.setter
    def price_dollar(self, value):
        self.__price_dollar = value
        self.__price_euro = self.__price_dollar / 1.2

    @price_euro.setter
    def price_euro(self, value):
        self.__price_euro = value
        self.__price_dollar = self.__price_euro * 1.2

    def add_ingredient(self, ingredient):
        self.ingredient.append(ingredient)

    def get_sorted_ingredients(self):
        liste_copie = sorted(self.ingredient.copy())
        return liste_copie


def checkout(my_product_list, is_euro=True):
    total = 0
    for i in my_product_list:
        if is_euro:
            total += i.price_euro
        else:
            total += i.price_dollar
    return total


pomme = Product()
print(pomme.price_dollar)

print(pomme.name)
pomme.price_euro = 1.42
print(pomme.price_euro)
print(pomme.price_dollar)

print("Prix($) = ", pomme.price_dollar)

print("Prix(€) =", pomme.price_euro)

pomme.price_dollar = 3.14
print(pomme.price_dollar)
print(pomme.price_euro)

print("Prix(€) = ", pomme.price_euro)
