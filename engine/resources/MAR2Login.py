from engine.model.User import User

def try_login(funcional, senha):
    try:
        if (funcional == '987313033') and (senha == '170698'):
            return User(funcional, 'TATSUYA', 'BRUNO TATSUYA MASUNAGA SANTOS')
    except: 
        pass