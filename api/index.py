from .app import app #, db
from flask import render_template, url_for, redirect, request, session, jsonify, send_file
# from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Optional
# from hashlib import sha256
# from .connexionPythonSQL import *
# from .requette import *

# form

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Se connecter')

    def get_data(self):
        return (self.email.data, self.password.data)

# routes

@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.get_data()
        if email == None and password == None:
            return redirect(url_for('home'))
        else:
            session['utilisateur'] = email, password
            return redirect(url_for('home'))
    return render_template('home.html', form=form)


@app.route('/anime/<int:id>')
def anime(id):
    return render_template('anime.html', id=id)

@app.route('/logout')
def logout():
    session.pop('utilisateur', None)
    return redirect(url_for('home'))