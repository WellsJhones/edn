def senha_forte(senha):
    # Verifica se tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    # Verifica se contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    return True

def verificar_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break

        if senha_forte(senha):
            print("Senha forte registrada com sucesso!")
            break
        else:
            print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")

# Executa o programa
verificar_senha()
