from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.jogo import Jogo
from models.usuario import Usuario

jogo1 = Jogo('Batman Knight', 'Aventura', 'PS4/PC')
jogo2 = Jogo('Assassin Creed', 'Aventura', 'PS4/PC')
jogo3 = Jogo('Tomb Raider', 'Aventura', 'PS4/PC/XBOX')
jogo4 = Jogo('FIFA 24', 'Esporte', 'PS4/PC/XBOX')

game_list = [jogo1, jogo2, jogo3, jogo4]

usuario1 = Usuario('Tiago Santos', 'TiagoSz', 'gamestart')
usuario2 = Usuario('Alex Junior', 'Naldo24', 'kenpachi2')
usuario3 = Usuario('Cleisla Santos', 'Clei', '18021603')

usuarios = {usuario1._username: usuario1, 
            usuario2._username: usuario2, 
            usuario3._username: usuario3}

app = Flask(__name__)
app.secret_key = 'jogotecaalura+'

@app.route('/')
def render_home():
    return render_template('lista.html', title='Biblioteca de Jogos', games=game_list)     

@app.route('/newgame')
def new_game():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', next=url_for('new_game')))
    return render_template('novo_jogo.html', title='Novo Jogo')

@app.route('/create', methods=['POST',])
def create_game():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    new_game = Jogo(nome, categoria, console)
    game_list.append(new_game)
    return redirect(url_for('render_home'))

@app.route('/login')
def login():
    if 'usuario_logado' in session and session['usuario_logado'] != None:
        flash(session['usuario_logado'] +' já está logado!')
        return redirect(url_for('render_home'))
    next = request.args.get('next')
    return render_template('login.html', title='Faça seu login', next=next)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario._senha:
            session['usuario_logado'] = usuario._username
            flash(usuario._username +' logado com sucesso!')
            next_page = request.form['next']
            return redirect(url_for('render_home'))
        
    else:
        flash('Senha ou usuário inválidos!')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')
    return redirect(url_for('render_home'))


app.run(debug=True)