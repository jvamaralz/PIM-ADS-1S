import time
import json

inicio = time.time() # váriável que vai calcular o tempo de exdecução do programa. 

from controladores import controlador, curso_controlador, relatorio_controlador # importando os arquivos necessários.

def menu_login(): # exibe o menu inicial de login
    while True:
        print("\n••• Plataforma PIM educação com Python •••")
        print("1. Login")
        print("2. Cadastrar novo usuário")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            usuario = controlador.login_usuario()
            if usuario:
                return usuario
        elif opcao == '2':
            controlador.cadastrar_usuario()
            input("Pressione Enter para voltar ao menu...")
        elif opcao == '3':
            print("Adios...")
            exit()
        else:
            print("Opção inválida.")

def menu_principal(usuario): # exibe e o menu principal após o login para acesso aos cursos e relatório.
    usuarios = controlador.carregar_usuarios()
    is_admin = any(u['username'] == usuario and u.get('admin', False) for u in usuarios)

    while True:
        print(f"\n••• Bem-vindo, {usuario} •••")
        print("1. Acessar Cursos")
        print("2. Ver meu Relatório")
        if is_admin:
            print("3. Ver Relatório Geral")
            print("4. Sair")
        else:
            print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            curso_controlador.exibir_cursos(usuario)
        elif opcao == '2':
            relatorio_controlador.relatorio_usuario(usuario)
        elif opcao == '3' and is_admin:
            relatorio_controlador.relatorio_geral()
        elif (opcao == '3' and not is_admin) or (opcao == '4' and is_admin):
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__": # inicia a aplicação.
    usuario_logado = menu_login()
    inicio = time.time() # váriável que vai calcular o tempo de exdecução do programa. 
    menu_principal(usuario_logado)
    fim = time.time()
    tempo_execucao = fim - inicio # gravando o tempo de execução

    print(f"O tempo de execução foi de exatamente: {tempo_execucao:.4f} ")
    
    usuarios = controlador.carregar_usuarios()# Atualizar tempo de execução do usuário
    for u in usuarios:
        if u['username'] == usuario_logado:
            u['tempo_total_execucao'] = u.get('tempo_total_execucao', 0) + tempo_execucao
            break
    controlador.salvar_usuarios(usuarios)
    
with open('modelos/usuarios.json', 'r', encoding='utf-8') as f:
    usuarios = json.load(f)

for usuario in usuarios: # incrementando o tmepo de execução ao json, para o relatório
    if usuario['username'] == usuario_logado:
        if 'tempo_total_execucao' not in usuario:
            usuario['tempo_total_execucao'] = 0
        usuario['tempo_total_execucao'] += tempo_execucao
        break

with open('modelos/usuarios.json', 'w', encoding='utf-8') as f:
    json.dump(usuarios, f, indent=4)