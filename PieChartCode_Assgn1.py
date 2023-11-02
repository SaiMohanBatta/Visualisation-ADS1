import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def CreatePieChart(PathToFile):
    # Load the dataset from the CSV file
    data = pd.read_csv(PathToFile)

    # Extract data for the specific year
    percent = data.iloc[:,1]

    # Extract country codes
    typeofFood = data['Food']

    # Creating a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(percent, labels=typeofFood)
    plt.title('Recommended Diet Chart')
    plt.show()

# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
PathToFile = r'C:\Users\Avinash Reddy\Videos\ADS1Assgn\Diet_Chart.csv'
CreatePieChart(PathToFile)
