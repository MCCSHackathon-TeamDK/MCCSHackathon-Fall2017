class Gift:

    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def compareTo(self, gift):
        return self.price < gift.price
