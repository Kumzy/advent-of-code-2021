previousLine = ''
increased,decreased = 0, 0

with open('input.txt','r') as f:
    for line in f:
        if previousLine:
            if int(line) > int(previousLine):
                increased = increased + 1
            elif int(line) < previousLine:
                decreased = decreased + 1
        previousLine = int(line)

print(f'Increased: {increased} - Decreased: {decreased}')