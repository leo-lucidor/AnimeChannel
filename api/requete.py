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


def test():
    Utilisateur.Get.get_all_utilisateur(cnx)

test()