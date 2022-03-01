from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from livereload import Server
from controllers.table_controller import table_blueprint
from controllers.teams_controller import teams_blueprint
from controllers.games_controller import games_blueprint


# from controllers.book_controller import books_blueprint
app = Flask(__name__)

ENV = 'prod'

if ENV =='dev':
    app.debug= True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'http://localhost:5000'
else:
    app.debug= False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cpznoflvpdznkq:ff678a0d848c30b6d4fa86484024ad9fc63a56b5d49a2fe2eb42df386a70c265@ec2-18-204-131-56.compute-1.amazonaws.com:5432/d4ion1dim6m1jc'

db = SQLAlchemy(app)

app.register_blueprint(table_blueprint)
app.register_blueprint(teams_blueprint)
app.register_blueprint(games_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
