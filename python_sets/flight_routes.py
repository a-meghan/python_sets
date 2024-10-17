def flight_routes(airline_1, airline_2):
    dest_in_common = airline_1.intersection(airline_2)
    our_unique = airline_1.difference(airline_2)
    theirs_unique = airline_2.difference(airline_1)
    neither_airline = set()

    print("Our airline & the competition share these destinations: ", dest_in_common)
    print("Our destinations that are unique to us are: ", our_unique)
    print("The destinations unique to our competition are: ", theirs_unique)
    print("Neither airline is going to: ", neither_airline)

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
flight_routes(our_routes, competitor_routes)