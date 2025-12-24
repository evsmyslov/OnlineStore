from flask import Blueprint, render_template, request, redirect, url_for
from models.user import db, User

# Создаем Blueprint (модуль контроллера)
users_bp = Blueprint('users', __name__, url_prefix='/users')

# READ - Получение всех пользователей
@users_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('index.html', users=users)

# CREATE - Страница создания и обработка формы
@users_bp.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Использование конструктора (Pattern Factory method)
        new_user = User(name=name, email=email)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('users.get_users'))
        except:
            return "Ошибка при добавлении пользователя"
    return render_template('user_form.html', user=None)

# UPDATE - Обновление пользователя
@users_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        try:
            db.session.commit()
            return redirect(url_for('users.get_users'))
        except:
            return "Ошибка при обновлении"
    return render_template('user_form.html', user=user)

# DELETE - Удаление пользователя
@users_bp.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('users.get_users'))
    except:
        return "Ошибка при удалении"