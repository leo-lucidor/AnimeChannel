from .app import app #, db
from flask import render_template, url_for, redirect, request, session, jsonify, send_file
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_wtf import FlaskForm
# from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField, IntegerField
# from wtforms.validators import DataRequired, Optional
# from wtforms import PasswordField
# from hashlib import sha256
# from .connexionPythonSQL import *
# from .requette import *

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/anime/<int:id>')
def anime(id):
    return render_template('anime.html', id=id)