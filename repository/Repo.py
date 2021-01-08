from tinydb import Query

from domain.Product import *


class Repo:
    def __init__(self, db):
        self.db = db
        self.table = db.table("Products")

    def addProduct(self, product):
        self.table.insert(product.toDict())

    def updateProduct(self, product):
        prod = Query()
        self.table.update(product.toDict(), prod.id == product.id)

    def returnAllElems(self, username, limit, page):
        prod = Query()
        elem = self.table.search(prod.username == username)
        result = []
        start = limit * (page - 1)
        end = min(len(elem), limit * page)

        for i in range(start, end):
            result.append(Product(**elem[i]))

        return result

    def returnOne(self, id):
        prod = Query()
        elem = self.table.search(prod.id == int(id))
        result = Product(**elem[0])

        return result

    def clear(self):
        self.db.drop_tables()

    def noProducts(self):
        return len(self.table)