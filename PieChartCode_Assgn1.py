import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart(path_to_file):
    """
    Generate a pie chart to visualize the distribution of energy provided by major food groups.

    Parameters:
    - path_to_file (str): The file path to the CSV file containing the data.

    Returns:
    returns no values but pie chart will be generated
    """
    # Load the dataset from the CSV file
    data = pd.read_csv(path_to_file)

    # Get the data of Percentages
    percent = data.iloc[:, 1]  # Percentages are in the 1st column.

    # Get the data of Food
    typeof_food = data['Food']

    # Creating a pie chart using the data.
    plt.figure(figsize=(8, 6))
    plt.pie(percent, labels=typeof_food)
    plt.title('Energy provided by major food group in 2000-2002')

    # Display the plot
    plt.show()


# Replace 'path_to_file.csv' with the actual path to your CSV file
path_to_file = r'C:\Users\batta\OneDrive\Desktop\ads1\assignments1\Energy_Chart.csv'
create_pie_chart(path_to_file)
