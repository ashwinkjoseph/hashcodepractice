with open("output.txt") as o:
    score = 0
    for line in o:
        score = score + int(line.rstrip('\n').lstrip('\n').split(' ')[0])
    print("final score: ", score)