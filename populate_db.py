from tinydb import TinyDB
from UtilitiesProvider import UtilitiesProvider
from domain.Product import Product
from domain.User import User

UtilitiesProvider.create()
repo = UtilitiesProvider.repo
userRepo = UtilitiesProvider.userRepo


repo.clear()

for i in range(3):
    product = Product(i.__str__(), "Lapte" + i.__str__(), "10", "200", "")
    product.username = "a"
    repo.addProduct(product)


userRepo.addUser(User("a", "a"))
userRepo.addUser(User("b", "b"))
