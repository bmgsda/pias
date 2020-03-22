def search_user_SQL(funcional):
    return "SELECT * FROM USU_USUARIO WHERE USU_FUNCIONAL = UPPER('" + funcional + "')"
