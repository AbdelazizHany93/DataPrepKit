import pandas as pd

def load_data(file_path, file_type):
  """Loads data from a CSV, XLSX, or JSON file.

  Args:
    file_path (str): Path to the data file.
    file_type (str): File extension (e.g., "csv", "xlsx", "json").

  Returns:
    pandas.DataFrame: Loaded data.

  Raises:
    FileNotFoundError: If the file path is incorrect or the file does not exist.
    ValueError: If the file type is not supported.
  """

  try:
    if file_type == "csv":
      data = pd.read_csv(file_path)
    elif file_type == "xlsx":
      data = pd.read_excel(file_path)
    elif file_type == "json":
      data = pd.read_json(file_path)
    else:
      raise ValueError("Unsupported file type")

    # Validate data types and ranges (if necessary)
    # ...

    return data

  except FileNotFoundError:
    raise FileNotFoundError(f"File not found: {file_path}")
