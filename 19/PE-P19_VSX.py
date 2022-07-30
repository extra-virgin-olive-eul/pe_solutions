#!/usr/bin/python3

'''
Program:     PE-P19_VSX.py
Author:      vsx-gh (https://github.com/vsx-gh)
Created:     20220730

Project Euler Problem 19:
	You are given the following information, but you may prefer to do some research for
	yourself.

		* 1 Jan 1900 was a Monday.
		* Thirty days has September,
		  April, June and November.
		  All the rest have thirty-one,
	      Saving February alone,
		  Which has twenty-eight, rain or shine.
	      And on leap years, twenty-nine.

	A leap year occurs on any year evenly divisible by 4, but not on a century unless it
	is divisible by 400. How many Sundays fell on the first of the month during the
	twentieth century (1 Jan 1901 to 31 Dec 2000)?

OMFG the off-by-one errors with this one.....
'''

import argparse
import sys
import datetime

def is_leap_year(year_in):
	"""
	Determines if year_in is a leap year, in which February has 29 days
	"""

	feb_len = 28

    # Early out
	if year_in % 4 != 0:
		return feb_len

    # Check century marker
	if year_in % 100 != 0:
		return feb_len + 1
	else:
		if year_in % 400 == 0:
			return feb_len + 1
		else:
			return feb_len



def year_len_days(input_year):
    """
    Determines length of {input_year} in days
    """

    # Find number of days in February
    feb_len = is_leap_year(input_year)

    year_total_days = jan_len + feb_len + mar_len + apr_len + may_len + jun_len \
                    + jul_len + aug_len + sep_len + oct_len + nov_len + dec_len

    return year_total_days



def find_month_starts(check_year):
    """
    Finds the start position for each month of {check_year}
    """
    feb_len = is_leap_year(check_year)
    months_list = [jan_len, feb_len, mar_len, apr_len, may_len, jun_len, \
                jul_len, aug_len, sep_len, oct_len, nov_len, dec_len]

    month_starts = []
    days_this_year = year_len_days(check_year)
    days_tot = 0

    # January 1
    month_starts.append(0)

    # Beginning of other months of the year
    for item in range(0, len(months_list) - 1, 1):
        days_tot += months_list[item]
        month_starts.append(days_tot)

    return month_starts



def convert_doy_month(num_doy, months_starts):
    """
    Converts numbered day of year {num_doy} to month in which it falls
    """

    for month_start in months_starts:
        if num_doy > month_start:
            continue
        else:
            return months_starts.index(month_start)



def year_dow(curr_year, start_dow):
    """
    Assign day of week to every day in year - FORWARD
    """

    curr_year_len = year_len_days(curr_year)
    year_start_day = weekday_list.index(start_dow)

    # First portion is remainder of weekday list, such as Wed->Sat
    year_dow_list = weekday_list[year_start_day:]

    # Trim off days we just used
    seed_len = curr_year_len - len(year_dow_list)

    # Number of full weeks in year
    num_weeks = int((seed_len) / len(weekday_list))
    year_dow_list += weekday_list * num_weeks

    # Leftover days/partial week
    remainder_days = (seed_len) % len(weekday_list)
    year_dow_list += weekday_list[0:remainder_days]

    return year_dow_list



def find_curr_year_start_dow():
    """
    Find weekday of January 1 of current year - BACKWARD
    """

    intl_weekday_pos = datetime.datetime.weekday(today)
    today_weekday = weekday_list.index(weekday_list_intl[intl_weekday_pos])
    this_month_starts = find_month_starts(today.year)

    # Find today's position in zero-indexed list
    today_doy = this_month_starts[today.month - 1] + today.day

    # Find portion of weekday list for this (probably partial) week
    curr_dow_list = weekday_list[0:(today_weekday + 1)]

    # Get full weeks
    seed_len = today_doy - len(curr_dow_list)
    num_weeks = int((seed_len) / len(weekday_list))
    whole_weeks = weekday_list * num_weeks

    # Get partial list of weekdays at beginning of month, if any
    remainder_days = (seed_len) % len(weekday_list)
    if remainder_days > 0:
        first_week = weekday_list[(len(weekday_list) - remainder_days):]
        year_dow_list = first_week + whole_weeks + curr_dow_list
    else:
        year_dow_list = whole_weeks + curr_dow_list

    return weekday_list.index(year_dow_list[0])



def find_year_start_dow(end_dow_pos, year_item):
    """
    Find weekday of January 1 of {year_item} - BACKWARD
    """

    # Hold days of the week for this year
    year_dow_list = []

    # Get partial weekdays from end of year
    curr_year_len = year_len_days(year_item)
    curr_dow_list = weekday_list[0:(end_dow_pos)]

    # Get full weeks
    seed_len = curr_year_len - len(curr_dow_list)
    num_weeks = int((seed_len) / len(weekday_list))
    whole_weeks = weekday_list * num_weeks

    # Get remainining weekdays for beginning of year, if any
    remainder_days = (seed_len) % len(weekday_list)
    if remainder_days > 0:
        first_week = weekday_list[(len(weekday_list) - remainder_days):]
        year_dow_list = first_week + whole_weeks + curr_dow_list
    else:
        year_dow_list = whole_weeks + curr_dow_list

    return year_dow_list[0], year_dow_list



# Set some helpful time parameters
today = datetime.datetime.now()
weekday_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', \
                'Friday', 'Saturday']
months_list_long = ['January', 'February', 'March', 'April', 'May', 'June', \
                'July', 'August', 'September', 'October', 'November', 'December']

# Get input(s)
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--beginyear',
                    required=True,
                    type=int,
                    help='Input start year',
                    )
parser.add_argument('-e', '--endyear',
                    required=True,
                    type=int,
                    help='Input end year',
                    )
parser.add_argument('-w', '--weekday',
                    required=True,
                    choices=weekday_list,
                    help='Day of week for which to search',
                    )
parser.add_argument('-d', '--debugyear',
                    required=False,
                    type=int,
                    help='Enter year to spot-check start and end DOW',
                    )
parser.add_argument('-v', '--doverbose',
                    required=False,
                    action='store_true',
                    help='Output matches',
                    )
all_args = parser.parse_args()
start_year = all_args.beginyear
end_year = all_args.endyear
find_weekday = all_args.weekday
debug_year = all_args.debugyear
do_verbose = all_args.doverbose

# Check inputs
if start_year > end_year:
    print('ERROR: Start year after end year.')
    sys.exit(-1)
if end_year > today.year:     # Makes finding DOW start point harder
    print('ERROR: End year after current year.')
    sys.exit(-1)
if debug_year and (debug_year < start_year or debug_year > end_year):
    print('ERROR: Debug year out of range {start_year}:{end_year}.')

# Putting Monday first?! I hate you, datetime.
# Yes, I understand this is for international purposes. Still sucks.
weekday_list_intl = weekday_list[1:] + [weekday_list[0]]

# Set number of days in each month
jan_len = mar_len = may_len = jul_len = aug_len = oct_len = dec_len = 31
apr_len = jun_len = sep_len = nov_len = 30

# Find first day of this (current) year, given you can find the last
first_dow = find_curr_year_start_dow()
for year_item in range(today.year - 1, start_year - 1, -1):
    # Working backwards, find first day of each year
    year_beg_day, year_dows = find_year_start_dow(first_dow, year_item)
    first_dow = weekday_list.index(year_beg_day)

    if debug_year is not None and year_item == debug_year:
        print(f'Year {year_item} began on a {year_dows[0]}, ended on a {year_dows[-1]}')

weekday_fom = 0     # First-of-months matching selected weekday
first_dow_str = weekday_list[first_dow]    # Prime first day of {start_year}

# Move forward, mapping weekdays for each year
for check_year in range(start_year, end_year + 1, 1):
    # Get first day of year
    this_year_weekdays = year_dow(check_year, first_dow_str)
    starts_of_months = find_month_starts(check_year)

    for month_start in starts_of_months:
        if this_year_weekdays[month_start] == find_weekday:
            month_pos = convert_doy_month(month_start, starts_of_months)
            weekday_fom += 1

            # Perform check and output matches - month starts are weekday you chose
            if do_verbose:
                print(f'{months_list_long[month_pos]} 1, {check_year}: '\
                f'{weekday_list_intl[datetime.date(year=check_year, month=(month_pos + 1), day=1).weekday()]}')

    # Move to first of next year
    advance_pos = weekday_list.index(this_year_weekdays[-1]) + 1  
    if advance_pos < len(weekday_list):
        next_weekday_pos = advance_pos
    else:
        next_weekday_pos = 0
    first_dow_str = weekday_list[next_weekday_pos]

# Output results
print(f'Number of {find_weekday}s on first of the month from {start_year} to {end_year}: {weekday_fom}')
