import unittest

import mongomock

from lib.db import Db
from services import BaseService
from tests.helpers import to_mongodb_document

name = 'impl'
plural_name = 'impls'


class Impl(BaseService):
    def __init__(self):
        super().__init__(name)


ImplService = Impl()

objects = ({'name': 'val1'}, {'name': 'val2'}, {'name': 'val3'})
mock = list(map(to_mongodb_document, objects))


class BaseServiceTest(unittest.TestCase):
    def setUp(self):
        self.client = mongomock.MongoClient()
        self.db = self.client['scraper-test']
        Db.conn = self.db
        self.collection = Db.conn[plural_name]

        self.collection.insert_many(mock)

    def test__init(self):
        self.assertEqual(ImplService.name, name)
        self.assertEqual(ImplService.plural_name, plural_name)

    def test__create_one(self):
        entry = {'name': 'val4'}
        obj = ImplService.create(entry)

        self.assertTrue('_id' in obj.keys())
        self.assertTrue('created_at' in obj.keys())
        self.assertTrue('updated_at' in obj.keys())

        table = list(self.collection.find({}))

        self.assertEqual(len(table), len(mock) + 1)

    def test__create_bulk(self):
        entries = [{'name': 'val4'}, {'name': 'val5'}]
        obj = ImplService.create(entries)

        self.assertTrue(type(obj) is list)
        self.assertEqual(len(obj), len(entries))

        for entry in obj:
            self.assertTrue('_id' in entry.keys())
            self.assertTrue('created_at' in entry.keys())
            self.assertTrue('updated_at' in entry.keys())

        table = list(self.collection.find({}))

        self.assertEqual(len(table), len(mock) + len(entries))
