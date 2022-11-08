# Importing the necessary modules and libraries
from flask import Flask, render_template
from flask_migrate import Migrate
from rest.blueprints import blueprint
#from model.Unclassified import db


def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    #db.init_app(app)  # Initializing the database
    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/pictures')
migrate = Migrate(app)  #, db)  # Initializing the migration

@app.route('/pictures/get-class')
def index():
    return render_template('index.html')

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)