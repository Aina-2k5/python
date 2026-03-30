from app import app, db
from models import Movie

with app.app_context():
    db.create_all()
    
    movies = [
        Movie(title="Начало", director="Кристофер Нолан", year=2010, rating=8.8),
        Movie(title="Матрица", director="Лана Вачовски", year=1999, rating=8.7),
        Movie(title="Интерстеллар", director="Кристофер Нолан", year=2014, rating=8.6),
        Movie(title="Побег из Шоушенка", director="Фрэнк Дарабонт", year=1994, rating=9.3),
        Movie(title="Крестный отец", director="Фрэнсис Форд Коппола", year=1972, rating=9.2)
    ]
    
    db.session.add_all(movies)
    db.session.commit()
    print("База данных создана и заполнена!")