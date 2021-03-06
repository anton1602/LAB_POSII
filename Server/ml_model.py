from pickle import load

best_clf_filename = "heart_d.dbd"


class MlModel(object):
    _model = None

    def __init__(self):
        loaded_model = load(open(best_clf_filename, 'rb'))
        self._model = loaded_model[1]

    def predict(self, x_data):
        return self._model.predict(x_data)
