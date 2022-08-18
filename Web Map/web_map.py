import folium
import pandas as pd

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

df = pd.read_csv("Volcanoes.txt")

lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df['ELEV'])

# Folium converts python code to JS, CSS, and HTML code.
tiles = "Stamen Terrain"
map = folium.Map(location=[38,-99], zoom_start=5, tiles='openstreetmap')

fg = folium.FeatureGroup(name='My Map')

for lat,lon,elev in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=f"Elevation: {elev}m",radius=6,
                    fill_color=color_producer(elev), color='grey', fill_opacity=.7))


map.add_child(fg)

map.save("Map1.html")
