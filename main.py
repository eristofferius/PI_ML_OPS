#import uvicorn
from fastapi import FastAPI




app = FastAPI()


@app.get("/")
async def ruta_prueba():
    return {"message" : "TEST"}


# Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. Ejemplo de retorno:
@app.get("/developer")
def developer( desarrollador : str ): 
    return {"message" : "developer"}



#  Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
@app.get("/userdata")
def userdata( User_id : str ):
    return {"message" : "userdata"}

#  Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
@app.get("/UserForGenre")
def UserForGenre( genero : str ):
    return {"message" : "UserForGenre"}


#Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)
@app.get("/best_developer_year")
def best_developer_year( año : int ):
    return {"message" : "best_developer_year"}



# Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de 
# reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.
@app.get("/developer_reviews_analysis")
def developer_reviews_analysis( desarrolladora : str ): 
    return {"message" : "developer_reviews_analysis"}



#Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

# Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.
@app.get("/recomendacion_juego")
def recomendacion_juego( id_de_producto ):
    return {"message" : "recomendacion_juego"}

# Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.
@app.get("/recomendacion_usuario")
def recomendacion_usuario( id_de_usuario ): 
    return {"message" : "recomendacion_usuario"}


#Video
