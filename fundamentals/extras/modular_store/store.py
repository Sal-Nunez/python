from product import Product
productClass = Product
class Store():
    def __init__(self, store_name):
        self.store_name = store_name
        self.all_products = []
    # all_products = Product.all_products
    def add_product(self, name, price, category):
        name = Product(name, price, category)
        self.all_products.append(name)
        # print(self.all_products)
        return self
    def sell_product(self, id):
        Product.all_products.remove(id)
        return self
    def inflation(self, percent_increase):
        for item in self.all_products:
            item.update_price(percent_increase, True)
        return self
    def set_clearance(self, category_input, percent_discount):
        for item in self.all_products:
            if category_input == item.category:
                item.update_price(percent_discount, False)
        return self
    def print_all_products(self):
        for item in self.all_products:
            print(item.name)
            print(item.price)
            print(item.category)
        return self
store = Store('Stater Broskis')
# store2 = Store('Tyler Store')
# print(store)
# print(store2)
store.add_product('Banana', 2, 'fruit')
store.add_product('Strawberry', 1, 'fruit')
store.add_product('Carrot', 3, 'vegetable')
# store.print_all_products()
# print(store.store_name, store.all_products)
# # store.sell_product('Banana')
store.inflation(2)
store.set_clearance('vegetable', 2)
print(store.store_name)
store.print_all_products()