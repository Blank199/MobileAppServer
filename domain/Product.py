from flask import jsonify


class Product:
    def __init__(self, id, name, price, stock, imgName, latitude, longitude, *args, **kwargs):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.imgName = imgName
        self.latitude = latitude
        self.longitude = longitude
        self.username = ""

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'imgName': self.imgName,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'username': self.username
        }
