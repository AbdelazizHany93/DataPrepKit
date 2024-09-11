#import libraries that i will use
import pandas as pd
import numpy as np
## Display all the columns of the dataframe
pd.pandas.set_option('display.max_columns',None)

"""Read data from a CSV file."""
def load_data(file_path,file_type):
    if file_type=="csv":
        data=pd.read_csv(file_path)
    elif file_type=="xlsx":
        data=pd.read_excel(file_path)
    elif file_type=="json":
        data=pd.read_json(file_path)
    return data