import json
import os

CURSOS_FILE = 'data/cursos.json'
DESEMPENHO_FILE = 'modelos/desempenho.json'

def carregar_cursos():
    if not os.path.exists(CURSOS_FILE):
        return []
    with open(CURSOS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_desempenho(usuario, curso_id, acertos):
    if not os.path.exists(DESEMPENHO_FILE):
        desempenho = []
    else:
        with open(DESEMPENHO_FILE, 'r', encoding='utf-8') as f:
            desempenho = json.load(f)
    desempenho.append({"usuario": usuario, "curso_id": curso_id, "acertos": acertos})
    with open(DESEMPENHO_FILE, 'w', encoding='utf-8') as f:
        json.dump(desempenho, f, indent=4)

def exibir_cursos(usuario):
    cursos = carregar_cursos()
    print("\n--- Cursos Disponíveis ---")
    for curso in cursos:
        print(f"{curso['id']}. {curso['titulo']}")
    escolha = input("Escolha o ID do curso para iniciar (ou 'sair' para voltar): ")
    if escolha.lower() == 'sair':
        return
    for curso in cursos:
        if str(curso['id']) == escolha:
            executar_curso(usuario, curso)
            return
    print("Curso não encontrado.")

def executar_curso(usuario, curso):
    print(f"\n--- {curso['titulo']} ---")
    print(curso['conteudo'])
    input("\nPressione Enter para iniciar o quiz...")
    acertos = 0
    for i, pergunta in enumerate(curso['perguntas'], 1):
        print(f"\nPergunta {i}: {pergunta['pergunta']}")
        for idx, alt in enumerate(pergunta['alternativas']):
            print(f"{idx}. {alt}")
        try:
            resposta = int(input("Escolha a alternativa correta: "))
            if resposta == pergunta['resposta_correta']:
                print("✅ Correto!")
                acertos += 1
            else:
                print("❌ Incorreto.")
        except ValueError:
            print("Entrada inválida. Pulando a pergunta.")
    print(f"\nVocê acertou {acertos} de {len(curso['perguntas'])} perguntas.")
    salvar_desempenho(usuario, curso['id'], acertos)
