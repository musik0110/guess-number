import random

class Game:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1
        if number < self.secret_number:
            return "Загаданное число больше."
        elif number > self.secret_number:
            return "Загаданное число меньше."
        else:
            return f"Поздравляю! Вы угадали число {self.secret_number} с {self.attempts} попытки."

def main():
    game = Game()

    while True:
        try:
            guess = int(input("Угодайте число от 1 до 100: "))
            result = game.guess(guess)
            print(result)
            if guess == game.secret_number:
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
