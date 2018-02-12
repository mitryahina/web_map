# web_map

This project is created to analyze IMDB in order to create the map of the most popular filming locations

It includes such modules:
get_files.py - extracts locations from the file locations.list and finds their coordinates, which are then written to coordinates.txt
map_movies.py - uses folium to create an html map using coordinates from coordinates.txt
Map_movies.html - the result of analisys
