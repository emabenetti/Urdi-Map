import folium

# Create map object
m = folium.Map(location=[-32.6859,-58.8910], zoom_start=16)

# Generate map
m.save('map.html')