from flask import Flask, render_template
from models import Movie, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    movies_list = Movie.query.all()
    return render_template('movies.html', movies=movies_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)