# Module that creates map with the information about filming locations
import folium
from continents import africa, europe, asia, america


def create_map():
    map_movies = folium.Map()

    fg_europe = folium.FeatureGroup(name='Europe')
    fg_america = folium.FeatureGroup(name="America")
    fg_other = folium.FeatureGroup(name='Other')
    fg_africa = folium.FeatureGroup(name='Africa')
    fg_asia = folium.FeatureGroup(name="Asia")

    with open("coordinates.txt", "r") as f:
        data = f.readlines()
        for line in data:
            coordinates = line.split("(")[1][:-2].split(",")
            location = line.split("\t\t")[0]
            if location.split()[-1] in europe:
                fg_europe.add_child(folium.Marker(location=[float(coordinates[0]), float(coordinates[1])],
                                                  popup=folium.Popup(location, parse_html=True),
                                                  icon=folium.Icon(color='red')))
            elif location.split()[-1] in africa:
                fg_africa.add_child(folium.Marker(location=[float(coordinates[0]), float(coordinates[1])],
                                                  popup=folium.Popup(location, parse_html=True),
                                                  icon=folium.Icon(color='green')))
            elif location.split()[-1] in asia:
                fg_asia.add_child(folium.Marker(location=[float(coordinates[0]), float(coordinates[1])],
                                                popup=folium.Popup(location, parse_html=True),
                                                icon=folium.Icon(color='orange')))
            elif location.split()[-1] in america:
                fg_america.add_child(folium.Marker(location=[float(coordinates[0]), float(coordinates[1])],
                                                   popup=folium.Popup(location, parse_html=True),
                                                   icon=folium.Icon(color='blue')))
            else:
                fg_other.add_child(folium.Marker(location=[float(coordinates[0]), float(coordinates[1])],
                                                 popup=folium.Popup(location, parse_html=True),
                                                 icon=folium.Icon(color='purple')))
    map_movies.add_child(fg_africa)
    map_movies.add_child(fg_europe)
    map_movies.add_child(fg_other)
    map_movies.add_child(fg_asia)
    map_movies.add_child(fg_america)

    map_movies.add_child(folium.LayerControl())

    map_movies.save("Map_movies.html")


create_map()
