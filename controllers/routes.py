from flask import render_template, request, redirect, url_for


listaLivros = [{
            'Titulo' : 'O Pequeno Príncipe',
            'Publicacao' : 1943,
            'Autor': 'Antoine de Saint-Exupéry​',
            'Genero': 'Literatura infantojuveni',
            'Editora': 'Agir',
            'Idioma': 'Português Brasileiro',
            'Classificacao': 'Livre',
            'Observacao': 'SimEmbora seja frequentemente catalogado como literatura infantil, O Pequeno Príncipe transcende faixas etárias, oferecendo reflexões profundas sobre temas como amizade, amor, solidão e o sentido da vida. A obra é conhecida por suas metáforas e simbolismos, que permitem múltiplas interpretações e a tornam relevante em diferentes fases da vida. Desde sua publicação, o livro tem encantado leitores ao redor do mundo, sendo traduzido para mais de 160 idiomas e dialetos.',
        }]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('home.html')


    # Rota de livros
    @app.route('/lista', methods=['GET', 'POST'])
    def lista():
        if request.method == 'POST':
            # Verifica se todos os campos obrigatórios existem
            if (request.form.get('titulo') and 
                request.form.get('data') and 
                request.form.get('autor') and 
                request.form.get('genero') and 
                request.form.get('editora') and 
                request.form.get('idioma') and 
                request.form.get('classificacao') and 
                request.form.get('observacao')):
                
                novoLivro = {
                    'Titulo': request.form.get('titulo'),
                    'Publicacao': request.form.get('data'),
                    'Autor': request.form.get('autor'),
                    'Genero': request.form.get('genero'),
                    'Editora': request.form.get('editora'),
                    'Idioma': request.form.get('idioma'),
                    'Classificacao': request.form.get('classificacao'),
                    'Observacao': request.form.get('observacao')
                }
                listaLivros.append(novoLivro)
                
            return redirect(url_for('lista'))
        
        return render_template('lista.html',
                            listaLivros=listaLivros)



    # Rota de cadastro de livros (em dicionário)
    @app.route('/cadastroLivro', methods=['GET', 'POST'])
    def cadastroLivro():
        return render_template('cadastroLivro.html')

    
