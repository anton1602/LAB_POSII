from time import sleep
from read_client_dataset import get_client_dataset
from Mongo.mongodb_service import MongodbService
from sklearn.preprocessing import StandardScaler
import cgi, cgitb




def predict(dto):
	storage = MongodbService.get_instance()
	#dto = {'age': 1.0, 'sex': 0.0, 'cp': 1.0, 'trestbps': 1.0, 'chol': -1.0, 'fbs': 1.0, 'restecg': -1.0, 'thalach': -1.0, 'exang': 0.0, 'oldpeak': -1.0, 'slope': 0.0, 'ca': 0.0, 'thal': -1.0}
	print(dto)
	storage.set_input_transaction(dto)
	result = None
	while result is None:
		sleep(0.5)
		result = storage.get_output_transaction()
	return result