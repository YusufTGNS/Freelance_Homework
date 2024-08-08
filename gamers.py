# Definition of the "Gamer" class
# Task 2. Add the nickname field
# Task 3. Add the email field
class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age

        self.games = []

    def add_game(self, game):
        self.games.append(game)

    # Task 4: Change the message
    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")


# Creating an instance of the "Gamer" class
gamer1 = Gamer("John", 14, "JohnForever", "john@gmail.com")

# Adding games
gamer1.add_game("Minecraft")
gamer1.add_game("Dota 2")

# A gamer's mini-presentation
gamer1.introduce()

# Outputting favourite games
print(f"{gamer1.name} enjoys these games: {', '.join(gamer1.games)}")
