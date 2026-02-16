import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_alunos_arquivo(nome_arquivo):
    """Lê nomes de um arquivo .txt, um por linha."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            # Captura linhas não vazias e remove espaços extras
            return [linha.strip() for linha in f.readlines() if linha.strip()]
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

def salvar_resultado(grupos):
    """Salva os grupos sorteados em um arquivo de texto."""
    with open('resultado_sorteio.txt', 'w', encoding='utf-8') as f:
        f.write("--- RESULTADO DO SORTEIO ---\n\n")
        for i, grupo in enumerate(grupos, 1):
            f.write(f"Grupo {i:02d}: {', '.join(grupo)}\n")
    print("\n💾 Resultado exportado com sucesso para 'resultado_sorteio.txt'!")

def sortear_grupos(alunos, tamanho_grupo):
    random.shuffle(alunos)
    return [alunos[i:i + tamanho_grupo] for i in range(0, len(alunos), tamanho_grupo)]

def menu():
    limpar_tela()
    print("--- 🎓 SORTEADOR PRO (PROF. MARCIO HERNANI) ---")
    print("1. Inserir nomes manualmente (separados por vírgula)")
    print("2. Carregar nomes de arquivo (alunos.txt)")
    
    opcao = input("\nEscolha uma opção: ")
    lista_alunos = []

    if opcao == '1':
        entrada = input("Nomes: ")
        lista_alunos = [n.strip() for n in entrada.split(',') if n.strip()]
    elif opcao == '2':
        # Cria um arquivo de exemplo se não existir para o usuário testar
        if not os.path.exists('alunos.txt'):
            with open('alunos.txt', 'w', encoding='utf-8') as f:
                f.write("João\nMaria\nPedro\nAna")
        lista_alunos = carregar_alunos_arquivo('alunos.txt')
    
    if not lista_alunos: return

    try:
        print(f"\nTotal de alunos: {len(lista_alunos)}")
        tamanho = int(input("Quantidade de pessoas por grupo: "))
        
        grupos = sortear_grupos(lista_alunos, tamanho)

        print("\n--- GRUPOS SORTEADOS ---")
        for i, g in enumerate(grupos, 1):
            print(f"Grupo {i:02d}: {', '.join(g)}")

        confirmar = input("\nDeseja salvar o resultado em .txt? (s/n): ").lower()
        if confirmar == 's':
            salvar_resultado(grupos)

    except ValueError:
        print("❌ Erro: Insira um número válido.")

if __name__ == "__main__":
    menu()