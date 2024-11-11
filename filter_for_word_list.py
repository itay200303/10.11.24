
# 2.
games = ["Fortnite", "Grand Theft Auto V", "The Elder Scrolls V:Skyrim", "Dark Souls", "Overwatch"]

# a.
print("only games that bigger than 8: ", list(filter(lambda game: len(game) > 8,games)))

# b.
print("only games that start with the letter "F": ", list(filter(lambda game: game.startswith("F") , games)))

# c.
print("only games that contains two word: ", list(filter(lambda game: len(game.split()) == 2 , games)))

# d.
print("only games with the letter 'V': ", list(filter(lambda game: "V" in game , games)))
