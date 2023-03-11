"""
Suppose, we are given two timestamps - for example, when the train or ferry boat starts its travel and when it finishes.
This may look like:
start: May 3, 17:08:30
end  : May 8, 12:54:15

and we are curious to know, how much time (in days, hours, minutes and seconds)
 is spent in traveling (perhaps, to choose faster variant). How this could be achieved?

One of the easiest way is:
    - convert both timestamps to big numbers, representing seconds from the beginning of the month (or year, or century);
    - calculate their difference - i.e. travel time in seconds;
    - convert this difference back to days, hours, minutes and seconds.

Input data:
    the first line contains number of test-cases, other lines contain test-cases themselves.
    Each test-case contains 8 numbers, 4 for each timestamp:
        day1 hour1 min1 sec1 day2 hour2 min2 sec2 (second timestamp will always be later than first).

    3
    1 0 0 0 2 3 4 5
    5 3 23 22 24 4 20 45
    8 4 6 47 9 11 51 13

Answer:
    for each test-case you are to output difference as following (days hours minutes seconds)
     please note brackets - separated by spaces.

    (1 3 4 5) (19 0 57 23) (1 7 44 26)
"""

from datetime import timedelta


class Calculation:

    def __init__(self):
        self.result = []

    def seconds_count(self):
        day1, hour1, min1, sec1, day2, hour2, min2, sec2 = map(int, input().split())
        datetime1 = timedelta(days=day1, hours=hour1, minutes=min1, seconds=sec1).total_seconds()
        datetime2 = timedelta(days=day2, hours=hour2, minutes=min2, seconds=sec2).total_seconds()
        x = datetime2 - datetime1

        minutes, seconds = divmod(x, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        self.result.append(f"({int(days)} {int(hours)} {int(minutes)} {int(seconds)})")

    def conversion_back(self):
        for _ in range(int(input())):
            self.seconds_count()
        print(*self.result)


if __name__ == '__main__':
    run = Calculation()
    run.conversion_back()
