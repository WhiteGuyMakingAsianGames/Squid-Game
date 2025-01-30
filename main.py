import random
import time

class Player:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Player {self.number}"

def simulate_red_light_green_light(num_players):
    players = [Player(i) for i in range(1, num_players + 1)]
    while len(players) > 1:
        print("Red Light!")
        eliminated_players = []
        for player in players:
            # Randomly decide if a player moves during Red Light
            if random.random() < 0.5:
                eliminated_players.append(player)
        for eliminated in eliminated_players:
            players.remove(eliminated)
            print(f"{eliminated} has been eliminated.")
        print("Green Light!")
        time.sleep(0.5)  # Wait for 0.5 seconds before the next round
    print(f"{players[0]} is the winner!")

if __name__ == "__main__":
    num_players = 456
    simulate_red_light_green_light(num_players)
