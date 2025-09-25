import pandas as pd
from tkinter import Tk, Label, Button, Entry, filedialog, Checkbutton, IntVar
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Preprocessing function
def preprocess_data(df, target_column):
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna(df[col].median())
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == "object" and col != target_column:
            df[col] = le.fit_transform(df[col])
    if df[target_column].dtype == "object":
        df[target_column] = le.fit_transform(df[target_column])
    return df

# Benchmark function
def benchmark_models(df, target_column, selected_models, dataset_name="Custom Dataset"):
    df = preprocess_data(df, target_column)
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    available_models = {
        "Logistic Regression": LogisticRegression(max_iter=500),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators=100),
        "Gradient Boosting": GradientBoostingClassifier(),
        "SVM": SVC(),
        "KNN": KNeighborsClassifier()
    }

    models = {name: model for name, model in available_models.items() if selected_models[name].get() == 1}

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results[name] = {
            "Accuracy": accuracy_score(y_test, y_pred)*100,
            "Precision": precision_score(y_test, y_pred, average="weighted")*100,
            "Recall": recall_score(y_test, y_pred, average="weighted")*100,
            "F1-Score": f1_score(y_test, y_pred, average="weighted")*100
        }

    # Print results
    print(f"\n--- Model Performance on {dataset_name} ---")
    for model_name, metrics in results.items():
        print(f"\n{model_name}:")
        for metric, score in metrics.items():
            print(f"  {metric}: {score:.2f}%")

    # Accuracy chart
    plt.figure(figsize=(8,5))
    plt.bar(results.keys(), [v["Accuracy"] for v in results.values()],
            color=["skyblue","orange","green","purple","red","cyan"][:len(results)])
    plt.title(f"Model Accuracy Comparison on {dataset_name}")
    plt.ylabel("Accuracy (%)")
    plt.ylim(0, 105)
    plt.show()

# GUI
def select_file():
    filename = filedialog.askopenfilename(filetypes=[("CSV Files","*.csv")])
    entry_file.delete(0, "end")
    entry_file.insert(0, filename)

def run_benchmark():
    file_path = entry_file.get()
    target_col = entry_target.get()
    df = pd.read_csv(file_path)
    selected = {name: var for name, var in model_vars.items()}
    benchmark_models(df, target_col, selected)

root = Tk()
root.title("ML Benchmarking Tool GUI")
root.geometry("500x400")

Label(root, text="Select CSV File:").pack(pady=5)
entry_file = Entry(root, width=50)
entry_file.pack()
Button(root, text="Browse", command=select_file).pack(pady=5)

Label(root, text="Target Column:").pack(pady=5)
entry_target = Entry(root, width=50)
entry_target.pack(pady=5)

Label(root, text="Select Models:").pack(pady=10)
model_vars = {}
for model in ["Logistic Regression", "Decision Tree", "Random Forest", "Gradient Boosting", "SVM", "KNN"]:
    var = IntVar(value=1)
    Checkbutton(root, text=model, variable=var).pack(anchor="w")
    model_vars[model] = var

Button(root, text="Run Benchmark", command=run_benchmark, bg="green", fg="white").pack(pady=20)

root.mainloop()
