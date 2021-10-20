
"""Question 3 - Write a python program that makes use of a generator that produces a list of dates
between two dates."""

from datetime import date
from datetime import timedelta
import timeit

# This creates a generator then iterates through it

def print_date_range(firstdate, lastdate):
    def generate_date_range(firstdate, lastdate):
        i = firstdate
        while i < lastdate:
            yield i
            i += timedelta(days=1)
    for i in generate_date_range(firstdate, lastdate):
        print(i)

# Meeting the question requirement

gstarttime = timeit.default_timer()
print_date_range(date(1020, 1, 1), date(2030, 2, 5))
gendtime = timeit.default_timer()

# Timing the function, compared with a while loop

def pdr_for_loop(firstdate, lastdate):
    i = firstdate
    while i < lastdate:
        print(i)
        i += timedelta(days=1)

wstarttime = timeit.default_timer()
pdr_for_loop(date(1020, 1, 1), date(2030, 2, 5))
wendtime = timeit.default_timer()

print('Time taken for generator :', gendtime-gstarttime)
print('Time taken for while loop :', wendtime-wstarttime)

'''Results when I ran it for a 1000 year period
Time taken for generator : 2.701644666
Time taken for while loop : 2.7765498250000005
'''