import sqlite3
import hashlib
import customtkinter as ctk

# Funções de banco de dados
def criar_banco_de_dados():
    """
    Cria o banco de dados e a tabela de usuários, se não existir.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_senha(senha):
    """
    Gera um hash SHA-256 para a senha fornecida.
    """
    return hashlib.sha256(senha.encode()).hexdigest()

def registrar_usuario(usuario, senha):
    """
    Registra um novo usuário no banco de dados com a senha hash.
    """
    if not usuario or not senha:
        return False, "Os campos não podem estar vazios."
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                       (usuario, hash_senha(senha)))
        conn.commit()
        return True, "Usuário registrado!"
    except sqlite3.IntegrityError:
        return False, "Usuário existente."
    finally:
        conn.close()

def fazer_login(usuario, senha):
    """
    Verifica se as credenciais fornecidas são válidas para login.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                   (usuario, hash_senha(senha)))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

def interface_principal():
    """
    Cria a interface gráfica principal para login e registro.
    """
    def registrar():
        """
        Função chamada ao clicar no botão 'Registrar'. Registra um novo usuário.
        """
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        sucesso, mensagem = registrar_usuario(usuario, senha)
        label_mensagem.configure(text=mensagem)

    def login():
        """
        Função chamada ao clicar no botão 'Entrar'. Faz login com o usuário fornecido.
        """
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if fazer_login(usuario, senha):
            label_mensagem.configure(text="Usuário logado com sucesso!")
        else:
            label_mensagem.configure(text="Login falhou!")

    def alternar_visibilidade_senha():
        """
        Alterna a visibilidade da senha no campo de entrada.
        """
        global senha_visivel
        if senha_visivel:
            entry_senha.configure(show='*')  # Oculta a senha
            botao_mostrar_senha.configure(text="Mostrar Senha")
        else:
            entry_senha.configure(show='')  # Exibe a senha
            botao_mostrar_senha.configure(text="Ocultar Senha")
        senha_visivel = not senha_visivel

    # Configuração da janela principal
    janela = ctk.CTk()
    janela.title("Sistema de Login")
    janela.geometry("400x300")

    # Configura o modo de aparência e tema
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Adiciona elementos na interface
    ctk.CTkLabel(janela, text="Login").pack(pady=10)

    entry_usuario = ctk.CTkEntry(janela, placeholder_text="Usuário")
    entry_usuario.pack(pady=5)

    ctk.CTkLabel(janela, text="Senha").pack(pady=10)

    frame_senha = ctk.CTkFrame(janela)
    frame_senha.pack(pady=5)

    entry_senha = ctk.CTkEntry(frame_senha, placeholder_text="Senha", show='*')
    entry_senha.pack(side="left", padx=(0, 10))

    botao_mostrar_senha = ctk.CTkButton(frame_senha, text="Mostrar Senha", command=alternar_visibilidade_senha)
    botao_mostrar_senha.pack(side="left")

    frame_botoes = ctk.CTkFrame(janela)
    frame_botoes.pack(pady=20)

    ctk.CTkButton(frame_botoes, text="Registrar", command=registrar).pack(side="left", padx=10)
    ctk.CTkButton(frame_botoes, text="Entrar", command=login).pack(side="right", padx=10)

    label_mensagem = ctk.CTkLabel(janela, text="")
    label_mensagem.pack(pady=10)

    global senha_visivel
    senha_visivel = False  # Estado inicial da visibilidade da senha

    # Inicia o loop principal da interface
    janela.mainloop()

# Inicializa o banco de dados
criar_banco_de_dados()

# Inicia a interface gráfica
interface_principal()
