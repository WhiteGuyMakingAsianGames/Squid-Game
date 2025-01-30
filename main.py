import random
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Player:
    """
    Represents a player in the game with a unique number.
    """
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Player {self.number}"

def simulate_red_light_green_light(num_players, move_probability=0.5, wait_time=4):
    """
    Simulates the Red Light, Green Light game.

    :param num_players: Total number of players.
    :param move_probability: Probability that a player moves during Red Light.
    :param wait_time: Time to wait between phases in seconds.
    """
    players = [Player(i) for i in range(1, num_players + 1)]
    
    while len(players) > 1:
        logging.info("Red Light!")
        eliminated_players = [player for player in players if random.random() < move_probability]
        
        for eliminated in eliminated_players:
            players.remove(eliminated)
            logging.info(f"{eliminated} has been eliminated.")
        
        logging.info("Green Light!")
        time.sleep(wait_time)  # Wait for the specified time before the next round
    
    logging.info(f"{players[0]} is the winner!")

if __name__ == "__main__":
    num_players = 456
    simulate_red_light_green_light(num_players)
