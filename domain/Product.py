from flask import jsonify


class Product:
    def __init__(self, id, name, price, stock, *args, **kwargs):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }



