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


st.write("Es importante resaltar que esta app es para jugar con los datos, es parte de un trabajo de investigación y exploración de resultados de las campañas. La exploración de datos no es un proceso lineal, lleva un conjunto de preguntas y análisis que constantemente te hace avanzar y retroceder para ir creando conclusiones. ")
st.write("Tiene inicialmente un objetivo de aprendizaje, analizar cuales son los valores de mayor interés, a qué darle mayor o menor importancia para el caso particular de cada campaña, no significa que para todas las campañas se deben analizar los mismos valores, pero por algún punto hay que empezar.")
st.write('Con este análisis se han llegado a muchas conclusiones, no las voy a reflejar aquí para no interferir en la capacidad analítica de alguien o crear algún tipo de sesgo en las decisiones, como decía antes, no funciona el mismo análisis para todas las campañas, depende del objetivo particular de cada una, el valor del producto o servicio, incluso si es propiamente un producto o servicio lo que se ofrece.')


st.header("Campañas realizadas", divider='rainbow')

# Insertar pestañas
tab1, tab2, tab3 = st.tabs(["01 Captación", "02 Registro", "03 Venta"])

with tab1:
    st.markdown("""
    ### **1. Fase de Captación**

    - **¿Qué es?**  
      Es la fase inicial del lanzamiento publicitario donde se busca atraer clientes potenciales que puedan estar interesados en la oferta. Se enfoca en generar tráfico hacia una página de registro.

    - **¿Qué se hace?**  
        - Creación de anuncios dirigidos a públicos fríos y tibios en plataformas como Facebook Ads.  
        - Uso de estrategias de contenido para generar interés y visibilidad.  
        - Implementación de una página de captura (Landing Page) para incentivar el registro.  

    - **Objetivo:**  
      Conseguir el mayor número posible de leads interesados en el lanzamiento, generando una base de datos sólida para las siguientes etapas.

    - **Resultados esperados:**  
        - Incremento en el reconocimiento de la marca.  
        - Crecimiento de la lista de contactos interesados.  
        - Aumento en la tasa de registros para el evento o promoción.
    """)

with tab2:
    st.markdown("""
    ### **2. Fase de Registro**

    - **¿Qué es?**  
      Es la fase donde se obtiene la conversión de visitantes en leads registrados, asegurando que los interesados pasen a la siguiente etapa del embudo.

    - **¿Qué se hace?**  
        - Creación de páginas de registro optimizadas con mensajes persuasivos.  
        - Uso de formularios sencillos y llamados a la acción claros.  
        - Automatización de respuestas y confirmaciones mediante email marketing o WhatsApp.  

    - **Objetivo:**  
      Lograr que las personas se registren en el evento, oferta o lanzamiento para mantener una comunicación directa con ellos.

    - **Resultados esperados:**  
        - Aumento en la tasa de conversión de visitantes a leads.  
        - Construcción de una base de datos cualificada.  
        - Segmentación efectiva de la audiencia según el interés mostrado.
    """)

with tab3:
    st.markdown("""
    ### **3. Fase de Venta**

    - **¿Qué es?**  
      Es la fase final donde se lleva a cabo la monetización del lanzamiento, convirtiendo a los leads en compradores.

    - **¿Qué se hace?**  
        - Implementación de estrategias de venta como escasez, prueba social y bonos de acción rápida.  
        - Envío de secuencias de correos y mensajes persuasivos.  
        - Cierre del carrito de compra con estrategias de urgencia.  

    - **Objetivo:**  
      Maximizar las conversiones y generar el mayor número de ventas en el periodo de lanzamiento.

    - **Resultados esperados:**  
        - Generación de ingresos y rentabilidad del lanzamiento.  
        - Posicionamiento del producto en el mercado.  
        - Creación de clientes satisfechos que pueden convertirse en embajadores de la marca.
    """)





#esto esta bien para una pagina de contacto
#st.text_area('a ver que haces')
