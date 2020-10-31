from domain.Product import *
class Repo:
    def __init__(self, db):
        self.table = db.table("Products")


    def addProduct(self, product):
        self.table.insert(product.toDict())

    def returnAllElems(self):
        elems = self.table.all()
        result = []
        for i in elems:
            result.append(Product(**i))

        return result


