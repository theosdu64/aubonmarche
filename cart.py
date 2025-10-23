from product import Product

class Cart:
	def __init__(self):
		self.items = list[tuple[Product, float]] = []

	def add_item(self, product: Product, quantite: float):

		self.items.append((product, quantite))