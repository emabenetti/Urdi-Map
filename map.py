import folium

# define donde esta el archivo .geojson y lo guarda en una variable
cuadras = f"cuadras.geojson"

# Esto crea un objeto mapa con las coordenadas y el zoom que le indiquemos
# Para este proyecto uso las coordenadas aproximadas del parque de la ciudad y un zoom de 16
# tiles se usa para elegir el motor de mapa predeterminado. En la doc de Folium estan todos los disponibles
m = folium.Map(
    location=[-32.6859,-58.8910],
    tiles="cartodbpositron",
    zoom_start=15,
)

# Folium convierte el GeoJson a un objeto y lo agrega al mapa
# name="" es el nombre que aparece en el menu de capas en la web
folium.GeoJson(cuadras, name="Manzanas").add_to(m)

# Agrego como opcion usar Open Street Map en vez de CartoDB Positron
folium.TileLayer('openstreetmap').add_to(m)

# Se crea el grupo de controles de capa y se agrega al mapa
folium.LayerControl().add_to(m)

# Esta funcion genera el archivo html con todo lo necesario para mostrar el mapa en el navegador
m.save('index.html')