import pandas as pd

# todos los excel son tablas descargados de las campañas de meta con un filtro y configuracion particular alli realizado
# Archivos excel usados
df_pais = pd.read_excel('datasets/df_pais.xlsx')
df_sex_edad = pd.read_excel('datasets/df_sex_edad.xlsx')
df_plat = pd.read_excel('datasets/df_plat.xlsx')
captacion = pd.read_excel('datasets/captacion.xlsx')                   #toma df_pais y lo filtra por valores unicos de nombre de campaña a 01 Nomada captación
registro = pd.read_excel('datasets/registro.xlsx')                     #toma df_pais y lo filtra por valores unicos de nombre de campaña a 01 Nomada Registros
venta = pd.read_excel('datasets/venta.xlsx')                           #toma df_pais y lo filtra por valores unicos de nombre de campaña a 01 Nomada Venta
captacion_edad = pd.read_excel('datasets/captacion_edad.xlsx')         #toma df_sex_edad y lo filtra por valores unicos de nombre de campaña a 01 Nomada captación
registro_edad = pd.read_excel('datasets/registro_edad.xlsx')           #toma df_sex_edad y lo filtra por valores unicos de nombre de campaña a 01 Nomada Registros
venta_edad = pd.read_excel('datasets/venta_edad.xlsx')                 #toma df_sex_edad y lo filtra por valores unicos de nombre de campaña a 01 Nomada Venta

#Tablas referidas al Alcance e impresiones por paises

#paises a los que hemos llegado en todas las campañas
paises_unicos = df_pais['País'].unique()
#alcance total de todas las campañas, cuentas unicas
alcance_total = df_pais['Alcance'].sum()
#impresiones totales de todas las campañas, cuentas unicas
impresion_total = df_pais['Impresiones'].sum()

#tabla de paises a los que llegamos y el alcance total en cada uno de ellos
alcance = df_pais.groupby('País', as_index=False)['Alcance'].sum()
alcance = alcance.sort_values(by='Alcance', ascending=False)
#actualizo el index a pais
alcance = alcance.set_index('País')

#tabla de paises a los que llegamos y las impresiones total en cada uno de ellos
impresiones = df_pais.groupby('País', as_index=False)['Impresiones'].sum()
impresiones = impresiones.sort_values(by='Impresiones', ascending=False)
impresiones2 = impresiones.set_index('País') #he añadido el 2 porque daba problema al cargar las tablas, al crearla en esta funciona.


#tabla de paises alcanzados por campaña y el numero de cuentas unicas
resultado_alcance = df_pais.groupby('Nombre de la campaña', as_index=False).agg({
    'País': 'unique',
    'Alcance': 'sum'
})

#tabla de paises alcanzados por campaña y el numero de visitas
resultado_impresiones = df_pais.groupby('Nombre de la campaña', as_index=False).agg({
    'País': 'unique',
    'Impresiones': 'sum'
})

#Tabla que reune los valores de alcane, impresiones y la relacion de impresiones/alcance
# Combinar los DataFrames usando la columna 'País' como índice común
r_alc_imp = pd.merge(alcance, impresiones, on='País').set_index('País')
# Añadir una columna que calcule la relacion de impresiones sobre alcance y esto me indica el nivel de incertidumbre
r_alc_imp['Impresiones/Alcance'] = (r_alc_imp['Impresiones'] / r_alc_imp['Alcance'])

# Cambiar formato de las columnas 'Alcance' e 'Impresiones' a enteros
r_alc_imp['Alcance'] = r_alc_imp['Alcance'].astype(int)
r_alc_imp['Impresiones'] = r_alc_imp['Impresiones'].astype(int)

# Formatear la columna '% Impresiones/Alcance' con 2 decimales
r_alc_imp['Impresiones/Alcance'] = r_alc_imp['Impresiones/Alcance'].round(2)

#ordeno de forma descendente por la relaciones de impresiones o alcance y asi determino la incertidumbre por paises
r_alc_imp = r_alc_imp.sort_values(by='Impresiones/Alcance', ascending=False)


#Resultados de la campaña de captacion
# creo un nuevo df para obtener nuevos resultados con mas columnas del mismo por paises
r_captacion = captacion[['País','Resultados','Alcance','Impresiones','Clics en el enlace']]

#cambio el tipo de valores a enteros 
cambio = ['Resultados','Alcance','Impresiones','Clics en el enlace']
r_captacion[cambio] = r_captacion[cambio].astype(int)

#actualizo el index a pais
r_captacion = r_captacion.set_index('País')
# orden descendente por clic en el enlace, asi determino el pais mas curioso en la fase inicial de captacion
r_captacion = r_captacion.sort_values(by='Clics en el enlace', ascending=False)
r_captacion


# Resultados de la campaña de registro
# creo un nuevo df para obtener nuevos resultados con mas columnas del mismo por paises
r_registro = registro[['País','Alcance','Impresiones','Clics en el enlace']]

#cambio el tipo de valores a enteros 
cambio2 = ['Alcance','Impresiones','Clics en el enlace']
r_registro[cambio2] = r_registro[cambio2].astype(int)

#actualizo el index a pais
r_registro = r_registro.set_index('País')
# orden descendente por clic en el enlace, asi determino el pais mas curioso en la fase inicial de registro
r_registro = r_registro.sort_values(by='Clics en el enlace', ascending=False)
r_registro


# Resultados de la campaña de venta
# creo un nuevo df para obtener nuevos resultados con mas columnas del mismo por paises
r_venta = venta[['País','Resultados','Alcance','Impresiones','Clics en el enlace']]

#cambio el tipo de valores a enteros 
cambio3 = ['Resultados','Alcance','Impresiones','Clics en el enlace']
r_venta[cambio3] = r_venta[cambio3].fillna(0)
r_venta[cambio3] = r_venta[cambio3].astype(int)

#actualizo el index a pais
r_venta = r_venta.set_index('País')
# orden descendente por clic en el enlace, asi determino el pais mas curioso en la fase inicial de venta
r_venta = r_venta.sort_values(by='Clics en el enlace', ascending=False)
r_venta


#Tabla de alcance, impresiones y clic por edad
df_edad = df_sex_edad.groupby('Edad', as_index=False).agg({
    'Alcance': 'sum',
    'Impresiones': 'sum',
    'Clics en el enlace': 'sum'
})
df_edad = df_edad.sort_values(by='Clics en el enlace', ascending=False)
df_edad

#Tabla de alcance, impresiones y clic por sexo
df_sex = df_sex_edad.groupby('Sexo', as_index=False).agg({
    'Alcance': 'sum',
    'Impresiones': 'sum',
    'Clics en el enlace': 'sum'
})
df_sex = df_sex.sort_values(by='Clics en el enlace', ascending=False)
df_sex

#Tablas de resultados para las plataformas 
#df filtrados por plataforma
face = 'Facebook'
plat_face = df_plat[df_plat['Plataforma'] == face]
insta = 'Instagram'
plat_insta = df_plat[df_plat['Plataforma'] == insta]


#Facebook
total_face = plat_face.fillna(0)
total_face = total_face.groupby('Ubicación', as_index = False).agg({
    'Nombre de la campaña': 'unique',
    'Plataforma': 'unique',
    'Plataforma de dispositivos': 'unique',
    'Resultados': 'sum',
    'Alcance': 'sum',
    'Impresiones' : 'sum',
    'Costo por resultados' : 'sum',
    'CTR (porcentaje de clics en el enlace)' : 'sum',
    'Clics en el enlace' : 'sum',
    '%Registros/Clic' : 'mean',
    'Clientes potenciales' : 'sum',
    'Costo por cliente potencial (USD)': 'sum',
    'CPC (costo por clic en el enlace) (USD)': 'sum'
})
total_face.drop(columns=['Plataforma'], inplace=True)

#Instagram
total_insta = plat_insta.fillna(0)
total_insta = total_insta.groupby('Ubicación', as_index = False).agg({
    'Nombre de la campaña': 'unique',
    'Plataforma': 'unique',
    'Plataforma de dispositivos': 'unique',
    'Resultados': 'sum',
    'Alcance': 'sum',
    'Impresiones' : 'sum',
    'Costo por resultados' : 'sum',
    'CTR (porcentaje de clics en el enlace)' : 'sum',
    'Clics en el enlace' : 'sum',
    '%Registros/Clic' : 'mean',
    'Clientes potenciales' : 'sum',
    'Costo por cliente potencial (USD)': 'sum',
    'CPC (costo por clic en el enlace) (USD)': 'sum'
})
total_insta.drop(columns=['Plataforma'], inplace=True)