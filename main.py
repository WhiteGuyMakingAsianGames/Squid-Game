import random

class Player:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Player {self.number}"

def simulate_game(num_players):
    players = [Player(i) for i in range(1, num_players + 1)]
    while len(players) > 1:
        eliminated = random.choice(players)
        players.remove(eliminated)
        print(f"{eliminated} has been eliminated.")
    print(f"{players[0]} is the winner!")

if __name__ == "__main__":
    num_players = 456
    simulate_game(num_players)
