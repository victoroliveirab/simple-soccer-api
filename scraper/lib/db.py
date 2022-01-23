from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class Db:
    conn: MongoClient

    @classmethod
    def connect(cls, conn_str: str):
        client = MongoClient(conn_str)
        cls.conn = client['scraper-dev']
        try:
            client.list_database_names()
            return True
        except ConnectionFailure as exc:
            print(exc)
            return False
