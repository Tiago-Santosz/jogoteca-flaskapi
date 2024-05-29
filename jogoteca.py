from flask import Flask, render_template, request, redirect
from models.jogo import Jogo

jogo1 = Jogo('Batman Knight', 'Aventura', 'PS4/PC')
jogo2 = Jogo('Assassin Creed', 'Aventura', 'PS4/PC')
jogo3 = Jogo('Tomb Raider', 'Aventura', 'PS4/PC/XBOX')
jogo4 = Jogo('FIFA 24', 'Esporte', 'PS4/PC/XBOX')

game_list = [jogo1, jogo2, jogo3, jogo4]


app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('lista.html', title='Biblioteca de Jogos', games=game_list)     

@app.route('/newgame')
def new_game():
    return render_template('novo_jogo.html', title='Novo Jogo')

@app.route('/create', methods=['POST',])
def create_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    new_game = Jogo(nome, categoria, console)
    game_list.append(new_game)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', title='Faça seu login')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'gamestart' == request.form['senha']:
        return redirect('/')
    else:
        return redirect('/login')


app.run(debug=True)