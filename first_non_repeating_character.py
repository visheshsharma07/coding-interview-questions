s = "adddettssa" # Pass the test string
rep = []
dist = []
for letter in s:
    if letter in dist:
        dist.remove(letter)
        rep.append(letter)
    elif letter in rep:
        continue
    else:
        dist.append(letter)
if len(dist) > 0:
    print(dist[0])
else:
    print('There is no repeating character')