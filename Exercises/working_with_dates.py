from datetime import datetime
import pytz
from pytz import timezone
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, WEEKLY

now = datetime.now()

# Exercise 1: Parse Dates
# Use strptime() to parse:
# "07-05-2025" as dd-mm-yyyy
d1 = datetime.strptime("07-05-2025", "%d-%m-%Y")
# "May 7, 2025 2:30 PM" to a datetime object
d2 = datetime.strptime("May 7, 2025 2:30 PM", "%B %d, %Y %I:%M %p")
# "2025/05/07 14:30:00" using %Y/%m/%d %H:%M:%S
d3 = datetime.strptime("2025/05/07 14:30:00", "%Y/%m/%d %H:%M:%S")

print("Parsed dates:", d1, d2, d3)



# Exercise 2: Format Dates
# Use strftime() to format:
# Today's date in "MM-DD-YYYY"
print("Month-Day-Year:", now.strftime("%m-%d-%Y"))
# Current time as "Hour:Minute AM/PM"
print("Hour:Minute AM/PM:", now.strftime("%I:%M %p"))
# Log-style timestamp like "[07/May/2025:14:30:00]"
print("Log Timestamp:", now.strftime("[%d/%b/%Y:%H:%M:%S]"))

# Exercise 3: Get UTC and Local Time
# Print the current UTC time using datetime.now(tz=...).
utc_now = datetime.now(pytz.utc)
print("UTC Time:", utc_now)
# Convert it to "America/Los_Angeles" time.
la_tz = timezone("America/Los_Angeles")
local_time = utc_now.astimezone(la_tz)
print("Los Angeles Time:", local_time)

# Exercise 4: Time Difference
# Calculate the number of days between "2025-05-07" and "2025-12-25".
date1 = datetime.strptime("2025-05-07", "%Y-%m-%d")
date2 = datetime.strptime("2025-12-25", "%Y-%m-%d")
days_between = (date2 - date1).days
print("Days between May 7 and Dec 25, 2025:", days_between)

# Exercise 5: Timezone Conversion
# Create a datetime in UTC.
dt_utc = datetime.now(pytz.utc)
# Convert it to "Asia/Tokyo" and "Europe/Paris".
tokyo = dt_utc.astimezone(timezone("Asia/Tokyo"))
paris = dt_utc.astimezone(timezone("Europe/Paris"))

print("UTC:", dt_utc.isoformat())
print("Tokyo Time:", tokyo.isoformat())
print("Paris Time:", paris.isoformat())


# Exercise 6: Datetime Comparison
# Write a function that takes two strings in ISO format
# and returns the one that represents the later time.
# def later_time(str1, str2)
#     dt1 =


# Exercise 7: Timedelta
# Find and print in ISO format today's date and a date 3 weeks from now
#
# Find and print in ISO format today's date and a date 3 month ago
#
