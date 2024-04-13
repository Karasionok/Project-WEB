from flask import Flask, render_template, redirect, request

from Forms.tracks_py import AddForm
from data import db_session
from Forms.login_py import LoginForm, RegisterForm
from data.users_py import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("DB/DataBase.sqlite")


@app.route('/')
@app.route('/index')
def index():
    track_list = [{'name': 'Blew',
                   'singer': 'Nirvana',
                   'album': 'Bleach',
                   'duration': '2:55'},
                  {'name': 'School',
                   'singer': 'Nirvana',
                   'album': 'Bleach',
                   'duration': '2:55'}
                  ]
    return render_template('main_menu.html', tracks=track_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        # if db_sess.query(User).filter(User.email == form.email.data).first():
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            # email=form.email.data,
            # about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if request.method == 'GET':
        return render_template('add.html', title='Добавить трек', form=form)
    elif request.method == 'POST':
        f = request.files['file']
        with open(AddForm.name if AddForm.name.endswith(".mp3") else AddForm.name + ".mp3", 'w') as file:
            file.write(f.read())
        return redirect('/index')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
