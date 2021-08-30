class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased):
        newPriceMultiplier = (percent_change / 100) * self.price
        if is_increased:
                self.price += newPriceMultiplier
                # print(newPriceMultiplier, self.price)
                # print(item.name, item.price)
        else:
                self.price -= newPriceMultiplier
        return self
    def print_info(self):
        print(self.name, self.category, self.price)