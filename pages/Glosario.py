import streamlit as st


#Barra lateral 

# Logo
st.sidebar.image("images/logo av_marina.png", width=100)
with st.sidebar.expander("Nota:"):
                st.caption("Esta App usa datos reales de campañas publicitarias realizadas de Septiembre a Diciembre. Tiene un uso práctico/didáctico con el que se pretende explorar y jugar con datos reales.")


st.sidebar.title("Glosario")
with st.sidebar.expander("Alcance e impresiones:"):
                st.caption("Alcance corresponde al número de cuentas únicas alcanzadas. Impresiones corresponde a las veces que ha sido visitado el anuncio en total")
with st.sidebar.expander("Campañas:"):
                st.caption("Para el caso mostrado se realizaron 3 fases o campañas. Captacion, Registro, Venta")



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


# Cuerpo de la web
# Título principal
st.title("Explicación de la App y el trabajo realizado en las campañas")

st.subheader("Estoy trabajando en este apartado")

st.write("Es importante resaltar que esta app es para jugar con los datos, es parte de un trabajo de investigación y exploración de resultados de las campañas. La exploración de datos no es un proceso lineal, lleva un conjunto de preguntas y análisis que constantemente te hace avanzar y retroceder para ir creando conclusiones. ")
st.write("Tiene inicialmente un objetivo de aprendizaje, analizar cuales son los valores de mayor interés, a qué darle mayor o menor importancia para el caso particular de cada campaña, no significa que para todas las campañas se deben analizar los mismos valores, pero por algún punto hay que empezar.")
st.write('Con este análisis se han llegado a muchas conclusiones, no las voy a reflejar aquí para no interferir en la capacidad analítica de alguien o crear algún tipo de sesgo en las decisiones, como decía antes, no funciona el mismo análisis para todas las campañas, depende del objetivo particular de cada una, el valor del producto o servicio, incluso si es propiamente un producto o servicio lo que se ofrece.')


st.header("Campañas realizadas", divider='rainbow')
# Insert containers separated into tabs:
tab1, tab2, tab3 = st.tabs(["01 Captacion", "02 Registro", "03 Venta"])
tab1.write("Se enfocó en reunir email a partir de una segmentacion estimada para reunir público objetivo")
tab2.write("Se enfocó en que se registren interesados a varias clases introductorias de lo que verían en el programa e informacion de valor")
tab3.write("Se enfocó en realizar venta del programa")




#esto esta bien para una pagina de contacto
#st.text_area('a ver que haces')
