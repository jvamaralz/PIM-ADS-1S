import json
import os
from statistics import mean, median, mode, StatisticsError

DESEMPENHO_FILE = 'modelos/desempenho.json'
CURSOS_FILE = 'data/cursos.json'

def carregar_desempenhos(): # função para carregar o desempenho do usuário no json 
    if not os.path.exists(DESEMPENHO_FILE):
        return []
    with open(DESEMPENHO_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def carregar_cursos(): # carrega os cursos a partir do json, em lista
    if not os.path.exists(CURSOS_FILE):
        return []
    with open(CURSOS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def relatorio_usuario(usuario): # função para gerar um relatório individual de acordo com o usuário de login exibindo cursos que foram feitos, média, moda e mediana dos acertos
    desempenho = carregar_desempenhos()
    cursos = carregar_cursos()
    dados = [d for d in desempenho if d['usuario'] == usuario]

    if not dados:
        print("\nNenhum desempenho registrado.")
        return

    acertos = [d['acertos'] for d in dados]
    print(f"\n--- Relatório de {usuario} ---")
    print(f"Quantidade de cursos feitos: {len(dados)}")
    print(f"Média de acertos: {mean(acertos):.2f}")
    print(f"Mediana de acertos: {median(acertos)}")
    try:
        print(f"Moda de acertos: {mode(acertos)}")
    except StatisticsError:
        print("Moda de acertos: Não há moda (valores únicos)")

    for d in dados:
        nome_curso = next((c['titulo'] for c in cursos if c['id'] == d['curso_id']), "Desconhecido")
        print(f"- {nome_curso}: {d['acertos']} acertos")

def relatorio_geral(): # gera um rel com o desempenho de todos os usuários do json, só usuário admin
    desempenho = carregar_desempenhos()
    cursos = carregar_cursos()

    if not desempenho:
        print("\nNenhum dado disponível.")
        return

    usuarios = set(d['usuario'] for d in desempenho)
    print("\n--- Relatório Geral ---")
    for u in usuarios:
        relatorio_usuario(u)

    print("\n--- Estatísticas Gerais por Curso ---")
    for curso in cursos:
        acertos_curso = [d['acertos'] for d in desempenho if d['curso_id'] == curso['id']]
        if acertos_curso:
            print(f"\nCurso: {curso['titulo']}")
            print(f"- Média de acertos: {mean(acertos_curso):.2f}")
            print(f"- Mediana de acertos: {median(acertos_curso)}")
            try:
                print(f"- Moda de acertos: {mode(acertos_curso)}")
            except StatisticsError:
                print("- Moda de acertos: Não há moda (valores únicos)")
        else:
            print(f"\nCurso: {curso['titulo']} - Sem dados registrados ainda.")
