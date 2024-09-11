#import libraries that i will use
import pandas as pd
import numpy as np 

##def explore_data(data):
def explore_data(data):


  """Prints summary statistics for all common data types in a Pandas DataFrame.

  Args:
    data: A Pandas DataFrame.
  """

  # Get information about column data types
  column_dtypes = data.dtypes

  # Calculate summary statistics for numerical columns (int, float)
  for column in column_dtypes.index:
    if pd.api.types.is_numeric_dtype(data[column]):
      count = data[column].count()
      mean = data[column].mean()
      median = data[column].median()
      mode = data[column].mode().tolist()  # Handle multiple modes
      std_dev = data[column].std()
      variance = data[column].var()
      min_value = data[column].min()
      max_value = data[column].max()
      quantile_25 = data[column].quantile(0.25)
      quantile_75 = data[column].quantile(0.75)

      # Print numerical summary statistics
      print(f"\nSummary Statistics for Numerical Column: {column}")
      print("-" * 40)
      print(f"Count: {count}")
      print(f"Mean: {mean:.2f}")
      print(f"Median: {median:.2f}")
      print(f"Mode: {mode}")
      print(f"Standard Deviation: {std_dev:.2f}")
      print(f"Variance: {variance:.2f}")
      print(f"Minimum: {min_value:.2f}")
      print(f"Maximum: {max_value:.2f}")
      print(f"25th Percentile: {quantile_25:.2f}")
      print(f"75th Percentile: {quantile_75:.2f}")
      print("-" * 40)

  # Calculate summary statistics for categorical columns (object)
  for column in column_dtypes.index:
    if data[column].dtype == 'object':
      value_counts = data[column].value_counts()
      total = value_counts.sum()

      # Print categorical summary statistics
      print(f"\nSummary Statistics for Categorical Column: {column}")
      print("-" * 40)
      print("Value Counts:")
      print(value_counts)
      print(f"Total: {total}")
      print("-" * 40)

  # Calculate summary statistics for datetime columns (datetime64)
  for column in column_dtypes.index:
    if data[column].dtype == 'datetime64[ns]': #changed to datetime64[ns]
      count = data[column].count()
      min_date = data[column].min()
      max_date = data[column].max()
      time_delta = max_date - min_date

      # Print datetime summary statistics
      print(f"\nSummary Statistics for Datetime Column: {column}")
      print("-" * 40)
      print(f"Count: {count}")
      print(f"Minimum Date: {min_date}")
      print(f"Maximum Date: {max_date}")
      print(f"Time Delta: {time_delta}")
      print("-" * 40)

  # Calculate summary statistics for boolean columns (bool)
  for column in column_dtypes.index:
    if data[column].dtype == 'bool':
      value_counts = data[column].value_counts()

      # Print boolean summary statistics
      print(f"\nSummary Statistics for Boolean Column: {column}")
      print("-" * 40)
      print("Value Counts:")
      print(value_counts)
      print("-" * 40)

   