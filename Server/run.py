import pandas as pd
from time import sleep
from ml_model import MlModel
from Mongo.mongodb_service import MongodbService

print("create MlModel")
model = MlModel()
storage = MongodbService.get_instance()

while 1:
    print("Waiting for transaction")
    transaction = None
    while transaction is None:
        sleep(0.5)
        transaction = storage.get_input_transaction()

    print("Got it - {}".format(transaction))
    df = pd.DataFrame(transaction, index=[0]).drop("_id", axis=1)

    result = model.predict(df)[0]
    print("Result - {}".format(result))
    storage.set_output_transaction(result)

