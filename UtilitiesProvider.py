from tinydb import TinyDB

from repository.Repo import *
from repository.UserRepo import *


class UtilitiesProvider:
    repo = None
    db = None
    userRepo = None

    @classmethod
    def create(cls):
        cls.db = TinyDB('D:\\Mobile\\Server\\data\\db.json')
        cls.repo = Repo(cls.db)
        cls.userRepo = UserRepo(cls.db)
