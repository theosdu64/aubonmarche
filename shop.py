from data import produits_data
from product import Product

class Shop:
	def __init__(self):
		self.tickets = []
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

	@staticmethod
	def format_input(number):
		return 'legume' if number == 1 else 'fruit'

	def get_products_by_category(self, product_category):
		product_category = self.format_input(product_category)
		names = []

		for name, product in self.stock.items():
			if product_category == product.category:
				names.append({'name' : name, 'stock' : product.stock, 'prix' : product.prix})
		return names
	
	def get_bilan(self):
		price_bilan = 0
		bilan = []
		tickets = self.tickets
		print(tickets)
		for x in tickets:
			for el in x:
				print(el['prix'])
				price_bilan += el['prix']
		for i, ticket in enumerate(self.tickets, 1):
			bilan.append(f"Commande n°{i}: {ticket}")	
		for x in bilan:	
			print(f'\n{x}')
		print(f'Total  des commandes {price_bilan}')

shop = Shop()     
