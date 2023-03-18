import os
from uuid import uuid4


class MongoTable:
    """
    ORM para MongoDB
    Desenvolvido por Júlio Cascalles
    """
# ---------------------------------
    # URL_HOST = 'mongodb://localhost:27017/'
    URL_HOST = 'mongodb+srv://{user}:{password}@{cluster}.mongodb.net/{options}'.format(
        user='root',
        password=os.environ.get('MONGODB_PASSWORD'),
        cluster='cluster0.t17ebgr',
        options='?retryWrites=true&w=majority'
    )
# ---------------------------------
    DATABASE_NAME = ''

    _db = None

    @classmethod
    def collection(cls):
        if MongoTable._db is None:
            from pymongo import MongoClient
            conn = MongoClient(cls.URL_HOST, connect=False)
            MongoTable._db = conn[cls.DATABASE_NAME]
        return MongoTable._db.get_collection(cls.__name__)

    def save(self):
        record  = {
            k: v for k, v in self.__dict__.items()
            if not k.startswith('_')
        }
        if not record.get('id'):
            record['id'] = str(uuid4())
            self.id = record['id']
        self.collection().update_one(
            {'id': record['id']},
            {'$set': record},
            upsert=True
        )

    @classmethod
    def find(cls, **args) -> list:
        return [cls(**o) for o in cls.collection().find(filter=args)]

    @classmethod
    def delete(cls, **args):
        cls.collection().delete_many(args)
