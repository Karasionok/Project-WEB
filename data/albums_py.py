# from flask import Flask, render_template, redirect
# from main import index.track_list
# from Forms.tracks_py import AddForm
# from data import db_session
# from Forms.login_py import LoginForm, RegisterForm
# from data.users_py import User
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# db_session.global_init("DB/DataBase.sqlite")
#
#
# @app.route('/')
# @app.route('/index')
# def albums():
#     track_list = [{'name': 'Blew',          # временно пока не доработали БД
#                    'singer': 'Nirvana',
#                    'album': 'Bleach',
#                    'duration': '2:55'},
#                   {'name': 'School',
#                    'singer': 'Nirvana',
#                    'album': 'Bleach',
#                    'duration': '2:55'}
#                   ]
#     for song in track_list:
#         if
#     return render_template('main_menu.html', tracks=track_list)
