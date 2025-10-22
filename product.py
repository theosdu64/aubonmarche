class Product:
    def __init__(self, name, prix, stock, unite, category):
        self.name = name
        self.prix = prix
        self.stock = stock
        self.unite = unite
        self.category = category

    def __repr__(self):
        return (f"name={self.name}, prix={self.prix}€, stock={self.stock} {self.unite}, "
                f"category={self.category})")

    def __str__(self):
        return (f"{self.name} - {self.prix}€ - {self.stock} {self.unite} - catégorie : {self.category}")