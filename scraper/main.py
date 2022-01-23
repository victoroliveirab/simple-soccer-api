from lib.db import Db
from lib.parser import DefaultParser

mongodb_conn_str = 'mongodb://admin:admin@127.0.0.1:27017/scraper-dev'

if __name__ == '__main__':
    Db.connect(mongodb_conn_str)
    parser = DefaultParser()
    with open('test.html') as text:
        parser.parse(text)
    print('Finished execution')
