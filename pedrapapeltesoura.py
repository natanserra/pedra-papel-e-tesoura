import random

def escolha_computador():
    """Escolhe aleatoriamente entre pedra, papel ou tesoura."""
    escolhas = ['pedra', 'papel', 'tesoura']
    return random.choice(escolhas)

def determinar_vencedor(usuario, computador):
    """Determina o vencedor com base nas regras do Jokenpô."""
    if usuario == computador:
        return "Empate!"
    elif (usuario == 'pedra' and computador == 'tesoura') or \
         (usuario == 'papel' and computador == 'pedra') or \
         (usuario == 'tesoura' and computador == 'papel'):
        return "Você venceu!"
    else:
        return "Computador venceu!"

def main():
    """Função principal para executar o jogo Jokenpô."""
    print("Bem-vindo ao Jokenpô!")
    
    while True:
        usuario = input("Escolha: pedra, papel ou tesoura (ou 'sair' para encerrar): ").strip().lower()
        
  
        if usuario == 'sair':
            print("Obrigado por jogar! Até a próxima.")
            break


        if usuario not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida! Por favor, escolha entre pedra, papel ou tesoura.")
            continue
        
      
        computador = escolha_computador()
        print(f"Computador escolheu: {computador}")
        

        resultado = determinar_vencedor(usuario, computador)
        print(resultado)

if __name__ == "__main__":
    main()
