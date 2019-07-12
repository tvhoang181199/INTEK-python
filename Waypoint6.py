from python_basic import *

#WP6
hotel_daily_rates = [    ('Majestic Saigon Hotel', 93),
    ('Hotel Grand Saigon', 80),
    ('Sofitel Saigon Plaza', 123),
    ('Hotel Continental', 62),
    ('Caravelle Hotel', 180),
    ('Sheraton Saigon Hotel', 216),
    ('Park Hyatt Saigon', 209)
]

for i in range(0, len(hotel_daily_rates)):
	print(hotel_daily_rates[i])

n = int(input("Enter n:   "))
print(find_cheapest_hotels(hotel_daily_rates, n))
