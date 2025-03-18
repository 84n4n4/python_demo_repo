import mlflow
from mlflow.models import infer_signature
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score

from sklearn.model_selection import train_test_split


def main():
    data = load_iris()
    x = data['data']
    y = data['target']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2)

    rnd_clf = RandomForestClassifier(n_estimators=500, n_jobs=-1)  # n_estimators=interaction
    rnd_clf.fit(x_train, y_train)
    y_pred_rnd = rnd_clf.predict(x_test)
    print(classification_report(y_test, y_pred_rnd))

    accuracy = accuracy_score(y_test, y_pred_rnd)
    f1 = f1_score(y_test, y_pred_rnd, average='macro')

    mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
    mlflow.set_experiment("/iris_RF_manual_log")

    with mlflow.start_run():
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1", f1)
        mlflow.set_tag("Training Info", "Basic RF model for iris data")
        signature = infer_signature(x_train, rnd_clf.predict(x_train))

        model_info = mlflow.sklearn.log_model(
            sk_model=rnd_clf,
            artifact_path="iris_model",
            signature=signature,
            input_example=x_train,
            registered_model_name="manual_log_exmaple",
        )


if __name__ == "__main__":
    main()
