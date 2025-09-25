from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def benchmark_models(dataset_loader, dataset_name):
    # Load dataset
    data = dataset_loader()
    X, y = data.data, data.target

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Models to compare
    models = {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators=100)
    }

    accuracies = {}

    # Train & evaluate
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        accuracies[name] = acc
        print(f"{dataset_name} → {name:20s} Accuracy: {acc*100:.2f}%")

    # Visualization
    plt.figure(figsize=(7,5))
    plt.bar(accuracies.keys(), [v*100 for v in accuracies.values()],
            color=["skyblue","orange","green"])
    plt.title(f"Model Accuracy Comparison on {dataset_name}")
    plt.ylabel("Accuracy (%)")
    plt.ylim(80, 105)
    plt.show()


if __name__ == "__main__":
    # Run benchmark on different datasets
    benchmark_models(load_iris, "Iris Dataset 🌸")
    benchmark_models(load_wine, "Wine Dataset 🍷")
    benchmark_models(load_digits, "Digits Dataset 🔢")
