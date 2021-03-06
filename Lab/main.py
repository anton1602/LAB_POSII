from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from pickle import dump

import read_dataset

names = ["Nearest Neighbors", "Linear SVM", "Decision Tree", "Neural Net"]
scoring = ["accuracy", "recall", "precision", "f1"]

kncParams = {'n_neighbors': [3, 5, 10]}
svcParams = {'C': [0.025, 0.5, 1]}
dtcParams = {'max_depth': [5, 10, 15]}
mlpParams = {'alpha': [0.0001, 0.001, 1], 'max_iter': [500, 1000, 1500]}
tuneParams = [kncParams, svcParams, dtcParams, mlpParams]

classifiers = [
    KNeighborsClassifier(),
    SVC(kernel="linear"),
    DecisionTreeClassifier(),
    MLPClassifier()]

X, y = read_dataset.get_breast_cancer_dataset()

X = StandardScaler().fit_transform(X)
y = y.astype('int')

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=.4, random_state=42)

wholeBestEstimator = None
wholeBestScore = 0.0

# iterate over classifiers
for name, clf, params in zip(names, classifiers, tuneParams):
    gsCV = GridSearchCV(clf, params, scoring=scoring, refit='accuracy')
    gsCV.fit(X_train, y_train)
    if wholeBestScore < gsCV.best_score_:
        wholeBestEstimator = (name, gsCV.best_estimator_)
        wholeBestScore = gsCV.best_score_

    y_pred = gsCV.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print("Accuracy:{:.3f}".format(accuracy),
          "| Recall:{:.3f}".format(recall),
          "| Precision:{:.3f}".format(precision),
          "| F1 score:{:.3f}".format(f1),
          "({0}; params:{1})".format(name, gsCV.best_params_))

print(wholeBestEstimator[0] + " won the prize!")

bestFileNameEver = "heart_d.dbd"
dump(wholeBestEstimator, open(bestFileNameEver, 'wb'))

print(wholeBestEstimator[0] + " was saved to " + bestFileNameEver)
print("Done")
