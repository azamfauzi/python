import pyarrow as pa
import requests

import pyarrow.parquet as pq
# Fetch the proto file from the URL
url = "https://api.data.gov.my/gtfs-realtime/vehicle-position/ktmb"
response = requests.get(url)

# Save the proto file locally
with open("vehicle_position.proto", "wb") as file:
    file.write(response.content)

print("Proto file downloaded: vehicle_position.proto")
