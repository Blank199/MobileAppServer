from tinydb import TinyDB

from repository.Repo import *


class UtilitiesPtovide:
    repo = None
    db = None

    @classmethod
    def create(cls):
        cls.db = TinyDB('D:\\Mobile\\Server\\data\\db.json')
        cls.repo = Repo(cls.db)
