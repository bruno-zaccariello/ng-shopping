import db

def tkUser(token):
    return db.TOKENS.get(token, False)