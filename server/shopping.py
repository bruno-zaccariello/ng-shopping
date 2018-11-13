from flask import Flask, jsonify, request
from flask_cors import CORS
import requests as r

import db
from tokenize import genToken as gTk
from extra import tkUser

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Index Page"

@app.route('/api/produtos')
def get_produtos():
    try:
        response = jsonify({
            'response':True, 
            'produtos':[p.get() for p in db.PRODUTOS]
            })
    except:
        return jsonify({'response':False}), 500
    return response, 200

@app.route('/api/produtos/<int:id>')
def get_produto(id, json=True):
    try:
        for produto in db.PRODUTOS:
            _produto = produto.get()
            if str(_produto['id']) == str(id):
                response = jsonify({'response':True, 'produto':_produto}) 
                return (response, 200) if json else produto
        return jsonify({'response':False}), 404
    except:
        return jsonify({'response':False}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    login = request.json.get('login')
    senha = request.json.get('senha')
    try:
        dbUser = db.USERS.get(login)
        token = gTk()
        if dbUser.authenticate(login, senha):
            dbUser.activateToken(token)
            db.TOKENS[token] = dbUser
            return jsonify({'response':True, 'login':True, 'token':token}), 200
        return jsonify({'response':True, 'login': False}), 200
    except:
        return jsonify({'response':False}), 500

@app.route('/api/auth/token', methods=['POST'])
def validate_token():
    try:
        token = request.json.get('token')
        user = tkUser(token)
        if user:
            return jsonify({'response':True, 'validation':user.checkToken()}), 200
        return jsonify({'response':True, 'validation':False})
    except:
        return jsonify({'response':False}), 500

@app.route('/api/carrinho/add/', methods=['POST'])
def add_carrinho():
    print('carrinho')
    id = request.json.get('pid')
    token = request.json.get('token')
    user = tkUser(token)
    print('adicionado')
    try:
        produto = get_produto(id, False)
        user.carrinho.addProduto(produto)
        print(user.carrinho)
        return jsonify({'response':True}), 200
    except Exception:
        return jsonify({'response':False}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')