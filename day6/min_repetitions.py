def min_repetitions(a, b):
    rep = (len(b) - 1) // len(a) + 1
    for i in range(2):
        if b in a*(rep+i):
            return rep+i
    return -1
if __name__ == "__main__":
    s1 = "abc"
    s2 = "cabcabca"
    print(min_repetitions(s1, s2))