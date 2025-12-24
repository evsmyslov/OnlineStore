from flask_sqlalchemy import SQLAlchemy

# Инициализация БД (Паттерн Singleton для соединения)
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), default='customer')

    def __repr__(self):
        return f'<User {self.name}>'