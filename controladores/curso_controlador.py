import json
import os

CURSOS_FILE = 'data/cursos.json'
DESEMPENHO_FILE = 'modelos/desempenho.json'

def carregar_cursos(): # função para carregar o curso no caminho de dados usando json
    if not os.path.exists(CURSOS_FILE):
        return []
    with open(CURSOS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_desempenho(usuario, curso_id, acertos): # salvas os desempenhos de acordo com os acertos usando json e cravando em modelos
    if not os.path.exists(DESEMPENHO_FILE):
        desempenho = []
    else:
        with open(DESEMPENHO_FILE, 'r', encoding='utf-8') as f:
            desempenho = json.load(f)
    desempenho.append({"usuario": usuario, "curso_id": curso_id, "acertos": acertos})
    with open(DESEMPENHO_FILE, 'w', encoding='utf-8') as f:
        json.dump(desempenho, f, indent=4)

def exibir_cursos(usuario): # função para mostrar o curso em tela quando selecionado 
    cursos = carregar_cursos()
    print("\n••• Cursos Disponíveis •••")
    for curso in cursos:
        print(f"{curso['id']}. {curso['titulo']}")
    escolha = input("Escolha o curso para iniciar (ou 'sair' para voltar): ")
    if escolha.lower() == 'sair':
        return
    for curso in cursos:
        if str(curso['id']) == escolha:
            executar_curso(usuario, curso)
            return
    print("Curso não encontrado.")

def executar_curso(usuario, curso): # função para puxar as perguntas dos cursos selecionado
    print(f"\n••• {curso['titulo']} •••")
    print(curso['conteudo'])
    input("\nPressione Enter para iniciar a provinha. ")
    acertos = 0
    for i, pergunta in enumerate(curso['perguntas'], 1):
        print(f"\nPergunta {i}: {pergunta['pergunta']}")
        for i, alt in enumerate(pergunta['alternativas']):
            print(f"{i}. {alt}")
        try:
            resposta = int(input("Escolha a alternativa correta: "))
            if resposta == pergunta['resposta_correta']: #usando o json salvo com a resposta correta para validação
                print("Correto!")
                acertos += 1
            else:
                print("Incorreto.")
        except ValueError:
            print("Opção invália. Vamos pular essa!")
    print(f"\nVocê acertou {acertos} de {len(curso['perguntas'])} perguntas.")
    salvar_desempenho(usuario, curso['id'], acertos) # chamando a função e salvando em json 
