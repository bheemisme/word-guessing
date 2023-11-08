with open('data/history.txt', 'r') as f:
    l = f.readlines()
    if len(l) > 0:
        print(int(l[-1].split(";")[0]))
