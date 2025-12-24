from flask import Flask, redirect
from models.user import db
from controllers.user_controller import users_bp

app = Flask(__name__)
# Настройка БД (SQLite для простоты)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация БД с приложением
db.init_app(app)

# Регистрация контроллеров
app.register_blueprint(users_bp)

@app.route('/')
def index():
    return redirect('/users')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаем таблицы при запуске
    app.run(debug=True, port=5000)