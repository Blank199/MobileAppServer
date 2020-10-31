from tinydb import TinyDB
from UtilitiesProvider import UtilitiesPtovide
from domain.Product import Product

UtilitiesPtovide.create()
repo = UtilitiesPtovide.repo


repo.addProduct(Product(1, "Lape", 10, 200))
repo.addProduct(Product(2, "Oua", 1, 400))
repo.addProduct(Product(3, "Sticsuri", 3, 2000))
