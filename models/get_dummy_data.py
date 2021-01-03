import random
from datetime import timedelta


def get_duration_by_stops(stops):
    if stops == 0:
        return random.randint(2, 6)
    elif stops == 1:
        return random.randint(7, 11)
    elif stops == 2:
        return random.randint(11, 18)
    else:
        return random.randint(18, 28)


def get_route(air_from, air_to, stops):
    pet_names = {
        'Chennai': 'MAA',
        'Mumbai': 'BOM',
        'New Delhi': 'DEL',
        'Banglore': 'BLR',
        'Cochin': 'COK',
        'Kolkata': 'CCU',
        'Delhi': 'DEL',
        'Hyderabad': 'HYD',
    }
    mid_sign = ' → '
    route_start = pet_names[air_from]
    route_end = pet_names[air_to]
    del pet_names[air_from]
    del pet_names[air_to]
    list1 = list(pet_names.values())

    if stops == 0:
        mid = mid_sign
    elif stops == 1:
        mid = mid_sign + list1[random.randint(0, 5)] + mid_sign
    elif stops == 2:
        mid = mid_sign + list1[random.randint(0, 2)] + mid_sign + list1[random.randint(3, 5)] + mid_sign
    else:
        mid = mid_sign + list1[random.randint(0, 1)] + mid_sign + list1[random.randint(2, 3)] \
              + mid_sign + list1[random.randint(3, 4)] + mid_sign
    return route_start + mid + route_end


def get_final_data(airline, air_from, air_to, dep):
    final_data = []
    add_info = ['No check-in baggage included', 'In-flight meal not included', 'No info']
    total_stops = ['non-stop', '1 stop', '2 stops', '3 stops']

    for i in range(random.randint(1, 6)):
        stops = random.randint(0, 3)
        departure = dep.replace(hour=random.randint(0, 23), minute=random.randint(0, 59))
        dep_time = str(departure.hour).rjust(2, '0')+':'+str(departure.minute).rjust(2, '0')
        duration_hours = get_duration_by_stops(stops)
        duration_minutes = random.randint(1, 59)
        arrival_datetime = departure + timedelta(hours=duration_hours, minutes=duration_minutes)
        final_data.append({
            'Airline': str(airline),
            'Date_of_Journey': str(dep.strftime("%d/%m/%Y")),
            'Source': air_from,
            'Destination': air_to,
            'Route': get_route(air_from, air_to, stops),
            'Dep_Time': dep_time,
            'Arrival_Time': str(arrival_datetime.hour).rjust(2, '0')+':'+str(arrival_datetime.minute).rjust(2, '0'),
            'Duration': str(duration_hours) + 'h ' + str(duration_minutes) + 'm',
            'Total_Stops': total_stops[stops],
            'Additional_Info': add_info[random.randint(0, 2)]
        })
    return final_data
