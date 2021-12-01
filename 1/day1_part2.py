previousWindow = 0
increased,decreased = 0, 0
windowSize = 3

with open('input.txt','r') as f:
    lines = list(map(int, map(str.strip, f.readlines())))
    for i in range(1, len(lines) - (windowSize - 1)):
        window_previous = sum(lines[previousWindow:previousWindow + windowSize])
        window_current = sum(lines[i:i + windowSize])
        if window_previous < window_current:
            increased += 1
        elif window_previous > window_current:
            decreased += 1
        previousWindow = i

print(f'Increased: {increased} - Decreased: {decreased}')