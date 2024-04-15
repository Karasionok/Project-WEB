from flask import Flask, render_template, redirect, request

from Forms.tracks_py import AddForm
from data import db_session
from Forms.login_py import LoginForm, RegisterForm
from data.add import Track
from data.albums_py import Album
from data.singers_py import Singer
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
    track_name = 'In Bloom'
    track_path = 'tracks/In Bloom.mp3'

    return render_template('index.html', tracks=track_list,
                           track_name=track_name, track_path=track_path)


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
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
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
        f = form.track.data
        with (open(f'static/tracks/{form.name.data if form.name.data.endswith(".mp3") else form.name.data + ".mp3"}', 'wb')
              as file):
            file.write(f.read())
        db_sess = db_session.create_session()
        # condition_s = db_sess.query(Singer).filter(Singer.name == form.singer.data).first()
        # if condition_s:
        #     condition_a = db_sess.query(Album).filter(
        #         Album.name == form.album.data and Album.singer_id == condition_s.id).first()
        #     if condition_a:
        #         condition_t = db_sess.query(Track).filter(
        #             Track.name == form.name.data and Track.album_id == condition_a.id).first()
        #         if condition_t:
        #             return render_template('add.html', title='Добавление трека',
        #                                    form=form,
        #                                    message="Такой трек уже есть")
        # if db_sess.query(Track).filter(Track.name == form.name.data).first():
        #     return render_template('add.html', title='Добавление трека',
        #                            form=form,
        #                            message="Такой трек уже есть")
        singer = Singer(
            name=form.singer.data
        )
        album = Album(
            album_name=form.album.data,
            singer_id=singer.id
        )
        db_sess.add(album)
        db_sess.commit()
        track = Track(
            name=form.name.data,
            album_id=album.id,
            duration=form.duration.data,
            path=f'tracks/{form.name.data}.mp3',
            singer_id=singer.id
        )

        db_sess.add(singer)
        db_sess.add(album)
        db_sess.add(track)
        db_sess.commit()
        return redirect('/index')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
