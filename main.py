#import libraries that i will use
import pandas as pd
import numpy as np
import sys
sys.path.append(".")  # Add the current directory to the Python search path (optional)
import dataprepkit.load as load
import dataprepkit.explore as explore
import dataprepkit.clean as clean
import dataprepkit.transform as transform

# Example usage
file_path = "path"  # Replace with your data file path
file_type = "Extention"  # or "xlsx", "json" #Replace with extenion of file

#load data
data = load.load_data(file_path, file_type)

explore.explore_data(data)   # Explore the data
clean.clean_data(data, strategy="mean")  # # Clean the data and Use your preferred strategy
transform.transform_data(data)# Transform the data

# Now you can use the cleaned and transformed data for further analysis
print("Data after processing:")
print(data.head())  # Display the first few rows
