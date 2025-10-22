from data import produits_data

class Shop:
    def __init__(self):
        self.stock = produits_data

store = Shop()
print(store.stock)