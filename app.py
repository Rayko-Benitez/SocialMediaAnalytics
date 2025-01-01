import streamlit as st
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
df_sex_edad = pd.read_excel('datasets/df_plat.xlsx')
df_plat = pd.read_excel('datasets/df_sex_edad.xlsx')
captacion = pd.read_excel('datasets/captacion.xlsx')
registro = pd.read_excel('datasets/registro.xlsx')
venta = pd.read_excel('datasets/venta.xlsx')

# Inicio de la interface de streamlit
# Título de la página
st.set_page_config(page_title="Dashboard de Métricas", layout="wide") #esto solo se puede usar al principio y no repetir

# Barra lateral
st.sidebar.title("Filtros")
opcion = st.sidebar.selectbox("Selecciona visualización", ["Gráficos", "Tablas"])

opciones = st.sidebar.multiselect(
    "Selecciona métricas",
    ["Pais", "Género", "Edad", "Plataformas"],
    default=["Pais", "Género", "Edad", "Plataformas"]
)
st.sidebar.markdown("---")
st.sidebar.title("KPI")

# Cuerpo de la interface


# Título principal
st.title("Dashboard de Métricas Publicitarias")
# Separador
st.markdown("---")


# Funnel de alcance e impresiones
st.header("Alcance e impresiones")

# Primera fila de gráficos
col1, col2 = st.columns(2)

with col1:
    df_funnel_al = df_pais.groupby('Nombre de la campaña', as_index=False)['Alcance'].sum()
    funnel_alcance = px.funnel_area(names=df_funnel_al['Nombre de la campaña'],
                    values=df_funnel_al['Alcance'],
                    width=700,
                    height=500,
                    labels=df_funnel_al['Nombre de la campaña'],
                    title='Funnel de alcance por campañas'
                    )
    st.plotly_chart(funnel_alcance)

with col2:
    df_funnel_im = df_pais.groupby('Nombre de la campaña', as_index=False)['Impresiones'].sum()
    funnel_impresiones = px.funnel_area(names=df_funnel_im['Nombre de la campaña'],
                        values=df_funnel_im['Impresiones'],
                        width=700,
                        height=500,
                        labels=df_funnel_im['Nombre de la campaña'],
                        title='Funnel de impresiones por campañas'
                        )
    st.plotly_chart(funnel_impresiones)

st.markdown("---")

#gáfico de barras para comparar alcance e impresiones por paises
# Primera fila de gráficos
col3, col4 = st.columns(2)

with col3:
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
    st.plotly_chart(columnas_alcance)

with col4:
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
    st.plotly_chart(columnas_impresiones)

st.markdown("---")

#graficos de pastel para alcance e impresiones por paises
# Alcance
st.subheader("Alcance por Paises para cada Campaña")
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

st.plotly_chart(pastel_alcance)

#impresiones
st.subheader("Impresiones por Paises para cada Campaña")
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

st.plotly_chart(pastel_impresiones)

st.markdown("---")

#graficos de Sunburst para alcance e impresiones por paises
st.subheader("Gráfico de familia para Alcance e Impresiones por paises")

col1, col2 = st.columns(2)
# Alcance
with col1:
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
    st.plotly_chart(sunburst_alcance)

# Impresiones
with col2:
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
    st.plotly_chart(sunburst_impresiones)

st.markdown("---")

#graficos tipo mapas para los paises alcanzados por campañas
st.subheader("Mapa de paises alcanzados por campaña")

st.markdown("### 01 Captación")
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
st.components.v1.html(world_map_captacion._repr_html_(), height=500)

st.markdown("### 02 Registro")
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
st.components.v1.html(world_map_registro._repr_html_(), height=500)

st.markdown("### 03 Venta")
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
st.components.v1.html(world_map_venta._repr_html_(), height=500)









