import pandas as pd
import matplotlib.pyplot as plt

def create_bar_chart(path_to_file):
    """
    Generate a bar chart to visualize access to electricity data over multiple years.

    Parameters:
    - path_to_file (str): The file path to the CSV file containing the data.

    Returns:
    returns no values but the bar graph will be generated
    """
    # Load the dataset from the CSV file
    data = pd.read_csv(path_to_file)

    # Get the data of country codes and years
    country_codes = data['World']
    # The data for the years 1980 to 2020 is in columns 2 to 10
    years = list(data.columns[1:10])  

    # Plotting of the bar chart
    plt.figure(figsize=(12, 8))
    for i in range(len(country_codes)):
        plt.bar([x + i for x in range(len(years))], data.iloc[i, 1:10])

    # Adding title and labels to the bar chart
    plt.title('Access to electricity (% of population) - World')
    plt.xlabel('Years')
    plt.ylabel('% of Population')

    # Adding x-axis labels for years
    plt.xticks([i for i in range(len(years))], years)

    # Display the plot
    plt.show()


# Replace 'path_to_file.csv' with the actual path to your CSV file
path_to_file = r'C:\Users\batta\OneDrive\Desktop\ads1\assignments1\AccesstoElec.csv'
create_bar_chart(path_to_file)
