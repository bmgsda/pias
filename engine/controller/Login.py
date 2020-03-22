from engine.resources import MAR2Login
from engine.database import SQLExecutor
from engine import GlobalData

# Funções chamadas pela camada de exposição
def try_login(funcional, senha):
    user = MAR2Login.try_login(funcional, senha)
    if (user is None):
        return "Falha de login"
    else:
        if not check_user(funcional):
            return "Usuário não cadastrado"
        else:
            GlobalData.set_logged_user(user)
            return "Success"

# Funções Auxiliares
def check_user(funcional):
    search_user_result = SQLExecutor.search_user(funcional)
    if not search_user_result:
        return False
    else:
        return True
