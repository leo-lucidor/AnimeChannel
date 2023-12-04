from connexionPythonSQL import *
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
            res =  []
            result = cnx.execute(text("select * from Utilisateur where email = :email;"), email=email)
            for row in result:
                print(row)
                res.append(row)
            return result
        
        


Utilisateur.Get.get_all_utilisateur(cnx)