import pandas as pd

def clean_data(data, strategy="mean", axis=0, numeric_only=True, categorical_strategy="mode", remove_duplicates=True):
    
    """Handles missing values in a DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame to process.
        strategy (str, optional): Imputation strategy for numeric columns (e.g., 'mean', 'median', 'mode', 'ffill', 'bfill'). Defaults to 'mean'.
        axis (int, optional): Axis along which to operate (0 for rows, 1 for columns). Defaults to 0.
        numeric_only (bool, optional): Whether to apply the imputation only to numeric columns. Defaults to True.
        categorical_strategy (str, optional): Imputation strategy for categorical columns (e.g., 'mode', 'most_frequent', 'constant'). Defaults to 'mode'.

    Returns:
        pd.DataFrame: DataFrame with missing values handled.
    """

    if numeric_only:
        numeric_columns = data.select_dtypes(include=['number']).columns
        data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
    else:
        for column in data.columns:
            if data[column].dtype.name == 'object':  # Check if column is categorical
                if categorical_strategy == "mode":
                    mode_value = data[column].mode().iloc[0]  # Handle multiple modes
                    data[column].fillna(mode_value, inplace=True)
                elif categorical_strategy == "most_frequent":
                    data[column].fillna(data[column].value_counts().idxmax(), inplace=True)
                elif categorical_strategy == "constant":
                    data[column].fillna("NA", inplace=True)  # Or other constant value
                else:
                    raise ValueError(f"Invalid categorical strategy: {categorical_strategy}")
            else:  # Numeric column
                if strategy == "remove":
                    data = data.dropna(axis=axis, subset=[column])
                elif strategy == "mean":
                    data[column].fillna(data[column].mean(), inplace=True)
                elif strategy == "median":
                    data[column].fillna(data[column].median(), inplace=True)
                elif strategy == "mode":
                    mode_value = data[column].mode().iloc[0]  # Handle multiple modes
                    data[column].fillna(mode_value, inplace=True)
                elif strategy in ("ffill", "bfill"):
                    data[column].fillna(method=strategy, inplace=True)
                else:
                    raise ValueError(f"Invalid strategy: {strategy}")

    return data