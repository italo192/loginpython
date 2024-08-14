# Sistema de Login com Python e CustomTkinter

Este projeto é um sistema de login simples desenvolvido em Python utilizando a biblioteca `customtkinter` para a interface gráfica e `sqlite3` para gerenciamento de banco de dados. O sistema permite registrar novos usuários e fazer login com credenciais previamente registradas.

## Funcionalidades

- **Criação e Gerenciamento do Banco de Dados**: Cria um banco de dados SQLite com uma tabela de usuários, se não existir.
- **Registro de Usuários**: Permite o registro de novos usuários com senhas armazenadas de forma segura usando hash SHA-256.
- **Login de Usuários**: Permite aos usuários fazer login com suas credenciais.
- **Interface Gráfica**: Utiliza `customtkinter` para uma interface gráfica moderna e intuitiva, incluindo funcionalidades para mostrar e ocultar a senha.

## Dependências

- `customtkinter` - Para a criação da interface gráfica.
- `sqlite3` - Para gerenciamento do banco de dados SQLite.
- `hashlib` - Para a geração do hash das senhas.

Você pode instalar as dependências necessárias com:

```bash
pip install customtkinter
