import eel
from engine.controller.Login import try_login 
from engine import GlobalData
from engine.versioning.AppData import APP_DATA

# Funções de exposição (API-like)
@eel.expose
def requestLogin(funcional, senha):
    return try_login(funcional, senha)

@eel.expose
def requestUserData():
    user = GlobalData.get_logged_user()
    return user.toJSON()

@eel.expose
def requestAppVersion():
    return APP_DATA["version"]