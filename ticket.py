from client import Client

class Ticket:
	def __init__(self, name: str, price: float | int, stock: float | int, unite: str, category: str):
		self.name = name