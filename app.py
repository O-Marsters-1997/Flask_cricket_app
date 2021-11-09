from flask import Flask, render_template
from controllers.table_controller import table_blueprint
from controllers.teams_controller import teams_blueprint
from controllers.games_controller import games_blueprint


# from controllers.book_controller import books_blueprint
app = Flask(__name__)

app.register_blueprint(table_blueprint)
app.register_blueprint(teams_blueprint)
app.register_blueprint(games_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
