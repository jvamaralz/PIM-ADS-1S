from controladores import controlador, curso_controlador, relatorio_controlador

def menu_login():
    while True:
        print("\n--- Plataforma PIM educação com Python ---")
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

def menu_principal(usuario):
    usuarios = controlador.carregar_usuarios()
    is_admin = any(u['username'] == usuario and u.get('admin', False) for u in usuarios)

    while True:
        print(f"\n--- Bem-vindo, {usuario} ---")
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

if __name__ == "__main__":
    usuario_logado = menu_login()
    menu_principal(usuario_logado)
