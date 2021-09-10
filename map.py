import folium

# define donde estan los archivos .geojson y se guardan en variables
cuadras_info = f"geojson/Manzanas_Urd.geojson"
lotes_info = f"geojson/Lotes_Urdi_1905.geojson"
curvas_info = f"geojson/Curvas_nivel_Urdi.geojson"

# Esto crea un objeto mapa con las coordenadas y el zoom que le indiquemos
# Para este proyecto uso las coordenadas aproximadas del parque de la ciudad y un zoom de 16
# tiles se usa para elegir el motor de mapa predeterminado. En la doc de Folium estan todos los disponibles
m = folium.Map(
    location=[-32.6859,-58.8910],
    tiles="cartodbpositron",
    zoom_start=15,
)

style1 = {'fillColor': '#228B22', 'color': '#2a9d8f'}
style2 = {'fillColor': '#00FFFFFF', 'color': '#cb997e'}
style3 = {'fillColor': '#00FFFFFF', 'color': '#6b705c'}

# Folium convierte el GeoJson a un objeto y lo agrega al mapa
# name="" es el nombre que aparece en el menu de capas en la web
# Se guarda el objeto GeoJson en la variable manzanas para despues seguir agregando cosas
manzanas = folium.GeoJson(cuadras_info, name="Manzanas", style_function=lambda x:style1).add_to(m)
lotes = folium.GeoJson(lotes_info, name="Lotes de 1905", style_function=lambda x:style3).add_to(m)
curvas = folium.GeoJson(curvas_info, name="Curva de nivel", style_function=lambda x:style2).add_to(m)

# Se le agrega un popup a la capa manzanas para cuando el usuario hace click
# Se pasa como parámetros la lista de propiedades en el json de cuadras
# TODO Se puede usar HTML para dejarlo mas presentable.
folium.features.GeoJsonPopup(aliases=['Codigo parcelario: ', 'Tipo de parcela: ', 'Autoridad de fuente: ', 'Area: '], fields=['CCA','TPA','SAG','ARA'], labels=True).add_to(manzanas)
folium.features.GeoJsonPopup(aliases=['Altura de curva de nivel: ', 'HQC: ', 'MO2: ', 'Autoridad de fuente: '], fields=['ALT','HQC','MO2','SAG'], labels=True).add_to(curvas)
folium.features.GeoJsonPopup(aliases=['Codigo parcelario: ', 'Tipo de parcela: ', 'Area: ', 'Fecha construccion: '], fields=['CCA','TPA','ARA','f_const'], labels=True).add_to(lotes)

# Agrego como opcion usar Open Street Map en vez de CartoDB Positron
folium.TileLayer('openstreetmap').add_to(m)

# Se crea el grupo de controles de capa y se agrega al mapa
folium.LayerControl().add_to(m)

# Esta funcion genera el archivo html con todo lo necesario para mostrar el mapa en el navegador
m.save('index.html')