from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT id, usuario, correo, contraseña FROM usuarios 
                    WHERE usuario = '{}' """.format(user.usuario)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row != None:
                user = User(row[0], row[1], row[2], User.check_contraseña(row[3], user.contraseña))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """ SELECT id, usuario, correo, contraseña FROM usuarios 
                    WHERE id = '{}' """.format(id)
            cursor.execute(sql)
            row = cursor.fetchone()

            if row != None:
                user = User(row[0], row[1], row[2], None)
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def registro(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO usuarios (usuario, correo, contraseña) 
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (user.usuario, user.correo, user.contraseña))
            db.connection.commit()
            return user
        
        except Exception as ex:
            raise Exception(ex)