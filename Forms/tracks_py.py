from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    album = StringField('Альбом', validators=[DataRequired()])
    singer = StringField('Исполнитель', validators=[DataRequired()])
    duration = StringField('Длительность', validators=[DataRequired()])
    submit = SubmitField('Добавить')
