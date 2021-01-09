from tinydb import TinyDB
from UtilitiesProvider import UtilitiesProvider
from domain.Product import Product
from domain.User import User

UtilitiesProvider.create()
repo = UtilitiesProvider.repo
userRepo = UtilitiesProvider.userRepo


repo.clear()

images = ['1610111869636.jpeg', '1610112228568.jpeg', '1610112264625.jpeg']

for i in range(3):
    product = Product(i.__str__(), "Lapte" + i.__str__(), "10", "200", images[i], 44.87549767121354, 24.841699598127455)
    product.username = "a"
    repo.addProduct(product)


userRepo.addUser(User("a", "a"))
userRepo.addUser(User("b", "b"))
