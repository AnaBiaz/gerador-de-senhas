import random
import string

# Lista para armazenar as senhas geradas
senhas_salvas = []

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = []

    for _ in range(tamanho):
        senha.append(random.choice(caracteres))

    senha_gerada = ''.join(senha)
    return senha_gerada

def salvar_senha(senha):
    senhas_salvas.append(senha)
    print("Senha gerada e salva com sucesso!")

def mostrar_senhas():
    if not senhas_salvas:
        print("Nenhuma senha salva ainda.")
    else:
        print("\nSenhas salvas:")
        for idx, senha in enumerate(senhas_salvas, start=1):
            print(f"{idx}. {senha}")
        print()

def apagar_senhas():
    senhas_salvas.clear()
    print("Todas as senhas foram apagadas.")

def main():
    while True:
        print("\n== Gerador de Senhas ==")
        print("1. Gerar nova senha")
        print("2. Mostrar senhas salvas")
        print("3. Apagar senhas salvas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tamanho = int(input("Quantos caracteres a senha deve ter? "))
            senha = gerar_senha(tamanho)
            salvar_senha(senha)
        elif opcao == "2":
            mostrar_senhas()
        elif opcao == "3":
            apagar_senhas()
        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
