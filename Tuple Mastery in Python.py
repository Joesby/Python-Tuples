#Task 1: Formatting Flight Itineraries
#Create a function that takes a list of tuples as an argument
#Each tuple contains information about a flight itinerary (name, origin, destination)
def Flight_Itinerary(list_of_tuples):
    for i in range(len(list_of_tuples)):
        name, origin, destination = list_of_tuples[i]
        print(f"Itinerary {i + 1}: {name} - From {origin} to {destination}")

#provide a list of itineraries in the form of tuples
itineraries_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Joe", "Kansas City", "Los Angeles")]
#call the function, passing the list of itineraries in as an argument
Flight_Itinerary(itineraries_list)