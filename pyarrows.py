import pyarrows as pa

data = [
        pa.array([1, 2, 3]),
        pa.array(['A', 'B', 'C']),
    ]
table = pa.Table.from_arrays(data, names=['column1', 'column2'])
print(table)