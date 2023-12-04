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
    animes = [
        {
            'id': 1,
            'titre': 'Naruto',
            'description': 'Naruto est un garçon un peu spécial. Il est toujours tout seul et son caractère fougueux ne l\'aide pas à se faire apprécier dans son village. Malgré cela, il garde au fond de lui une ambition: celle de devenir un "maître Hokage", la plus haute distinction dans l\'ordre des ninjas, et ainsi obtenir la reconnaissance de ses pairs mais cela ne sera pas de tout repos...',
            'image': 'https://www.nautiljon.com/images/anime/00/00/naruto_1.jpg',
            'date': '2002',
            'auteur': 'Masashi Kishimoto',
            'genre': 'Action, Aventure, Comédie, Drame, Fantasy, Shônen',
            'studio': 'Studio Pierrot',
            'note': 4.5,
            'nbNote': 100000,
            'nbEpisode': 220,
            'dureeEpisode': 24,
            'statut': 'Terminé',
            'type': 'Série',
            'lien': 'https://www.nautiljon.com/animes/naruto.html'
        },
        {
            'id': 2,
            'titre': 'Naruto Shippuden',
            'description': 'Naruto Shippuden est la suite de Naruto. On y retrouve tous les personnages plus mûrs et plus âgés. L\'intrigue tourne autour des aventures de Naruto et Sakura à la recherche de Sasuke, parti de Konoha pour acquérir de nouveaux pouvoirs, mais on y découvre aussi les objectifs de l\'Akatsuki.',
            'image': 'https://www.nautiljon.com/images/anime/00/00/naruto_shippuden_1.jpg',
            'date': '2007',
            'auteur': 'Masashi Kishimoto',
            'genre': 'Action, Aventure, Comédie, Drame, Fantasy, Shônen',
            'studio': 'Studio Pierrot',
            'note': 4.5,
            'nbNote': 100000,
            'nbEpisode': 500,
            'dureeEpisode': 24,
            'statut': 'Terminé',
            'type': 'Série',
            'lien': 'https://www.nautiljon.com/animes/naruto+shippuden.html'
        },
        {
            'id': 3,
            'titre': 'Boruto: Naruto Next Generations',
            'description': 'Cette série fera suite à Naruto Shippuden et se passera donc après les événements du manga. Elle se concentrera principalement sur le fils de Naruto, Boruto, mais il est fort probable que l\'on voit les autres personnages de la génération précédente.',
            'image': 'https://www.nautiljon.com/images/anime/00/00/boruto_naruto_next_generations_1.jpg',
            'date': '2017',
            'auteur': 'Masashi Kishimoto',
            'genre': 'Action, Aventure, Comédie, Drame, Fantasy, Shônen',
            'studio': 'Studio Pierrot',
            'note': 4.5,
            'nbNote': 100000,
            'nbEpisode': 220,
            'dureeEpisode': 24,
            'statut': 'En cours',
            'type': 'Série',
            'lien': 'https://www.nautiljon.com/animes/boruto+naruto+next+generations.html'
        },
        {
            'id': 4,
            'titre': 'One Piece',
            'description': 'Gol D. Roger était connu comme le "Roi Pirate", l\'être le plus fort et le plus infâme d\'avoir navigué sur la Grand Line. La capture et l\'exécution de Roger par le gouvernement mondial a apporté un changement dans le monde entier. Ses dernières paroles avant sa mort ont révélé l\'existence du plus grand trésor du monde, One Piece. C\'est cette révélation qui a amené le Grand Age des Pirates, hommes qui rêvaient de trouver One Piece (ce qui promet une quantité illimitée de richesses et de renommée), et assez de courage pour affronter la Grand Line (où la majorité des dangers du monde se cache).',
            'image': 'https://www.nautiljon.com/images/anime/00/00/one_piece_1.jpg',
            'date': '1999',
            'auteur': 'Eiichirô Oda',
            'genre': 'Action, Aventure, Comédie, Drame, Fantasy, Shônen',
            'studio': 'Toei Animation',
            'note': 4.5,
            'nbNote': 100000,
            'nbEpisode': 1000,
            'dureeEpisode': 24,
            'statut': 'En cours',
            'type': 'Série',
            'lien': 'https://www.nautiljon.com/animes/one+piece.html'
        }]
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.get_data()
        if email == None and password == None:
            return redirect(url_for('home'))
        else:
            session['utilisateur'] = email, password
            return render_template('home.html', form=form, name=email, animes=animes)
    return render_template('home.html', form=form, animes=animes)


@app.route('/anime/<int:id>')
def anime(id):
    return render_template('anime.html', id=id)

@app.route('/logout')
def logout():
    session.pop('utilisateur', None)
    return redirect(url_for('home'))