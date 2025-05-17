import json
import os


USERS_FILE = 'modelos/usuarios.json'

def carregar_usuarios(): # carregando o usuário do json, retornando uma lista de usuários
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_usuarios(usuarios): # salva o usuário na lista em json, formatodos com indentação 
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario(): # realiaza o cadatro de um novo usuário 
    usuarios = carregar_usuarios()
    username = input("Escolha um nome de usuário: ")
    if any(u['username'] == username for u in usuarios): # verifica se o usuário já existe 
        print("Usuário já existe.")
        return
    senha = input("Escolha uma senha: ")
    idade = input("Qual sua idade: ")
    usuarios.append({"username": username, "senha": senha,"idade": idade, "admin": False})
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def login_usuario(): # realiza o login do usuário 
    usuarios = carregar_usuarios()
    username = input("Nome de usuário: ")
    senha = input("Senha: ")
    for i in usuarios:
        if i['username'] == username and i['senha'] == senha: # verificando se o usuário e senha para acessar
            print(f"Bem-vindo, {username}!")
            i['logins'] = i.get('logins', 0) + 1 #adicionando um login ao usuário 
            salvar_usuarios(usuarios)
            return username
    print("Usuário ou senha inválidos.")
    return None

