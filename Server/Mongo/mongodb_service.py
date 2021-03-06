from pymongo import MongoClient


class MongodbService(object):
    _instance = None
    _client = None
    _db = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.__init__(cls._instance, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._client = MongoClient("192.168.1.10", 27017)
        self._db = self._client.breast_cancer_db

    def get_input_transaction(self):
        current_transaction = self._db.transactions_input.find_one()
        if current_transaction is not None:
            self._db.transactions_input.delete_one({"_id": current_transaction["_id"]})
        return current_transaction

    def set_output_transaction(self, result):
        return self._db.transactions_output.insert_one({"result": int(result)})
