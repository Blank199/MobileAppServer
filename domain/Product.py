from flask import jsonify


class Product:
    def __init__(self, id, name, price, stock, imgName, *args, **kwargs):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.imgName = imgName
        self.username = ""

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'imgName': self.imgName,
            'username': self.username
        }
