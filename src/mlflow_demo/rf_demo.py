import pandas
from sklearn import metrics, svm
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from src.anchor import data_dir

from sklearn.model_selection import train_test_split
import pandas as pd

def main():
    data = load_iris()
    x = data['data']
    y = data['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

    rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1)  # n_estimators=interaction
    rnd_clf.fit(x_train, y_train)
    y_pred_rnd = rnd_clf.predict(x_test)
    print(classification_report(y_test, y_pred_rnd))



if __name__ == "__main__":
    main()