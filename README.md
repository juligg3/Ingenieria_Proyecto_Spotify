# Ingenieria_Proyecto_Spotify

Repositorio del proyecto Ingeniería de datos proviene de: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/ 

# Introducción

Para nuestro proyecto, hemos seleccionado la base de datos 'Canciones más reproducidas en Spotify en 2023', disponible en Kaggle, una plataforma de bases de datos de renombre a nivel mundial. Este conjunto de datos proporciona una amplia gama de información sobre las canciones más populares en 2023. Ofrece detalles acerca de las características de las canciones, su popularidad y su presencia en varias plataformas de música, entre las que se incluyen Spotify, Apple Music, Shazam y Deezer.

# Problemática

Nuestro objetivo principal consiste en identificar las tendencias en la industria musical, lo cual implica no solo determinar cuáles son las canciones más escuchadas, sino también analizar las variables que se relacionan con su éxito. Nos interesa profundizar en el entendimiento de la popularidad y el impacto de las canciones, y cómo estos factores varían dependiendo de las plataformas de música.

# Reglas de negocio

1. Una canción puede estar en varias plataformas, pero las plataformas solo tienen una vez la canción.
2. Una canción tiene solo una composición por categoría.
3. La composición refleja los indicadores.
4. Cada plataforma tiene datos independientes.
5. Una canción puede tener varios artistas 
6. Cada canción es identificada con un código único.
7. El código de la canción será el mismo en cada aplicación.
8. Cada canción  tiene un porcentaje por cada indicador.
9. Si alguna canción no está en alguna aplicación se identifica con nulo.
10. Un artista puede participar en varias canciones, por lo que un artista puede repetirse.
11. No todas las canciones tienen reproducciones en algunas aplicaciones.
12. Cada artista tiene su código único.
13. Cada canción tiene como mínimo 2 codigos, el de la canción y el de n número de artistas.
14. El código de artista será el mismo en cada aplicación.
15. El número de reproducciones de una canción es único e independiente en cada aplicación.

# Problemas de análisis

1. Identificar cual o cuales son los artistas con mejores estadísticas y analizar la causa de su éxito. Poder diferenciar si es el artista el que resalta o simplemente la corriente de la moda musical es la que lo impulsa.
2. Identificar aquellos artistas cuya repetición en la lista es mínima pero su número de reproducciones es alto. Analizar un posible one hit wonder .”Un cantante de un solo éxito​ (en inglés one-hit wonder) o grupo de un solo éxito, similar a la expresión «flor de un día», es un término utilizado a propósito para designar a un artista o grupo musical cuya popularidad o éxito se debe únicamente a una sola canción.”
3. Identificar por medio del número de reproducciones en cada aplicación las tendencias musicales o de artistas y analizar por medio de comparación que corriente musical o artista es más afín a la aplicación, por ejemplo, podría profundizar si los usuarios de apple music y los de spotify varían lo que escuchan lo que conlleva a ver si ser usuarios ios o android tienen gustos musicales distintos.
4. Identificar el top de canciones y analizar si su nivel de composición y bailabilidad tiene relación con su éxito en las tablas o por el contrario hay canciones con mejor composición y bailabilidad que no triunfan tanto como las otras, lo cual trae a colación variables externas que apoyan el éxito de estas canciones.

