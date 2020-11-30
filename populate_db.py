from tinydb import TinyDB
from UtilitiesProvider import UtilitiesProvider
from domain.Product import Product

UtilitiesProvider.create()
repo = UtilitiesProvider.repo

repo.clear()

repo.addProduct(Product("1", "Lapte", 10, 200))
repo.addProduct(Product("2", "Oua", 1, 400))
repo.addProduct(Product("3", "Sticsuri", 3, 2000))
