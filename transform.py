#import libraries that i will use
import pandas as pd
import numpy as np
def transform_data(data, categorical_cols=None):
    """Encodes categorical variables in the data.

    Args:
        data (pandas.DataFrame): Input data.
        categorical_cols (list, optional): List of categorical column names. Defaults to None.

    Returns:
        pandas.DataFrame: Data with encoded categorical variables.
    """

    if categorical_cols is None:
        categorical_cols = data.select_dtypes(include=["object"]).columns

    data = pd.get_dummies(data, columns=categorical_cols)

    return data