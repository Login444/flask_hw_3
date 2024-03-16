# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request
from models import db, User
from flask_wtf.csrf import CSRFProtect
from forms import SignInForm
import cryptocode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_2.db'
app.config['SECRET_KEY'] = 'e302ae76c64f5f3e3aec3b1dfea6c6d33b45ebf82392cb3dc2c8c1317b38f8cf'
"""
>>> import secrets
>>> secrets.token_hex()
"""
csrf = CSRFProtect(app)
db.init_app(app)
SECRET_CRYPTOKEY = 'f464805e0ffc4c808af0933217fc4cb444497f0d9fcc01bda9c6133fd4229509'


@app.route('/', methods=['GET', 'POST'])
def registration_form():
    form = SignInForm()
    if request.method == 'POST' and form.validate():
        user_name = form.user_name.data
        user_lastname = form.user_lastname.data
        user_email = form.user_email.data
        user_password = form.user_password.data
        password_encoded = cryptocode.encrypt(user_password, SECRET_CRYPTOKEY)
        add_user_db(user_name, user_lastname, user_email, password_encoded)
        return 'Registration completed'
    return render_template('form.html', title='Registration', form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('Ok')

def add_user_db(u_name: str, u_lastname: str, u_email: str, u_password: str):
    user = User(user_name=u_name, user_lastname=u_lastname, user_email=u_email, user_password=u_password)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
