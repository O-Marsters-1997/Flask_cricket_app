from flask import Flask, render_template
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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ftyceuqgtqwfeu:27da0604226e180b6266c1364c2be036531ddecf08a594d656e74c9b40fe6957@ec2-99-80-108-106.eu-west-1.compute.amazonaws.com:5432/da2p5f62l76kqk'


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
