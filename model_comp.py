from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def compare_models_visual():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    target_names = iris.target_names

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Models to compare
    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators=100)
    }

    accuracies = {}

    # Train, predict & evaluate
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        accuracies[name] = acc
        print(f"{name:20s} → Accuracy: {acc*100:.2f}%")

    # Visualization
    plt.figure(figsize=(7,5))
    plt.bar(accuracies.keys(), [v*100 for v in accuracies.values()], color=["skyblue","orange","green"])
    plt.title("Model Accuracy Comparison on Iris Dataset")
    plt.ylabel("Accuracy (%)")
    plt.ylim(90, 105)  # zoom in for better view
    plt.show()

if __name__ == "__main__":
    compare_models_visual()
