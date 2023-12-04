from .app import app #, db
from flask import render_template, url_for, redirect, request, session, jsonify, send_file
# from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Optional
# from hashlib import sha256
from .connexionPythonSQL import *
from .requette import *

cnx = ouvrir_connexion()

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
    liste_animes = Anime.Get.get_all_anime(cnx)
    
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.get_data()
        if email != None and password != None:   
            user = Utilisateur.Get.get_utlisateurs_by_mail(cnx, email)
            if user != None:
                if user[4] == password:
                    session['utilisateur'] = email, password, Utilisateur.Get.get_nom_with_email(cnx, email)
            else:
                return render_template('home.html', form=form, erreur="Email ou mot de passe incorrect")
        return render_template('home.html', form=form, animes=liste_animes)
    return render_template('home.html', form=form, animes=liste_animes)


@app.route('/anime/<int:id>')
def anime(id):
    anime = Anime.Get.get_anime_by_id(cnx, id)
    return render_template('anime.html', anime=anime) 

@app.route('/logout')
def logout():
    session.pop('utilisateur', None)
    return redirect(url_for('home'))