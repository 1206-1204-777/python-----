for i in range(1, 10):
    for j in range(1, 10):
        print("{: >2}".format(i * j), end="")
        if j == 9:
            print()
        else:
            print(end=" | ")

    if i < 9:
        print("=" * (2 * 9 + 3 * (9 - 1)))



