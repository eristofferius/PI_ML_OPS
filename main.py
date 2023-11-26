import uvicorn
from fastapi import FastAPI

#app = FastAPI()

#http://127.0.0.1:8000

#@app.get("/inicio")
#async def ruta_prueba():
 #   return {"message" : "TEST"}


app = FastAPI()


@app.get("/inicio")
async def ruta_prueba():
    return {"message" : "TEST"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

#def developer( desarrollador : str ): Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. Ejemplo de retorno:

#def userdata( User_id : str ): Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

#def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por 
#año de lanzamiento.

  
#def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

#def developer_reviews_analysis( desarrolladora : str ): Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

#Deployment: Conoces sobre Render y tienes un tutorial de Render que te hace la vida mas fácil :smile: . También podrías usar Railway, o cualquier otro servicio que permita que la API pueda ser consumida desde la web.

#Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)


#def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

#def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

#Video
