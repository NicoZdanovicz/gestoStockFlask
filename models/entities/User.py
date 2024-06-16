from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, usuario, correo, contraseña) -> None:
        self.id = id
        self.usuario = usuario
        self.correo = correo
        self.contraseña = contraseña

    @classmethod
    def check_contraseña(self, check_contraseña, contraseña):
        return check_contraseña == contraseña
    
class Register():
    def __init__(self, usuario, correo, contraseña) -> None:
        self.usuario = usuario
        self.correo = correo
        self.contraseña = contraseña