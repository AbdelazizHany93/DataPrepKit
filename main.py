#import libraries that i will use
import pandas as pd
import numpy as np
import sys
sys.path.append(".")  # Add the current directory to the Python search path (optional)

# Import the functions from your DataPrepKit package
import dataprepkit.load as load
import dataprepkit.explore as explore
import dataprepkit.clean as clean
import dataprepkit.transform as transform

# Example usage
file_path = "C:\\Users\Abdelaziz_Hany\\Desktop\\Alcamp\\Python\\DataPrep\\Datasets\\Employee Sample Data.xlsx"  # Replace with your data file path
#file_path = "C:\\Users\Abdelaziz_Hany\\Desktop\\Alcamp\\Python\\DataPrep\\Datasets\\boston.csv"  # Replace with your data file path
file_type = "xlsx" #"csv"  # or "xlsx", "json"

data = load.load_data(file_path, file_type)

# Explore the data
explore.explore_data(data)


# Clean the data
data = clean.clean_data(data, strategy="mean")  # Use your preferred strategy

# Transform the data
data = transform.transform_data(data)

# Now you can use the cleaned and transformed data for further analysis
print("Data after processing:")
print(data.head())  # Display the first few rows