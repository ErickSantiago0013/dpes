from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
DATABASE = 'database.db'
app.secret_key = 'mysecretkey'  # Chave secreta para a sessão
app.config['UPLOAD_FOLDER'] = 'uploads'  # Pasta para salvar as fotos de perfil

def obter_usuario_id_atual():
    if 'username' in session:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM users WHERE username = ?', (session['username'],))
        usuario_id = cursor.fetchone()[0]
        conn.close()
        return usuario_id
    else:
        return None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Verificar se o usuário existe no banco de dados
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            # Autenticação bem-sucedida, definir a sessão do usuário
            session['username'] = username
            return redirect('/dashboard')
        else:
            # Autenticação falhou, exibir mensagem de erro
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render_template('login.html', error_message=error_message)
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Verificar se o usuário já existe no banco de dados
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            error_message = 'O nome de usuário já está em uso. Escolha outro nome.'
            return render_template('register.html', error_message=error_message)
        else:
            # Inserir o novo usuário no banco de dados
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()

            # Autenticação bem-sucedida, definir a sessão do usuário
            session['username'] = username

            return redirect('/login')
    else:
        return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Obter o nome de usuário da sessão atual (assumindo que você armazenou essa informação na sessão durante o login)
    username = session.get('username')

    # Conectar-se ao banco de dados e obter as configurações do usuário
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Verificar se existe uma configuração para o usuário atual
    cursor.execute("SELECT tema FROM configuracoes WHERE usuario_id = ?", (username,))
    result = cursor.fetchone()
    tema = result[0] if result else None

    # Fechar a conexão com o banco de dados
    conn.close()

    # Renderizar o template 'dashboard.html' com as configurações e o nome de usuário
    return render_template('dashboard.html', username=username, tema=tema)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    # Obter os dados da mensagem enviada pelo usuário
    mensagem = request.form['mensagem']
    usuario_id = obter_usuario_id_atual()  # Função para obter o ID do usuário atualmente logado

    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Inserir a mensagem na tabela "conversas" com o usuário associado
    cursor.execute('INSERT INTO conversas (usuario, mensagem) VALUES (?, ?)', (usuario_id, mensagem))

    # Salvar as alterações e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionar para a página de visualização da conversa
    return redirect('/conversa')

@app.route('/conversa')
def visualizar_conversa():
    usuario_id = obter_usuario_id_atual()  # Função para obter o ID do usuário atualmente logado

    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Recuperar a conversa do usuário atual
    cursor.execute('SELECT * FROM conversas WHERE usuario_id = ?', (usuario_id,))
    conversa = cursor.fetchall()

    # Salvar as alterações e fechar a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Renderizar a página de visualização da conversa com os registros filtrados
    return render_template('conversa.html', conversa=conversa)


@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')


@app.route('/salvar_candidato', methods=['POST'])
def salvar_candidato():
    nome = request.form['nome']
    idade = request.form['idade']
    sexo = request.form['sexo']
    estado_civil = request.form['estado_civil']
    quantidade_filhos = request.form['quantidade_filhos']
    idade_filho_1 = request.form['idade_filho_1']
    escolaridade = request.form['escolaridade']
    area_formacao = request.form['area_formacao']
    entidade = request.form['entidade']
    logradouro = request.form['logradouro']
    bairro = request.form['bairro']
    cidade = request.form['cidade']
    estado = request.form['estado']
    filial = request.form['filial']
    cargo = request.form['cargo']
    admissao = request.form['admissao']
    praca = request.form['praca']
    vale_transporte = request.form['vale_transporte']
    entrevistador = request.form['entrevistador']
    data_entrevista = request.form['data_entrevista']
    status = request.form['status']
    grau_anotacao = request.form['grau_anotacao']
    anotacao = request.form['anotacao']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO candidatos (
            nome, idade, sexo, estado_civil, quantidade_filhos, idade_filho_1,
            escolaridade, area_formacao, entidade, logradouro, bairro, cidade,
            estado, filial, cargo, admissao, praca, vale_transporte, entrevistador,
            data_entrevista, status, grau_anotacao, anotacao
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, idade, sexo, estado_civil, quantidade_filhos, idade_filho_1,
          escolaridade, area_formacao, entidade, logradouro, bairro, cidade,
          estado, filial, cargo, admissao, praca, vale_transporte, entrevistador,
          data_entrevista, status, grau_anotacao, anotacao))
    conn.commit()
    conn.close()

    return redirect('/cadastro')

    #return redirect('/dashboard')

# Rota para renderizar a página de relatórios
@app.route('/relatorio')
def relatorios():
    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Executar a consulta para obter os dados dos candidatos
    cursor.execute('SELECT * FROM candidatos')
    candidatos = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Renderizar o template e passar os dados dos candidatos para a página
    return render_template('relatorio.html', candidatos=candidatos)

# Rota para buscar os detalhes de um candidato pelo ID
@app.route('/get-candidate-details', methods=['POST'])
def get_candidate_details():
    # Obter o ID do candidato enviado pelo frontend
    id = request.form.get('id')

    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Executar a consulta para obter os detalhes do candidato pelo ID
    cursor.execute('SELECT * FROM candidatos WHERE id = ?', (id,))
    candidato = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Retornar os detalhes do candidato em formato JSON
    return jsonify(candidato)

def obter_configuracao(usuario):
    # Conectar ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Executar a consulta para obter a configuração do usuário
    cursor.execute('SELECT * FROM configuracoes WHERE usuario = ?', (usuario,))
    configuracao = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    cursor.close()
    conn.close()

    return configuracao

def salvar_configuracoes_no_banco(usuario, tema, fonte, tamanho_fonte, cor_fonte, foto_perfil):
    # Conectar ao banco de dados
    conexao = sqlite3.connect(DATABASE)
    cursor = conexao.cursor()

    # Verificar se a tabela 'configuracoes' já existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='configuracoes'")
    tabela_existe = cursor.fetchone()

    if tabela_existe:
        # Verificar se já existe uma configuração para o usuário
        configuracao = obter_configuracao(usuario)

        if configuracao:
            # Atualizar os valores da configuração existente
            cursor.execute("UPDATE configuracoes SET tema=?, fonte=?, tamanho_fonte=?, cor_fonte=? WHERE usuario=?",
                        (tema, fonte, tamanho_fonte, cor_fonte, usuario))
        else:
            # Criar uma nova configuração para o usuário
            cursor.execute("INSERT INTO configuracoes (usuario, tema, fonte, tamanho_fonte, cor_fonte) VALUES (?, ?, ?, ?, ?)",
                        (usuario, tema, fonte, tamanho_fonte, cor_fonte))
    else:
        # Criar a tabela 'configuracoes' e inserir os valores da configuração
        cursor.execute('''CREATE TABLE configuracoes (
                            id INTEGER PRIMARY KEY,
                            usuario TEXT,
                            tema TEXT,
                            fonte TEXT,
                            tamanho_fonte INTEGER,
                            cor_fonte TEXT,
                        )''')
        cursor.execute("INSERT INTO configuracoes (usuario, tema, fonte, tamanho_fonte, cor_fonte) VALUES (?, ?, ?, ?, ?)",
                    (usuario, tema, fonte, tamanho_fonte, cor_fonte))

    # Salvar as alterações no banco de dados
    conexao.commit()
    conexao.close()

@app.route('/configuracoes', methods=['GET', 'POST'])
def configuracoes():
    if request.method == 'POST':
        # Obter os valores do formulário
        tema = request.form.get('tema')
        fonte = request.form.get('fonte')
        tamanho_fonte = request.form.get('tamanho_fonte')
        cor_fonte = request.form.get('cor_fonte')

        # Verificar se já existe uma configuração para o usuário
        usuario_id = obter_usuario_id_atual()
        if usuario_id:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM configuracoes WHERE usuario_id = ?", (usuario_id,))
            configuracao = cursor.fetchone()

            if configuracao:
                # Atualizar os valores da configuração existente
                cursor.execute("UPDATE configuracoes SET tema=?, fonte=?, tamanho_fonte=?, cor_fonte=? WHERE usuario_id=?",
                               (tema, fonte, tamanho_fonte, cor_fonte, usuario_id))
            else:
                # Criar uma nova configuração para o usuário
                cursor.execute("INSERT INTO configuracoes (usuario_id, tema, fonte, tamanho_fonte, cor_fonte) VALUES (?, ?, ?, ?, ?)",
                               (usuario_id, tema, fonte, tamanho_fonte, cor_fonte))

            # Salvar as alterações no banco de dados
            conn.commit()
            conn.close()

        # Redirecionar para a página de configurações com uma mensagem de sucesso
        return render_template('configuracoes.html', saved=True)

    # Caso contrário, é uma solicitação GET, então exiba a página de configurações
    return render_template('configuracoes.html', saved=False)

@app.route('/graficos')
def graficos():
    # Conectar-se ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Consultar o banco de dados para obter os dados dos gráficos
    cursor.execute("SELECT COUNT(*) FROM candidatos WHERE status = 'Reprovado'")
    candidatos_reprovados = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM candidatos WHERE status = 'Aprovado'")
    candidatos_aprovados = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM candidatos WHERE status = 'Aguardando'")
    candidatos_aguardando = cursor.fetchone()[0]

    # Fechar a conexão com o banco de dados
    conn.close()

    # Dados dos gráficos
    dados_graficos = {
        'categorias': ['Candidatos Reprovados', 'Candidatos Aprovados', 'Aguardando'],
        'valores': [candidatos_reprovados, candidatos_aprovados, candidatos_aguardando]
    }

    return render_template('graficos.html', dados=dados_graficos)

# Rota para lidar com a solicitação das estatísticas
@app.route('/estatisticas', methods=['GET'])
def estatisticas():
    # Obter os parâmetros da solicitação
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    start_admission = request.args.get('start_admission')
    end_admission = request.args.get('end_admission')
    state_quantity = request.args.get('state_quantity')

    # Conectar-se ao banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Consultar o banco de dados para obter as estatísticas filtradas
    query = "SELECT COUNT(*) FROM candidatos WHERE 1=1"
    params = []

    if start_date and end_date:
        query += " AND data_entrevista BETWEEN ? AND ?"
        params.extend([start_date, end_date])

    if start_admission and end_admission:
        query += " AND previsao_admissao BETWEEN ? AND ?"
        params.extend([start_admission, end_admission])

    if state_quantity:
        query += " AND estado = ?"
        params.append(state_quantity)

    cursor.execute(query, tuple(params))
    total_candidatos = cursor.fetchone()[0]

    cursor.execute(query + " AND status = 'Reprovado'", tuple(params))
    candidatos_reprovados = cursor.fetchone()[0]

    cursor.execute(query + " AND status = 'Aprovado'", tuple(params))
    candidatos_aprovados = cursor.fetchone()[0]

    cursor.execute(query + " AND status = 'Aguardando'", tuple(params))
    candidatos_aguardando = cursor.fetchone()[0]

    # Filtrar as datas de admissão no formato YYYY-MM-DD
    filtered_admission_dates = []
    if start_admission and end_admission:
        query_admission_dates = "SELECT previsao_admissao FROM candidatos WHERE previsao_admissao BETWEEN ? AND ?"
        cursor.execute(query_admission_dates, (start_admission, end_admission))
        filtered_admission_dates = [date[0] for date in cursor.fetchall()]

    # Fechar a conexão com o banco de dados
    conn.close()

    # Criar um dicionário com as estatísticas e as datas filtradas
    estatisticas = {
        'total_candidatos': total_candidatos,
        'candidatos_reprovados': candidatos_reprovados,
        'candidatos_aprovados': candidatos_aprovados,
        'candidatos_aguardando': candidatos_aguardando,
        'filtered_admission_dates': filtered_admission_dates
    }

    # Retornar as estatísticas em formato JSON
    return jsonify(estatisticas)

@app.route('/caixa_mensagem')
def caixa_mensagem():
    # Aqui você pode obter as mensagens recebidas do banco de dados ou de outra fonte de dados
    # Em seguida, você pode passar as mensagens para o template da caixa de mensagens

    mensagens = [
        {'remetente': 'Suporte', 'assunto': 'Bem-vindo!', 'conteudo': 'Seja bem-vindo à caixa de mensagens.'},
        {'remetente': 'Suporte', 'assunto': 'Atualização do sistema', 'conteudo': 'Uma nova atualização está disponível.'},
        {'remetente': 'Suporte', 'assunto': 'Promoção especial', 'conteudo': 'Aproveite nossas ofertas exclusivas.'}
    ]

    return render_template('caixa_mensagem.html', mensagens=mensagens)

@app.route('/beneficios')
def beneficios():
    return render_template('beneficios.html')

if __name__ == '__main__':
    app.run(debug=True)
