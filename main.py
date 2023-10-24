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
import unittest

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = Game()
        self.assertTrue(1 <= game.secret_number <= 100)
        self.assertEqual(game.attempts, 0)

    def test_guess_lower(self):
        game = Game()
        game.secret_number = 50
        result = game.guess(30)
        self.assertEqual(result, "Загаданное число больше.")

    def test_guess_higher(self):
        game = Game()
        game.secret_number = 50
        result = game.guess(50070)
        self.assertEqual(result, "Загаданное число меньше.")

    def test_guess_correct(self):
        game = Game()
        game.secret_number = 42
        result = game.guess(42)
        self.assertEqual(result, f"Поздравляю! Вы угадали число {game.secret_number} с 1 попытки.")

if __name__ == "__main__":
    unittest.main()
