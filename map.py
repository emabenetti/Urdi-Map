import folium

# define cual es la pagina donde estan alojados los archivos json de datos

url = (
#    "https://emabenetti.github.io/Urdi-Map"
)
cuadras = f"cuadras.geojson"

# Esto crea un objeto mapa con las coordenadas y el zoom que le indiquemos
# Para este proyecto uso las coordenadas aproximadas del parque de la ciudad y un zoom de 16

m = folium.Map(
    location=[-32.6859,-58.8910],
    tiles="cartodbpositron",
    zoom_start=15,
)

folium.GeoJson(cuadras, name="Manzanas").add_to(m)


folium.LayerControl().add_to(m)



m

# Esta funcion genera el archivo html con todo lo necesario para mostrar el mapa en el navegador
m.save('index.html')