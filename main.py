from game import SpadesScoreKeeper

spades = SpadesScoreKeeper()
done = False

print("Welcome to your very own SPADES SCORE TRACKER!")

team1_name = input("Enter team 1 name:\n")
team2_name = input("Enter team 2 name:\n")

while not done:
    spades.game(team1_name, team2_name)
    done = spades.done()

spades.finish(team1_name, team2_name)
# this is a test added line