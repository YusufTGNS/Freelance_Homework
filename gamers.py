# Definition of the "Gamer" class
# Task 2. Add the nickname field
# Task 3. Add the email field
class Gamer:
    def __init__(self, name, age, nickname, email):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.email = email
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    # Task 4: Change the message
    def introduce(self):
        print(f"Merhaba benim adım: {self.name}, Takma Adım: {self.nickname}, Yaşım: {self.age}, E-POSTA: {self.email}")


# Creating an instance of the "Gamer" class
gamer1 = Gamer("John", 14, "JohnForever", "john@gmail.com")

# Adding games
gamer1.add_game("Minecraft")
gamer1.add_game("Dota 2")
gamer1.add_game("Counter-Strike 2")
gamer1.add_game("League of Legends")

# A gamer's mini-presentation
gamer1.introduce()

# Outputting favourite games
print(f"{gamer1.name} Şu oyunlardan hoşlanıyor: {', '.join(gamer1.games)}")
