import streamlit as st
#import pandas as pd
#import json

#gráficos
from grafic import funnel_alcance, funnel_impresiones                                       # Importo los gráficos de funnel para alcance e impresiones por campañas
from grafic import columnas_alcance, columnas_impresiones                                   # Importo los gráficos de columnas para alcance e impresiones por campañas y paises
from grafic import pastel_alcance, pastel_impresiones                                       # Importo los gráficos de pastel para alcance e impresiones por campañas por paises
from grafic import sunburst_alcance, sunburst_impresiones                                   # Importo los gráficos de sunburst para alcance e impresiones por campañas y paises
from grafic import world_map_captacion, world_map_registro, world_map_venta                 # Importo los mapas para alcance campañas
#edad
from grafic import bar_edad_al, bar_edad_im                                                 # Importo los gráficos de columnas para alcance e impresiones por campañas y edad
from grafic import pastel_edad_al, pastel_edad_im                                           # Importo los gráficos de pastel para alcance e impresiones por campañas por edad
from grafic import sunburst_edad_al, sunburst_edad_im                                       # Importo los gráficos de sunburst para alcance e impresiones por campañas y edad
#genero
from grafic import bar_sex_al, bar_sex_im                                                   # Importo los gráficos de columnas para alcance e impresiones por campañas y genero
from grafic import pastel_sex_al, pastel_sex_im                                             # Importo los gráficos de pastel para alcance e impresiones por campañas por genero
from grafic import sunburst_sex_al, sunburst_sex_im                                         # Importo los gráficos de sunburst para alcance e impresiones por campañas y genero
#plataforma
from grafic import sunburst_plat_al, sunburst_plat_im                                       # Importo los gráficos de sunburst para alcance e impresiones por plataformas
from grafic import pastel_plat_al, pastel_plat_im                                           # Importo los gráficos de pastel para alcance e impresiones por plataformas

#Tablas
from tables import df_sex, df_plat, df_edad                                       # Importo las tablas de alcance e impresiones total
from tables import alcance, impresiones2                                       # Importo las tablas de alcance e impresiones total ojo, el impresiones 2 es porque daba un error sin sentido, no renocia columna pais
from tables import resultado_alcance, resultado_impresiones                                       # Importo las tablas de alcance e impresiones total
from tables import r_captacion, r_registro, r_venta                                       # Importo las tablas de resultados totales por campañas
from tables import total_face, total_insta                                       # Importo las tablas de resultados por plataformas


# Inicio de la interface de streamlit
# Título de la página
st.set_page_config(page_title="Dashboard de Métricas", layout="wide") #esto solo se puede usar al principio y no repetir


#Barra lateral
# Logo
st.sidebar.image("images/logo av_marina.png", width=100)
with st.sidebar.expander("Nota:"):
                st.caption("Esta App usa datos reales de campañas publicitarias realizadas de Septiembre a Diciembre. Tiene un uso práctico/didáctico con el que se pretende explorar y jugar con datos reales.")

st.sidebar.title("Filtros")
visual = st.sidebar.selectbox("Selecciona visualización", ["Gráficos", "Tablas"])

if visual == 'Gráficos': 
    metrica = st.sidebar.selectbox("Selecciona métrica", ["Pais", "Género", "Edad", "Plataformas"])


st.sidebar.markdown("---")
st.sidebar.title("Glosario")
with st.sidebar.expander("Alcance e impresiones:"):
                st.caption("Alcance corresponde al número de cuentas únicas alcanzadas. Impresiones corresponde a las veces que ha sido visitado el anuncio en total")
with st.sidebar.expander("Campañas:"):
                st.caption("Para el caso mostrado se realizaron 3 fases o campañas. Captacion, Registro, Venta. Explicadas en glosario")

st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <a href="https://linktr.ee/rayko_benitez" target="_blank">
            <img src="https://ugc.production.linktr.ee/097834f8-e2d7-4fe7-9d38-489fc794f840_DAGNQ4WeEPc.png?io=true&size=avatar-v3_0" width="50">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

#Interface o pantalla principal


# Título principal
st.title("Dashboard de Métricas Publicitarias")

if visual == 'Gráficos':
    if metrica == 'Pais':
        # Funnel de alcance e impresiones
        st.header("Alcance e impresiones", divider='rainbow') 

        # Primera fila de gráficos
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(funnel_alcance)

        with col2:
            st.plotly_chart(funnel_impresiones)


        #gáfico de barras para comparar alcance e impresiones por paises
        st.header("Alcance e impresiones por paises", divider='rainbow')
        # Primera fila de gráficos
        col3, col4 = st.columns(2)

        with col3:
            st.plotly_chart(columnas_alcance)

        with col4:
            st.plotly_chart(columnas_impresiones)


        #graficos de pastel para alcance e impresiones por paises
        # Alcance
        st.header("Alcance por paises para cada Campaña", divider='rainbow')
        st.plotly_chart(pastel_alcance)

        #impresiones
        st.header("Impresiones por paises para cada Campaña", divider='rainbow')
        st.plotly_chart(pastel_impresiones)


        #graficos de Sunburst para alcance e impresiones por paises
        st.header("Gráfico de familia para Alcance e Impresiones por paises", divider='rainbow')

        col1, col2 = st.columns(2)
        # Alcance
        with col1:
            st.plotly_chart(sunburst_alcance)

        # Impresiones
        with col2:
            st.plotly_chart(sunburst_impresiones)


        #graficos tipo mapas para los paises alcanzados por campañas
        st.header("Mapa de paises alcanzados por campaña", divider='rainbow')

        st.markdown("### 01 Captación")
        st.components.v1.html(world_map_captacion._repr_html_(), height=500)

        st.markdown("### 02 Registro")
        st.components.v1.html(world_map_registro._repr_html_(), height=500)

        st.markdown("### 03 Venta")
        st.components.v1.html(world_map_venta._repr_html_(), height=500)

    elif metrica == 'Edad':
        # gráficos por edad
        # Funnel de alcance e impresiones
        st.header("Alcance e impresiones", divider='rainbow') 

        # Primera fila de gráficos
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(funnel_alcance)

        with col2:
            st.plotly_chart(funnel_impresiones)


        #gáfico de barras para comparar alcance e impresiones por paises
        st.header("Alcance e impresiones por Edad", divider='rainbow')
        # Primera fila de gráficos
        col3, col4 = st.columns(2)

        with col3:
            st.plotly_chart(bar_edad_al)

        with col4:
            st.plotly_chart(bar_edad_im)


        #graficos de pastel para alcance e impresiones por edad
        # Alcance
        st.header("Alcance por edad para cada Campaña", divider='rainbow')
        st.plotly_chart(pastel_edad_al)

        #impresiones
        st.header("Impresiones por edad para cada Campaña", divider='rainbow')
        st.plotly_chart(pastel_edad_im)


        #graficos de Sunburst para alcance e impresiones por edad
        st.header("Gráfico de familia para Alcance e Impresiones por edad", divider='rainbow')

        col1, col2 = st.columns(2)
        # Alcance
        with col1:
            st.plotly_chart(sunburst_edad_al)

        # Impresiones
        with col2:
            st.plotly_chart(sunburst_edad_im)
    
    elif metrica == 'Género':
          # gráficos por genero
          # Funnel de alcance e impresiones
        st.header("Alcance e impresiones", divider='rainbow') 

        # Primera fila de gráficos
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(funnel_alcance)

        with col2:
            st.plotly_chart(funnel_impresiones)


        #gáfico de barras para comparar alcance e impresiones por genero
        st.header("Alcance e impresiones por Género", divider='rainbow')
        # Primera fila de gráficos
        col3, col4 = st.columns(2)

        with col3:
            st.plotly_chart(bar_sex_al)

        with col4:
            st.plotly_chart(bar_sex_im)


        #graficos de pastel para alcance e impresiones por edad
        # Alcance
        st.header("Alcance por género para cada Campaña", divider='rainbow')
        st.plotly_chart(pastel_sex_al)

        #impresiones
        st.header("Impresiones por género para cada Campaña", divider='rainbow')
        st.plotly_chart(pastel_sex_im)


        #graficos de Sunburst para alcance e impresiones por género
        st.header("Gráfico de familia para Alcance e Impresiones por género", divider='rainbow')

        col1, col2 = st.columns(2)
        # Alcance
        with col1:
            st.plotly_chart(sunburst_sex_al)

        # Impresiones
        with col2:
            st.plotly_chart(sunburst_sex_im)

    elif metrica == 'Plataformas':
        # gráficos por plataforma
        #graficos de Sunburst para alcance e impresiones por plataformas
        st.header("Gráfico de familia para Alcance e Impresiones plataformas", divider='rainbow')

        col1, col2 = st.columns(2)
        # Alcance
        with col1:
            st.plotly_chart(sunburst_plat_al)

        # Impresiones
        with col2:
            st.plotly_chart(sunburst_plat_im)
        
        #graficos de pastel para alcance e impresiones plataforma
        # Alcance
        st.header("Alcance por plataformas", divider='rainbow')
        st.plotly_chart(pastel_plat_al)

        #impresiones
        st.header("Impresiones por plataformas", divider='rainbow')
        st.plotly_chart(pastel_plat_im)


elif visual == 'Tablas':
       # Tabla resultados por campaña
       st.header("Resultados por campaña", divider='rainbow')
       col1, col2, col3 = st.columns(3)
       with col1:
           st.subheader('01 Captacion')
           st.table(r_captacion)
       with col2:
           st.subheader('02 Registro')
           st.table(r_registro)
           st.info(':red[NOTA]: Las tablas contienen distintas métricas por los objetivos configurados en :blue[META] para cada una de las fases.')
       with col3:
           st.subheader('03 Venta')
           st.table(r_venta)
        
       st.header("Alcance e Impresiones por paises", divider='rainbow')
       col1, col2 = st.columns(2)
       with col1:
            st.subheader('Alcance')
            st.table(alcance)
       with col2:
            st.subheader('Impresiones')
            st.table(impresiones2)
        
       col1, col2 = st.columns(2)
       with col1:
            st.header("Género", divider='rainbow')
            st.table(df_sex)
       with col2:
            st.header("Edad", divider='rainbow')
            st.table(df_edad)

        

       st.header("Resultados en Facebook", divider='rainbow')
       st.write(total_face)
       st.header("Resultados en Instagram", divider='rainbow')
       st.write(total_insta)


