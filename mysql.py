from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

db_connection_str = 'mysql+pymysql://root:1234@localhost/cwsalpha'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT stocks_itemcode, created_at FROM stocks', con=db_connection)
#a = ['branchname', 'staff_name']
#ax = pd.Series(a)
#df.columns = ax
#df = df.drop(columns=['id'])

#df['full_name'] = df['first_name'] + ' ' + df['last_name']
#print(df.tail(10))
#print(df)
#df['created_at'] = pd.to_datetime(df['created_at'])


#df.to_csv('/Users/AzamMacX/Documents/Python/staffs.csv', index=False)

#df['stocks_itemcode'] = pd.to_numeric(df['stocks_itemcode'], errors='coerce')

# Remove rows where created_at is empty
#invalid_rows = df[pd.to_datetime(df['created_at'], errors='coerce').isna()]

# Display the invalid rows
#print(invalid_rows)
#df = df.dropna(subset=['created_at'])
# Plotting stocks_itemcode against created_at
df['created_at'] = pd.to_datetime(df['created_at'])  # Ensure created_at is in datetime format


# Group the data by week and count the occurrences of stocks_itemcode
counts = df.set_index('created_at').resample('W')['stocks_itemcode'].count()

# Plot the counts as a line chart
counts.plot(kind='line', title='Stocks Item Code Count (Weekly)')

# Set x-axis labels for weekly intervals
plt.xticks(counts.index, rotation=45, ha='right')  # Rotate for better readability

# Add labels to the axes
plt.xlabel('Week')
plt.ylabel('Stocks Item Code Count')

# Display the plots
plt.show()