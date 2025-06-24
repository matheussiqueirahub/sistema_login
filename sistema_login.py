def main():
    USUARIO_CORRETO = "admin"
    SENHA_CORRETA = "1234"
    tentativas_max = 3

    for tentativa in range(1, tentativas_max + 1):
        usuario = input("Nome de usuário: ")
        senha = input("Senha: ")

        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            print(f"Bem-vindo, {usuario}!")
            break
        else:
            tentativas_restantes = tentativas_max - tentativa
            if tentativas_restantes > 0:
                print(f"Credenciais incorretas. Você ainda tem {tentativas_restantes} tentativa(s).")
    else:
        for _ in range(3):
            print("Acesso bloqueado")

if __name__ == "__main__":
    main()