import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to generate a line plot with multiple lines
def Create_LinePlot(PathToFile):
    # Load the dataset from the CSV file
    data = pd.read_csv(PathToFile)

    # Display the loaded data
    print(data)

    # Extracting the data for plotting
    country_codes = data['Country Code'] # Fetched the country codes from CSV
    years = data.columns[3:]  # the columns of years starts from 3rd column.

    # Creating a line plot with multiple lines based on Number of countries 
    plt.figure(figsize=(10, 6))
    for idx in range(len(country_codes)):
        plt.plot(years, data.iloc[idx, 3:],label=country_codes[idx])

    # Adding plot title and Axis labels
    plt.title('Infant Mortality Rate in Major Europe Countries from 1970 to 2020')
    plt.xlabel('Years') 
    plt.ylabel('Infant Mortality rate (per 1,000 live births)')

    # Adding legend
    plt.legend()

    # Display the plot
    plt.show()

# Calling function to generate the Line Plot
PathToFile = r'C:\Users\Avinash Reddy\Videos\Harsha Assignment\reduceddata.csv'
Create_LinePlot(PathToFile)
