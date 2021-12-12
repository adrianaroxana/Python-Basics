a = [5, 1, "a", "A", 2]


def sort_set(playerset):
    playerset = list(
        map(int, filter(lambda x: x.isdigit(), sorted(map(str, playerset))))
    ) + list(filter(lambda x: x.isalpha(), sorted(map(str, playerset))))
    return playerset


def check_pairs(playerset):
    pairs = 0
    try:
        for i in range(len(playerset)):
            if playerset[i] == playerset[i + 1] == playerset[i + 2] == playerset[i + 3]:
                pairs += 1
                playerset.remove(playerset[i])
                playerset.remove(playerset[i + 1])
                playerset.remove(playerset[i + 2])
                playerset.remove(playerset[i + 3])
    except Exception:
        return pairs
