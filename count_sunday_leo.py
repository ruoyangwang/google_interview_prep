


months = [
  31, # jan
  28, # feb
  31, # mar
  30, # apr
  31, # may
  30, # jun
  31, # jul
  31, # ago
  30, # sep
  31, # oct
  30, # nov
  31  # dec
]


def is_leap_year(year):
		return (year%4==0) and (year%400 ==0 or year%100!=0)


def count_sunday():
	year=1901
	day=1
	month=1
	weekday=1
	sundays=0
	while(year<=2000):
		monthdays= months[month-1]
		
		
		if month==2:
			monthdays+=is_leap_year(year)

		if day>monthdays:
			day=1
			month+=1
		
			if month>12:
				month=1
				year+=1

		
		if weekday==7 and month==1:
			sundays+=1
		
		if weekday>7:
			weekday=1

		day+=1
		weekday+=1

	return sundays

print count_sunday()
