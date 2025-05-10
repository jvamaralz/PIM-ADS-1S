import json
import os

USERS_FILE = 'modelos/usuarios.json'

def carregar_usuarios():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    username = input("Escolha um nome de usuário: ")
    if any(u['username'] == username for u in usuarios):
        print("Usuário já existe.")
        return
    senha = input("Escolha uma senha: ")
    usuarios.append({"username": username, "senha": senha, "admin": False})
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def login_usuario():
    usuarios = carregar_usuarios()
    username = input("Nome de usuário: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u['username'] == username and u['senha'] == senha:
            print(f"Bem-vindo, {username}!")
            return username
    print("Usuário ou senha inválidos.")
    return None
