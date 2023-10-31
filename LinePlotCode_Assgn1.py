import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Function to read the file
def ReadFile(file_path)
    Dataset = pd.read_csv(file_path)

# Function to create Line plot with multiple lines
# For desired years based on the column numbers
def Create_Line_Plot(CntryCol,YearsCol1,YearsCol2)
    Country_Codes = data['CntryCol']
    Years = data.columns[YearsCol1:YearsCol2] 
    plt.figure()
    for inx in range(len(Country_Codes)):
        Country_data = data.loc[inx, Country_Codes[inx]]
        plt.plot(Years, country_data, label=country_codes[inx])
    # Adding title to the graph and labels to axis
    plt.title('Infant Mortality Rate in Major Europe Countries from 1970 to 2020')
    plt.xlabel('Years')
    plt.ylabel('Infant Mortality rate (per 1,000 live births)')

    # Adding legend
    plt.legend()

    # Display the plot
    plt.show()

# Calling functions to read and create line plot
file_path = r'C:\Users\Avinash Reddy\Videos\Harsha Assignment\reduceddata.csv'
ReadFile(file_path)
Create_Line_Plot(Country Code,3,)



