import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate a bar chart
def CreateBarChart(PathToFile):
    # Load the dataset from the CSV file
    data = pd.read_csv(PathToFile)

    # Extract the country codes and data for plotting
    country_codes = data['World']
    years = list(data.columns[1:10])  # the data for years 1970 to 2020 is in columns 3 to 7

    # Plotting the bar chart
    plt.figure(figsize=(12, 8))
    for i in range(len(country_codes)):
        plt.bar([x + i  for x in range(len(years))], data.iloc[i, 1:10])

    # Adding title and labels
    plt.title('Access to electricity (% of population) - World')
    plt.xlabel('Years')
    plt.ylabel('% of Population')

    # Adding x-axis labels for years
    plt.xticks([i for i in range(len(years))], years)

    # Adding legend
    plt.legend()

    # Display the plot
    plt.show()

# Replace 'path_to_your_csv_file.csv' with the actual path to your CSV file
PathToFile = r'C:\Users\Avinash Reddy\Videos\ADS1Assgn\AccesstoElec.csv'
CreateBarChart(PathToFile)
