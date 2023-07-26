import random

def number_guessing_game():
    print("Bienvenue dans le jeu de devinette de nombre !")
    print("L'ordinateur a choisi un nombre entre 1 et 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Devinez le nombre : "))
            attempts += 1

            if guess < secret_number:
                print("Trop petit ! Essayez encore.")
            elif guess > secret_number:
                print("Trop grand ! Essayez encore.")
            else:
                print(f"Bravo ! Vous avez deviné le nombre en {attempts} tentatives.")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    number_guessing_game()
