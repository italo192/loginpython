Sistema de Login com Python e CustomTkinter
Este projeto é um sistema de login simples desenvolvido em Python utilizando a biblioteca customtkinter para a interface gráfica e sqlite3 para gerenciamento de banco de dados. O sistema permite registrar novos usuários e fazer login com credenciais previamente registradas.

Funcionalidades
Criação e Gerenciamento do Banco de Dados: Cria um banco de dados SQLite com uma tabela de usuários, se não existir.
Registro de Usuários: Permite o registro de novos usuários com senhas armazenadas de forma segura usando hash SHA-256.
Login de Usuários: Permite aos usuários fazer login com suas credenciais.
Interface Gráfica: Utiliza customtkinter para uma interface gráfica moderna e intuitiva, incluindo funcionalidades para mostrar e ocultar a senha.
Dependências
customtkinter - Para a criação da interface gráfica.
sqlite3 - Para gerenciamento do banco de dados SQLite.
hashlib - Para a geração do hash das senhas.
Você pode instalar as dependências necessárias com:

bash
Copiar código
pip install customtkinter
Como Executar
Inicialize o Banco de Dados: O banco de dados será criado automaticamente ao executar o script, se ainda não existir.

Execute o Script:

Execute o script principal login_system.py para iniciar a interface gráfica.

bash
Copiar código
python login_system.py
Funcionalidades da Interface
Registrar: Registra um novo usuário com o nome de usuário e senha fornecidos. Se o usuário já existir, uma mensagem de erro será exibida.
Entrar: Faz login com as credenciais fornecidas. Se o login for bem-sucedido, uma mensagem de sucesso será exibida; caso contrário, uma mensagem de erro será mostrada.
Mostrar/Ocultar Senha: Alterna a visibilidade da senha no campo de entrada.
Código
O código é dividido em duas partes principais:

Funções de Banco de Dados: Funções para criar o banco de dados, registrar usuários e verificar credenciais de login.
Interface Gráfica: Configuração e criação da interface gráfica usando customtkinter.
