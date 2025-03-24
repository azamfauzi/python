import pandas as pd

# Example usage of pandas
# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
data = pd.read_parquet('https://storage.data.gov.my/healthcare/nutrition_status_u5_sex.parquet')

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
