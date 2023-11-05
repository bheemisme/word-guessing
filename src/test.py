with open("./words.txt", "r") as f:
    line= f.readline()
    print(line.split("=")[-1].strip())