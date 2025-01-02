import pandas as pd
import json

#graficos
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.express import choropleth
from plotly import graph_objects as go
from plotly.subplots import make_subplots


#para el mapa del mundo
import folium
from folium import Choropleth

#para el sunburst interactivo
import plotly.express as px

#para cambiar el codigo de pais al nombre
import pycountry


# Archivos json usados 
world_geo = 'json/world_countries.json'
diccionario_paises = 'json/diccionario_paises.json'

# Archivos excel usados
df_pais = pd.read_excel('datasets/df_pais.xlsx')
df_sex_edad = pd.read_excel('datasets/df_sex_edad.xlsx')
df_plat = pd.read_excel('datasets/df_plat.xlsx')
captacion = pd.read_excel('datasets/captacion.xlsx')
registro = pd.read_excel('datasets/registro.xlsx')
venta = pd.read_excel('datasets/venta.xlsx')
captacion_edad = pd.read_excel('datasets/captacion_edad.xlsx')
registro_edad = pd.read_excel('datasets/registro_edad.xlsx')
venta_edad = pd.read_excel('datasets/venta_edad.xlsx')

""""
Aqui inicia los gráficos relacionados a alcance e impresiones por paises

"""

# Gráficos de funnel para alcance e impresiones de las campañas
df_funnel_al = df_pais.groupby('Nombre de la campaña', as_index=False)['Alcance'].sum()
funnel_alcance = px.funnel_area(names=df_funnel_al['Nombre de la campaña'],
                values=df_funnel_al['Alcance'],
                width=700,
                height=500,
                labels=df_funnel_al['Nombre de la campaña'],
                title='Funnel de alcance por campañas'
                )

df_funnel_im = df_pais.groupby('Nombre de la campaña', as_index=False)['Impresiones'].sum()
funnel_impresiones = px.funnel_area(names=df_funnel_im['Nombre de la campaña'],
                    values=df_funnel_im['Impresiones'],
                    width=700,
                    height=500,
                    labels=df_funnel_im['Nombre de la campaña'],
                    title='Funnel de impresiones por campañas'
                    )

#gáfico de barras para comparar alcance e impresiones por paises
#alcance
columnas_alcance = go.Figure(
data=[
    go.Bar(x=captacion['País'], y=captacion['Alcance'], name="Captacion"),
    go.Bar(x=registro['País'], y=registro['Alcance'], name="Registro"),
    go.Bar(x=venta['País'], y=venta['Alcance'], name="Venta"),
],
layout=dict(
    barcornerradius=5,
    height=500,
    barmode='group',
    xaxis_tickangle=-45,
    title='Alcance por Paises para cada Campaña'
    ),
)

#impresiones    
columnas_impresiones = go.Figure(
data=[
    go.Bar(x=captacion['País'], y=captacion['Impresiones'], name="Captacion"),
    go.Bar(x=registro['País'], y=registro['Impresiones'], name="Registro"),
    go.Bar(x=venta['País'], y=venta['Impresiones'], name="Venta"),
],
layout=dict(
    barcornerradius=5,
    height=500,
    barmode='group',
    xaxis_tickangle=-45,
    title='Impresiones por Paises para cada Campaña'
    ),
)

#graficos de pastel para alcance e impresiones por paises
# Alcance
pastel_alcance = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_alcance.add_trace(go.Pie(
                labels=captacion['País'],
                values=captacion['Alcance'],
                name="Captacion"),
                1, 1
             )
pastel_alcance.add_trace(go.Pie(
                labels=registro['País'],
                values=registro['Alcance'],
                name="Registro"),
                1, 2
             )
pastel_alcance.add_trace(go.Pie(
                labels=venta['País'],
                values=venta['Alcance'],
                name="Venta"),
                1, 3
             )
# Use `hole` to create a donut-like pie chart
pastel_alcance.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0

pastel_alcance.update_layout(
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Captacion', x=sum(pastel_alcance.get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Registro', x=sum(pastel_alcance.get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Venta', x=sum(pastel_alcance.get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])

#impresiones
pastel_impresiones = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_impresiones.add_trace(go.Pie(
                labels=captacion['País'],
                values=captacion['Impresiones'],
                name="Captacion"),
                1, 1
             )
pastel_impresiones.add_trace(go.Pie(
                labels=registro['País'],
                values=registro['Impresiones'],
                name="Registro"),
                1, 2
             )
pastel_impresiones.add_trace(go.Pie(
                labels=venta['País'],
                values=venta['Impresiones'],
                name="Venta"),
                1, 3
             )
# Use `hole` to create a donut-like pie chart
pastel_impresiones.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0

pastel_impresiones.update_layout(    
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Captacion', x=sum(pastel_impresiones.get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Registro', x=sum(pastel_impresiones.get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Venta', x=sum(pastel_impresiones.get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])

#graficos de Sunburst para alcance e impresiones por paises
# Alcance
sunburst_alcance = px.sunburst(
    df_pais,
    path=['Nombre de la campaña', 'País'],  # Jerarquía: campaña -> países
    values='Alcance',                         # Tamaño de cada segmento
    title='Alcance de Campañas y Países',
    width=500,
    height=500,
    color='Nombre de la campaña',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_alcance.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje

# Impresiones
sunburst_impresiones = px.sunburst(
    df_pais,
    path=['Nombre de la campaña', 'País'],  # Jerarquía: campaña -> países
    values='Impresiones',                         # Tamaño de cada segmento
    title='Impresiones de Campañas y Países',
    width=500,
    height=500,
    color='Nombre de la campaña',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_impresiones.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje
   
#graficos tipo mapas para los paises alcanzados por campañas
# captacion
world_map_captacion = folium.Map(location=[0, 0], zoom_start=2)
# Crear el mapa coroplético usando los datos de "Alcance" por "País"
Choropleth(
    geo_data=world_geo,
    data= captacion,  # Tu DataFrame con las columnas 'País' y 'Alcance'
    columns=['País', 'Alcance'],  # Especificar columnas clave para el análisis
    key_on='feature.properties.name',  # Conectar los nombres del GeoJSON con los de tu DataFrame
    fill_color='YlOrRd',  # Escala de colores
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Alcance por País',
    reset=True
).add_to(world_map_captacion)

#registro
world_map_registro = folium.Map(location=[0, 0], zoom_start=2)
# Crear el mapa coroplético usando los datos de "Alcance" por "País"
Choropleth(
    geo_data=world_geo,
    data= registro,  # Tu DataFrame con las columnas 'País' y 'Alcance'
    columns=['País', 'Alcance'],  # Especificar columnas clave para el análisis
    key_on='feature.properties.name',  # Conectar los nombres del GeoJSON con los de tu DataFrame
    fill_color='YlOrRd',  # Escala de colores
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Alcance por País',
    reset=True
).add_to(world_map_registro)

# venta
world_map_venta = folium.Map(location=[0, 0], zoom_start=2)
# Crear el mapa coroplético usando los datos de "Alcance" por "País"
Choropleth(
    geo_data=world_geo,
    data= venta,  # Tu DataFrame con las columnas 'País' y 'Alcance'
    columns=['País', 'Alcance'],  # Especificar columnas clave para el análisis
    key_on='feature.properties.name',  # Conectar los nombres del GeoJSON con los de tu DataFrame
    fill_color='YlOrRd',  # Escala de colores
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Alcance por País',
    reset=True
).add_to(world_map_venta)


""""
Aqui inicia los gráficos relacionados a alcance e impresiones por edad

"""

# Gráfico de barras Alcance e impresiones por edad para cada campaña
#Alcance
captacion_edad_suma = captacion_edad.groupby('Edad', as_index=False)['Alcance'].sum()
registro_edad_suma = registro_edad.groupby('Edad', as_index=False)['Alcance'].sum()
venta_edad_suma = venta_edad.groupby('Edad', as_index=False)['Alcance'].sum()

bar_edad_al = go.Figure(
    data=[
        go.Bar(x=captacion_edad_suma['Edad'], y=captacion_edad_suma['Alcance'], name="Captacion"),
        go.Bar(x=registro_edad_suma['Edad'], y=registro_edad_suma['Alcance'], name="Registro"),
        go.Bar(x=venta_edad_suma['Edad'], y=venta_edad_suma['Alcance'], name="Venta"),
    ],
    layout=dict(
        barcornerradius=5,
        height=500,
        barmode='group',
        xaxis_tickangle=-45,
        title='Alcance por Edad para cada Campaña'
    ),
)
#Impresiones 
captacion_edad_suma2 = captacion_edad.groupby('Edad', as_index=False)['Impresiones'].sum()
registro_edad_suma2 = registro_edad.groupby('Edad', as_index=False)['Impresiones'].sum()
venta_edad_suma2 = venta_edad.groupby('Edad', as_index=False)['Impresiones'].sum()

bar_edad_im = go.Figure(
    data=[
        go.Bar(x=captacion_edad_suma2['Edad'], y=captacion_edad_suma2['Impresiones'], name="Captacion"),
        go.Bar(x=registro_edad_suma2['Edad'], y=registro_edad_suma2['Impresiones'], name="Registro"),
        go.Bar(x=venta_edad_suma2['Edad'], y=venta_edad_suma2['Impresiones'], name="Venta"),
    ],
    layout=dict(
        barcornerradius=5,
        height=500,
        barmode='group',
        xaxis_tickangle=-45,
        title='Impresiones por Edad para cada Campaña'
    ),
)

# Gráfico de pastel Alcance e impresiones por edad para cada campaña
#Alcance
# Create subplots: use 'domain' type for Pie subplot
pastel_edad_al = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_edad_al.add_trace(go.Pie(
                labels=captacion_edad['Edad'],
                values=captacion_edad['Alcance'],
                name="Captacion"),
                1, 1
             )
pastel_edad_al.add_trace(go.Pie(
                labels=registro_edad['Edad'],
                values=registro_edad['Alcance'],
                name="Registro"),
                1, 2
             )
pastel_edad_al.add_trace(go.Pie(
                labels=venta_edad['Edad'],
                values=venta_edad['Alcance'],
                name="Venta"),
                1, 3
             )

# Use `hole` to create a donut-like pie chart
pastel_edad_al.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0

pastel_edad_al.update_layout(
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Captacion', x=sum(pastel_edad_al .get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Registro', x=sum(pastel_edad_al .get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Venta', x=sum(pastel_edad_al .get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])

#impresiones
# Create subplots: use 'domain' type for Pie subplot
pastel_edad_im = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_edad_im.add_trace(go.Pie(
                labels=captacion_edad['Edad'],
                values=captacion_edad['Impresiones'],
                name="Captacion"),
                1, 1
             )
pastel_edad_im.add_trace(go.Pie(
                labels=registro_edad['Edad'],
                values=registro_edad['Impresiones'],
                name="Registro"),
                1, 2
             )
pastel_edad_im.add_trace(go.Pie(
                labels=venta_edad['Edad'],
                values=venta_edad['Impresiones'],
                name="Venta"),
                1, 3
             )

# Use `hole` to create a donut-like pie chart
pastel_edad_im.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0

pastel_edad_im.update_layout(
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Captacion', x=sum(pastel_edad_im.get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Registro', x=sum(pastel_edad_im.get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Venta', x=sum(pastel_edad_im.get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])


# Gráfico de Sunburst Alcance e impresiones por edad para cada campaña
#Alcance
sunburst_edad_al = px.sunburst(
    df_sex_edad,
    path=['Nombre de la campaña', 'Edad'],  # Jerarquía: campaña -> países
    values='Alcance',                         # Tamaño de cada segmento
    title='Alcance de Campañas por Edad',
    width=500,
    height=500,
    color='Nombre de la campaña',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_edad_al.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje

# Impresiones
sunburst_edad_im = px.sunburst(
    df_sex_edad,
    path=['Nombre de la campaña', 'Edad'],  # Jerarquía: campaña -> países
    values='Impresiones',                         # Tamaño de cada segmento
    title='Impresiones de Campañas por Edad',
    width=500,
    height=500,
    color='Nombre de la campaña',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_edad_im.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje

""""
Aqui inicia los gráficos relacionados a alcance e impresiones por género

"""

# Gráfico de barras Alcance e impresiones por genero para cada campaña
#Alcance
captacion_sex_suma = captacion_edad.groupby('Sexo', as_index=False)['Alcance'].sum()
registro_sex_suma = registro_edad.groupby('Sexo', as_index=False)['Alcance'].sum()
venta_sex_suma = venta_edad.groupby('Sexo', as_index=False)['Alcance'].sum()

bar_sex_al = go.Figure(
    data=[
        go.Bar(x=captacion_sex_suma['Sexo'], y=captacion_sex_suma['Alcance'], name="Captacion"),
        go.Bar(x=registro_sex_suma['Sexo'], y=registro_sex_suma['Alcance'], name="Registro"),
        go.Bar(x=venta_sex_suma['Sexo'], y=venta_sex_suma['Alcance'], name="Venta"),
    ],
    layout=dict(
        barcornerradius=5,
        height=500,
        barmode='group',
        xaxis_tickangle=-45,
        title='Alcance por Género para cada Campaña'
    ),
)

#Impresiones
captacion_sex_suma2 = captacion_edad.groupby('Sexo', as_index=False)['Impresiones'].sum()
registro_sex_suma2 = registro_edad.groupby('Sexo', as_index=False)['Impresiones'].sum()
venta_sex_suma2 = venta_edad.groupby('Sexo', as_index=False)['Impresiones'].sum()

bar_sex_im = go.Figure(
    data=[
        go.Bar(x=captacion_sex_suma2['Sexo'], y=captacion_sex_suma2['Impresiones'], name="Captacion"),
        go.Bar(x=registro_sex_suma2['Sexo'], y=registro_sex_suma2['Impresiones'], name="Registro"),
        go.Bar(x=venta_sex_suma2['Sexo'], y=venta_sex_suma2['Impresiones'], name="Venta"),
    ],
    layout=dict(
        barcornerradius=5,
        height=500,
        barmode='group',
        xaxis_tickangle=-45,
        title='Impresiones por Género para cada Campaña'
    ),
)


# Gráfico de pastel Alcance e impresiones por genero para cada campaña
#Alcance
pastel_sex_al = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_sex_al.add_trace(go.Pie(
                labels=captacion_edad['Sexo'],
                values=captacion_edad['Alcance'],
                name="Captacion"),
                1, 1
             )
pastel_sex_al.add_trace(go.Pie(
                labels=registro_edad['Sexo'],
                values=registro_edad['Alcance'],
                name="Registro"),
                1, 2
             )
pastel_sex_al.add_trace(go.Pie(
                labels=venta_edad['Sexo'],
                values=venta_edad['Alcance'],
                name="Venta"),
                1, 3
             )
# Use `hole` to create a donut-like pie chart
pastel_sex_al.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0
pastel_sex_al.update_layout(
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Captacion', x=sum(pastel_sex_al.get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Registro', x=sum(pastel_sex_al.get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Venta', x=sum(pastel_sex_al.get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])

#Impresiones
pastel_sex_im = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_sex_im.add_trace(go.Pie(
                labels=captacion_edad['Sexo'],
                values=captacion_edad['Impresiones'],
                name="Captacion"),
                1, 1
             )
pastel_sex_im.add_trace(go.Pie(
                labels=registro_edad['Sexo'],
                values=registro_edad['Impresiones'],
                name="Registro"),
                1, 2
             )
pastel_sex_im.add_trace(go.Pie(
                labels=venta_edad['Sexo'],
                values=venta_edad['Impresiones'],
                name="Venta"),
                1, 3
             )
# Use `hole` to create a donut-like pie chart
pastel_sex_im.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0

pastel_sex_im.update_layout(
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Captacion', x=sum(pastel_sex_im.get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Registro', x=sum(pastel_sex_im.get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Venta', x=sum(pastel_sex_im.get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])


# Gráfico de Sunburst Alcance e impresiones por edad para cada campaña
#Alcance
sunburst_sex_al = px.sunburst(
    df_sex_edad,
    path=['Nombre de la campaña', 'Sexo'],  # Jerarquía: campaña -> países
    values='Alcance',                         # Tamaño de cada segmento
    title='Alcance de Campañas por Género',
    width=500,
    height=500,
    color='Nombre de la campaña',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_sex_al.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje

#Impresiones
sunburst_sex_im = px.sunburst(
    df_sex_edad,
    path=['Nombre de la campaña', 'Sexo'],  # Jerarquía: campaña -> países
    values='Impresiones',                         # Tamaño de cada segmento
    title='Impresiones de Campañas por Género',
    width=500,
    height=500,
    color='Nombre de la campaña',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_sex_im.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje

""""
Aqui inicia los gráficos relacionados a alcance e impresiones por plataforma

"""

# preparacion de datos por plataforma

face = 'Facebook'
plat_face = df_plat[df_plat['Plataforma'] == face]

insta = 'Instagram'
plat_insta = df_plat[df_plat['Plataforma'] == insta]

# Gráfico de Sunburst Alcance e impresiones por plataformas
# Alcance
sunburst_plat_al = px.sunburst(
    df_plat,
    path=['Plataforma', 'Ubicación', 'Plataforma de dispositivos'],  # Jerarquía: campaña -> países
    values='Alcance',                         # Tamaño de cada segmento
    title='Alcance por plataformas',
    width=500,
    height=500,
    color='Plataforma',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_plat_al.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje

#Impresiones
sunburst_plat_im = px.sunburst(
    df_plat,
    path=['Plataforma', 'Ubicación', 'Plataforma de dispositivos'],  # Jerarquía: campaña -> países
    values='Impresiones',                         # Tamaño de cada segmento
    title='Impresiones por plataformas',
    width=500,
    height=500,
    color='Plataforma',             # Opcional, para diferenciar por color
    color_discrete_sequence=px.colors.qualitative.Pastel  # Colores personalizados (opcional)
)
sunburst_plat_im.update_traces(textinfo="label+percent entry")  # Muestra etiquetas y porcentaje

# Gráfico de pastel Alcance e impresiones por plataformas
# Alcance
pastel_plat_al = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_plat_al.add_trace(go.Pie(
                labels=plat_face['Ubicación'],
                values=plat_face['Alcance'],
                name="Facebook"),
                1, 1
             )
pastel_plat_al.add_trace(go.Pie(
                labels=plat_insta['Ubicación'],
                values=plat_insta['Alcance'],
                name="Instagram"),
                1, 2
             )
pastel_plat_al.add_trace(go.Pie(
                labels=df_plat['Plataforma'],
                values=df_plat['Alcance'],
                name="Plataforma"),
                1, 3
             )

# Use `hole` to create a donut-like pie chart
pastel_plat_al.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0

pastel_plat_al.update_layout(
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Facebook', x=sum(pastel_plat_al.get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Instagram', x=sum(pastel_plat_al.get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Plataforma', x=sum(pastel_plat_al.get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])

#Impresiones
pastel_plat_im = make_subplots(rows=1, cols=3,
                    column_widths=[700,700,700],
                    row_heights=[2500],
                    specs=[[{'type':'domain'},{'type':'domain'}, {'type':'domain'}]])
pastel_plat_im.add_trace(go.Pie(
                labels=plat_face['Ubicación'],
                values=plat_face['Impresiones'],
                name="Facebook"),
                1, 1
             )
pastel_plat_im.add_trace(go.Pie(
                labels=plat_insta['Ubicación'],
                values=plat_insta['Impresiones'],
                name="Instagram"),
                1, 2
             )
pastel_plat_im.add_trace(go.Pie(
                labels=df_plat['Plataforma'],
                values=df_plat['Impresiones'],
                name="Plataforma"),
                1, 3
             )

# Use `hole` to create a donut-like pie chart
pastel_plat_im.update_traces(hole=0, hoverinfo="label+percent+name") #tamaño del circulo interno, lo he quitado por eso 0

pastel_plat_im.update_layout(
    # Añadir las anotaciones, que las he puesto encima porque quite el hueco del medio
    annotations=[dict(text='Facebook', x=sum(pastel_plat_im.get_subplot(1, 1).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Instagram', x=sum(pastel_plat_im.get_subplot(1, 2).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center"),
                 dict(text='Plataforma', x=sum(pastel_plat_im.get_subplot(1, 3).x) / 2, y=1.2,
                      font_size=20, showarrow=False, xanchor="center")])