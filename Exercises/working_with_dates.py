from datetime import datetime
import pytz
from pytz import timezone
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, WEEKLY
from dateutil import parser

now = datetime.now()

def parse_dates():
    d1 = datetime.strptime("07-05-2025", "%d-%m-%Y")
    d2 = datetime.strptime("May 7, 2025 2:30 PM", "%B %d, %Y %I:%M %p")
    d3 = datetime.strptime("2025/05/07 14:30:00", "%Y/%m/%d %H:%M:%S")
    print("\nParsed dates:", d1, d2, d3)

def format_dates():
    print("\nMonth-Day-Year:", now.strftime("%m-%d-%Y"))
    print("Hour:Minute AM/PM:", now.strftime("%I:%M %p"))
    print("Log Timestamp:", now.strftime("[%d/%b/%Y:%H:%M:%S]"))

def get_time():
    utc_now = datetime.now(pytz.utc)
    print("\nUTC Time:", utc_now)
    la_tz = timezone("America/Los_Angeles")
    local_time = utc_now.astimezone(la_tz)
    print("Los Angeles Time:", local_time)

def time_difference():
    date1 = datetime.strptime("2025-05-07", "%Y-%m-%d")
    date2 = datetime.strptime("2025-12-25", "%Y-%m-%d")
    days_between = (date2 - date1).days
    print("\nDays between May 7 and Dec 25, 2025:", days_between)

def timezone_convert():
    dt_utc = datetime.now(pytz.utc)
    tokyo = dt_utc.astimezone(timezone("Asia/Tokyo"))
    paris = dt_utc.astimezone(timezone("Europe/Paris"))
    print("\nUTC:", dt_utc.isoformat())
    print("Tokyo Time:", tokyo.isoformat())
    print("Paris Time:", paris.isoformat())

def later_time(str1, str2):
    dt1 = parser.parse(str1)
    dt2 = parser.parse(str2)
    return str1 if dt1 > dt2 else str2

def time_delta():
    three_weeks = now + relativedelta(weeks=3)
    print("\nToday's date: ", now)
    print("Date in 3 weeks from today: ", three_weeks)
    three_months_ago = now - relativedelta(months=3)
    print("Date 3 months ago from today: ", three_months_ago)

if __name__ == '__main__':
    parse_dates()
    format_dates()
    get_time()
    time_difference()
    timezone_convert()
    dt_later = later_time("2025-05-07T14:30:00", "2025-05-07T16:00:00")
    print("\nPrint later time of '2025-05-07T14:30:00' and '2025-05-07T16:00:00':")
    print(dt_later)
    time_delta()
