from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract five days from the current date
new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Date five days ago:", new_date)

from datetime import datetime, timedelta

# Get today's date
today = datetime.now().date()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

from datetime import datetime

# Get the current datetime with microseconds
current_datetime = datetime.now()

# Drop microseconds
datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("Current datetime with microseconds:", current_datetime)
print("Current datetime without microseconds:", datetime_without_microseconds)


from datetime import datetime

# Define two datetime objects
datetime1 = datetime(2023, 6, 20, 12, 0, 0)
datetime2 = datetime(2023, 6, 21, 14, 30, 0)

# Calculate the difference in seconds
time_difference = (datetime2 - datetime1).total_seconds()

print("Difference in seconds:", time_difference)