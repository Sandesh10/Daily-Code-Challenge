'''
Given an unordered list of flights taken by someone, each represented
as (origin, destination) pairs, and a starting airport, compute the
person's itinerary. If no such itinerary exists, return null. If there
are multiple possible itineraries, return the lexicographically smallest
one. All flights must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'),('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL',
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
and starting airport 'A', you should return
the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C']
is also a valid itinerary.
However, the first one is lexicographically smaller.
'''

def check_flight(flight_list, current):
    temp = []
    for flight in flight_list:
        if flight[0]==current:
            temp.append(flight[1])
    if len(temp)>1:
        return sorted(temp)
    return temp

def flight_ordering(flight_list, start):
    current = start
    places = []
    while len(flight_list)>0:
        next_dest = check_flight(flight_list,current)
        if next_dest== []:
            return None
        places.append(current)
        flight_list.remove((current,next_dest[0]))
        current = next_dest[0]
    places.append(current)    
    return places

print(flight_ordering([('SFO', 'COM'), ('COM', 'YYZ')] ,'COM'))
            
