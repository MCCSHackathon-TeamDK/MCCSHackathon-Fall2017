class Gift:

    def __init__(self, name, price, year, id):
        self.name = name
        self.price = price
        self.year = year
        self.id = id

    def compare_to(self, gift):
        """
        Compares price to price of other gift
        """
        return self.price < gift.price

    def is_card(self):
        """
        A card is a gift with card in the name and price is zero
        """
        return "card" in self.name and self.price == 0
