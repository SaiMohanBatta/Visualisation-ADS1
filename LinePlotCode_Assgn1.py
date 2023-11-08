import pandas as pd
import matplotlib.pyplot as plt


# Function to generate a line plot with multiple lines
# By reading the data from a CSV file
def create_line_plot(path_to_file):
    # Load the dataset from the CSV file
    data = pd.read_csv(path_to_file)

    # Getting the data of country codes and years
    # Fetched the country codes from the CSV
    country_codes = data['Country Code']
    # The columns of years start from the 3rd column.
    years = data.columns[2:]

    # Create a line plot with multiple lines based on the number of countries
    plt.figure(figsize=(10, 6))
    for idx in range(len(country_codes)):
	# The data of years starts from column 3.
        plt.plot(years, data.iloc[idx, 2:], label=country_codes[idx])  

    # Adding plot title and axis labels to append to the graphs.
    plt.title('Infant Mortality Rate in Major EU Countries from 1970 to 2020')
    plt.xlabel('Years')
    plt.ylabel('Infant Mortality rate (per 1,000 live births)')

    # Adding legend to the map countrywide
    plt.legend()

    # Display the plot after generating
    plt.show()


# Calling the function to generate the Line Plot
path_to_file = r'C:\Users\batta\OneDrive\Desktop\ads1\assignments1\InfantMortalityRates.csv'
create_line_plot(path_to_file)
