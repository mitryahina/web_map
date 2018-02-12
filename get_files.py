# This module reads file from IMDB containing films and their filming locations
# The file with locations and their coordinates is created
import googlemaps


def read_file(path):
    """
    (str)-> list
    Return list of lines from file
    """
    # open file
    with open(path, "r", encoding='utf-8', errors='ignore') as f:
        data = f.readlines()
        data = data[14: -1]
        films = set()
        for line in data:
            line = line.strip()
            # extract information from lines
            name = line[: line.index('(') - 1]
            country = line[line.index('\t') + 1:].strip()
            year = line[line.index('(') + 1: line.index('(') + 5]
            try:
                if year == "????" or int(year):
                    films.add((name, year, country))
            except ValueError:
                pass
        return films


def get_locations(films):
    """
    Function, that takes list of films and returns the set of locations
    """
    locations_set = set()
    for film in films:
        location = film[2]
        if "\t" in location:
            location = location.split("\t")[0]
        locations_set.add(location)
    return locations_set


def get_locations_dict(locations):
    """
    Function that takes set of location and writes to file the location and its
    coordinates using Google API
    """
    f = open("coordinates.txt", "a")
    locations_dict = {}
    for location in locations:
        if location not in locations_dict:  # to prevent repetition of same locations
            try:
                gmaps = googlemaps.Client(key="AIzaSyCrzgL6a4wlLUu5Q6Y4n8Tmp98DP-Yay1o")
                coordinates = gmaps.geocode(location)[0].get('geometry').get('location')
                locations_dict[location] = (coordinates['lat'], coordinates['lng'])
                val = str(location) + "\t\t" + str(locations_dict[location]) + '\n'
                f.write(val)
            except IndexError:
                pass
    f.close()


if __name__ == '__main__':
    locations = get_locations(read_file("locations.list"))
    locations_dict = get_locations_dict(locations)
