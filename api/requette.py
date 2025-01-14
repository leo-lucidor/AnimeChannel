from .connexionPythonSQL import *
from sqlalchemy import text
cnx = ouvrir_connexion()

class Utilisateur:
    class Get:
        def get_all_utilisateur(cnx):
            res =  []
            result = cnx.execute(text("select * from Utilisateur;"))
            for row in result:
                print(row)
                res.append(row)
            return result
        
        def get_utlisateurs_by_id(cnx, id):
            res =  []
            result = cnx.execute(text("select * from Utilisateur where id = :id;"), id=id)
            for row in result:
                print(row)
                res.append(row)
            return result
        
        def get_utlisateurs_by_mail(cnx, email):
            result = cnx.execute(text("select * from Utilisateur where email = '" + email + "';"))
            for row in result:
                return row

        def get_nom_with_email(cnx, email):
            result = cnx.execute(text("select nom from Utilisateur where email = '" + email + "';"))
            for row in result:
                return row[0]
            return result
        
class MotsDePasse:
    class Get:
        def get_mdp_by_id(cnx, id):
            result = cnx.execute(text("select motDePasse from Utilisateur where idUtilisateur = " + str(id) + ";"))
            for row in result:
                print(row[0])
                return row[0]
            return result
        
        def get_mdp_by_email(cnx, email):
            result = cnx.execute(text("select motDePasse from Utilisateur where email =" + email + ";"))
            for row in result:
                print(row[0])
                return row[0]
            return result

class Anime:
    class Get:
        def get_all_anime(cnx):
            res =  []
            result = cnx.execute(text("select * from Anime natural join CategorieAnime;"))
            for row in result:
                res.append(row)
            return res
        
        def get_anime_by_id(cnx, id):
            res =  []
            result = cnx.execute(text("select * from Anime where idAnime = '" + str(id) + "';"))
            for row in result:
                res.append(row)
            return result
        
        def get_anime_by_name(cnx, name):
            res =  []
            result = cnx.execute(text("select * from Anime where nameA = :name;"), name=name)
            for row in result:
                print(row)
                res.append(row)
            return result
        

class Episode:
    class Get:
        def get_episode_by_id(cnx, id):
            res =  []
            result = cnx.execute(text("select * from Episode where idEpisode = :id;"), id=id)
            for row in result:
                print(row)
                res.append(row)
            return result
        
        def get_episode_by_name(cnx, name):
            res =  []
            result = cnx.execute(text("select * from Episode where nameE = :name;"), name=name)
            for row in result:
                print(row)
                res.append(row)
            return result
        
        def get_episode_by_id_and_numeroEpisode(cnx, id, numeroEpisode):
            result = cnx.execute(text("select * from Episode where idAnime = " + str(id) + " and numeroEpisode = " + str(numeroEpisode) + ";"))
            for row in result:
                print(row)
                return row
            return result
        
        def get_all_episode(cnx, id):
            res =  []
            result = cnx.execute(text("select * from Episode natural join Anime where idAnime = '"+str(id)+"';"))
            for row in result:
                res.append(row)
            return res
        

# Utilisateur.Get.get_all_utilisateur(cnx)
# Anime.Get.get_all_anime(cnx)
# Episode.Get.get_all_episode(cnx)
# Episode.Get.get_episode_by_id_and_numeroEpisode(cnx, 1, 1)

