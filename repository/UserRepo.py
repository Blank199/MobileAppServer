from tinydb import Query

from domain.User import *


class UserRepo:
    def __init__(self, db):
        self.db = db
        self.table = db.table("Users")

    def addUser(self, user):
        self.table.insert(user.toDict())

    def returnOne(self, username):
        user = Query()
        elem = self.table.search(user.username == username)
        result = User(**elem[0])

        return result

    def verifyLogin(self, myUser):
        user = Query()
        elem = self.table.search(user.username == myUser.username)
        result = User(**elem[0])
        if result.password != myUser.password:
            result = None

        return result

