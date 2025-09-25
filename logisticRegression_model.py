from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def iris_logistic_regression():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    target_names = iris.target_names

    # Split into training & testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Logistic Regression model
    model = LogisticRegression(max_iter=200)  # increase iterations for convergence
    model.fit(X_train, y_train)

    # Test model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n✅ Logistic Regression Accuracy: {accuracy*100:.2f}%")

    # Predict a new flower
    sample = [[6.7, 3.1, 4.7, 1.5]]  # Example measurements
    prediction = model.predict(sample)
    print(f"🌸 Predicted Flower: {target_names[prediction[0]]}")

if __name__ == "__main__":
    iris_logistic_regression()
