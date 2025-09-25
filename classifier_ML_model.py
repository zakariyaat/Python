from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def iris_classifier():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    target_names = iris.target_names

    # Split into training & testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Test model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n✅ Model Accuracy: {accuracy*100:.2f}%")

    # Predict a new flower
    sample = [[5.1, 3.5, 1.4, 0.2]]  # Sepal & Petal measurements
    prediction = model.predict(sample)
    print(f"🌸 Predicted Flower: {target_names[prediction[0]]}")

if __name__ == "__main__":
    iris_classifier()
