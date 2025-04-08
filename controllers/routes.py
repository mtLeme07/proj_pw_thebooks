from flask import render_template, request, redirect, url_for

def init_app(app):
    # Cria a primeira rota do site
    @app.route("/")
    #Cria uma função
    def home():
        return render_template('home.html')
  

    @app.route("/lista")
    def lista():
        return render_template('lista.html',)
    

    @app.route("/cadastroLivro")
    def cadastroLivro():
        return render_template('cadastroLivro.html')