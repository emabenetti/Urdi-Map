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
# Se guarda el objeto GeoJson en la variable manzanas para despues seguir agregando cosas
manzanas = folium.GeoJson(cuadras, name="Manzanas").add_to(m)

# Se le agrega un popup a la capa manzanas para cuando el usuario hace click
# Se pasa como parámetros la lista de propiedades en el json de cuadras
# TODO Se puede usar HTML para dejarlo mas presentable.
folium.features.GeoJsonPopup(fields=['id','Sector','Uso_suelo','EDIF'], labels=False).add_to(manzanas)

# Agrego como opcion usar Open Street Map en vez de CartoDB Positron
folium.TileLayer('openstreetmap').add_to(m)

# Se crea el grupo de controles de capa y se agrega al mapa
folium.LayerControl().add_to(m)

# Esta funcion genera el archivo html con todo lo necesario para mostrar el mapa en el navegador
m.save('index.html')