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

	def buy_product(self, product_name, qty):
		if product_name not in self.stock:
			raise ValueError('Produit inexistant')
		product = self.stock[product_name]
		price = product.prix * qty
		product.update_stock(qty)
		return price

	def get_products_by_category(self, product_category):
		names = []

		for name, product in self.stock.items():
			if product_category == product.category:
				names.append(name)
		return names

shop = Shop()     
print(shop.buy_product('Poire', 1))
get = shop.get_products_by_category("fruit")
print(get)