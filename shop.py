from data import produits_data
from product import Product

class Shop:
    def __init__(self):
        self.stock = {}
        for name, info in produits_data.items():
            self.stock[name] = Product(
                name=name,
                prix=info["prix"],
                stock=info["stock"],
                unite=info['unite'],
                category=info['categorie']
            )

store = Shop()
# poire = store.stock['Poire']
# print(poire.name)     
# print(poire.prix)      
# print(poire.stock)     
# print(poire.unite)     
# print(poire.category)  

# print('-' * 60)
# print(store.stock['Poire'])