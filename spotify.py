from dash import Dash, html, dcc
import plotly.express as px
import psycopg2
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table

# Grafico que encuentra a los 10 artistas que mas se repiten
def repiten_artistas():
    conn = psycopg2.connect(
        dbname="final",
        user="postgres",
        password="123456789",
        host="localhost"
    )
    cur = conn.cursor()

    query = """
    SELECT a.nombre, COUNT(c.cod_cancion) AS cantidad_canciones
    FROM relacion_cancion_artista c
    JOIN artista a ON c.cod_artista = a.codigo_artista
    GROUP BY a.nombre
    ORDER BY cantidad_canciones DESC
    LIMIT 5
    """
    cur.execute(query)
    data = cur.fetchall()

    cur.close()
    conn.close()

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(data, columns=['Artista', 'Repeticiones'])
    return df

df_top_artistas = repiten_artistas()

# Crear la figura con Plotly Express
fig1 = px.bar(df_top_artistas, x='Artista', y='Repeticiones', title='Top 5 Artistas que más se repiten')


# Grafico que obtiene las 10 canciones mas escuchadas
def obtener_top_10_canciones():
    conn = psycopg2.connect(
        dbname="final",
        user="postgres",
        password="123456789",
        host="localhost"
    )
    cur = conn.cursor()

    query = """
    select nombre_cancion, stream  
    from cancion, info_plataformas where codigo_cancion=cod_cancion 
    order by stream desc
    limit 10
    """
    cur.execute(query)
    data = cur.fetchall()

    cur.close()
    conn.close()

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(data, columns=['Canción', 'Streams'])
    return df

df_top_canciones = obtener_top_10_canciones()

# Crear la figura con Plotly Express
fig2 = px.bar(df_top_canciones, x='Canción', y='Streams', title='Top 10 Canciones Más Escuchadas')



# Iniciar la aplicación Dash
app = Dash(__name__)

app.layout = html.Div([
    # Título
    html.H1("Las canciones más escuchadas"),

    # Introducción
    html.Div([
        html.H2("Introducción"),
        html.P("Para nuestro proyecto, hemos seleccionado la base de datos Canciones más reproducidas en Spotify en 2023, disponible en Kaggle, una plataforma de bases de datos de renombre a nivel mundial. Este conjunto de datos proporciona una amplia gama de información sobre las canciones más populares en 2023. Ofrece detalles acerca de las características de las canciones, su popularidad y su presencia en varias plataformas de música, entre las que se incluyen Spotify, Apple Music, Shazam y Deezer.")
    ]),

    # Problemática
    html.Div([
        html.H2("Problemática"),
        html.P("Nuestro objetivo principal consiste en identificar las tendencias en la industria musical, lo cual implica no solo determinar cuáles son las canciones más escuchadas, sino también analizar las variables que se relacionan con su éxito. Nos interesa profundizar en el entendimiento de la popularidad y el impacto de las canciones, y cómo estos factores varían dependiendo de las plataformas de música. ")
    ]),
    
    # Problema 1
    html.Div([
        html.H2("Causa del éxito"),
        dcc.Graph(
            id='grafico-top-artistas',
            figure=fig1
        )
    ]),
    
    # Problema 2
    html.Div([
        html.H3("Movimiento de las plataformas"),
        dcc.Graph(id='grafico-top-canciones',
        figure=fig2
        )
    ]),

])


if __name__ == '__main__':
    app.run_server(debug=True)
