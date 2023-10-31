import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def CreatePieChart(PathToFile):
    # Load the dataset from the CSV file
    data = pd.read_csv(PathToFile)

    # Extract data for the specific year
    year_data = data.iloc[:,7]

    # Extract country codes
    country_codes = data['Country Code']

    # Creating a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(year_data, labels=country_codes)
    plt.title(f'Pie Chart for Year 1980')
    plt.show()

# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
PathToFile = r'C:\Users\Avinash Reddy\Videos\Harsha Assignment\reduceddata.csv'
CreatePieChart(PathToFile)
