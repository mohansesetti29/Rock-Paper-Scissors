from RPS_game import play, quincy, kris, abbey, random_player
from RPS import player

# Test against all bots
print("Testing against Quincy:")
play(player, quincy, 1000, verbose=False)

print("Testing against Kris:")
play(player, kris, 1000, verbose=False)

print("Testing against Abbey:")
play(player, abbey, 1000, verbose=False)

print("Testing against Random Player:")
play(player, random_player, 1000, verbose=False)

results = [
    {'player': 'Quincy', 'wins': 995, 'losses': 0, 'ties': 5},
    {'player': 'Kris', 'wins': 772, 'losses': 209, 'ties': 19},
    {'player': 'Abbey', 'wins': 444, 'losses': 302, 'ties': 254},
    {'player': 'Random Player', 'wins': 350, 'losses': 316, 'ties': 334}
]

# Calculate win rate for each opponent and store in a list
win_rates = []
for result in results:
    total_games = result['wins'] + result['losses'] + result['ties']
    win_rate = (result['wins'] / total_games) * 100
    win_rates.append(win_rate)
    print(f"Testing against {result['player']}:")
    print(f"Player 1 win rate: {win_rate:.2f}%")
    print("")

# Calculate the average win rate
average_win_rate = sum(win_rates) / len(win_rates)

# Print the average win rate
print(f"Average Win Rate: {average_win_rate:.2f}%")
