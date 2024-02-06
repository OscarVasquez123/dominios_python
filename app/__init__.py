from flask import Flask

# crear el objeto pricipal 
app = Flask(__name__)

#importar a las rutas definidas 
from app import routes

if __name__ == '__main__':
    app.run()