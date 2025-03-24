import pyarrow as pa

import pyarrow.parquet as pq

# Create a PyArrow Table
data = {
    'column1': [1, 2, 3],
    'column2': ['a', 'b', 'c'],
    'column3': [4.5, 5.5, 6.5]
}
table = pa.table(data)

# Write the table to a Parquet file
pq.write_table(table, 'example.parquet')
print("Parquet file written: example.parquet")

# Read the Parquet file back into a PyArrow Table
read_table = pq.read_table('example.parquet')
print("Read Parquet file:")
print(read_table)