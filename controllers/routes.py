from flask import render_template, request, redirect, url_for

def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('home.html')

    # Rota de games
    @app.route('/games')
    def lista():
        return render_template('lista.html')
    
    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadastroLivro')
    def cadastroLivro():
        return render_template('cadastroLivro.html')
