import pandas as pd
import matplotlib.pyplot as plt

def covid_visualization():
    # Sample dataset (worldwide COVID-19 cases)
    data = {
        "Country": ["USA", "India", "Brazil", "Russia", "France", "Germany", "Australia", "China", "Bangladesh"],
        "Total Cases (M)": [110, 45, 38, 22, 40, 35, 20, 50, 15],
        "Total Deaths (M)": [1.2, 0.53, 0.7, 0.4, 0.35, 0.3, 0.25, 0.45, 0.5]
    }
    
    df = pd.DataFrame(data)
    print("\n--- COVID-19 Data ---")
    print(df)

    # Plot bar chart
    plt.figure(figsize=(8,5))
    plt.bar(df["Country"], df["Total Cases (M)"], color="skyblue", label="Cases")
    plt.bar(df["Country"], df["Total Deaths (M)"], color="red", alpha=0.6, label="Deaths")
    plt.title("COVID-19 Cases vs Deaths")
    plt.xlabel("Country")
    plt.ylabel("Millions")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    covid_visualization()

