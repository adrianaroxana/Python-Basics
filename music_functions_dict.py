
SongDetails = {"Genre": "Rap", "Artist": "El Nino", "Year": 2015}


def GuessKey(Details):
    while True:
        x = random.choice(list(Details))
        print(x)
        y = input("Guess the value: ")
        if y == str(Details[x]):
            return True
        else:
            return False


x = GuessKey(SongDetails)
print(x)
