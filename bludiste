bludiste = [["_", "_", "X", "X", "_"], ["X", "_", "X", "_", "_"], ["_", "_", "_", "_", "X"], ["_", "X", "_", "_", "X"], ["_", "X", "X", "_", "X"], ["X", "_", "X", "_", "_"]]
x = 0
y = 0
end_x = len(bludiste)-1
end_y = len(bludiste[0])-1
bludiste[x][y] = "❤"
kolo = 1
print("❤ je tvoje pozice")
print(bludiste[0])
print(bludiste[1])
print(bludiste[2])
print(bludiste[3])
print(bludiste[4])
print(bludiste[5])

while x < end_x and y < end_y:
    if bludiste[x+1][y] == "_":
        bludiste[x][y] = "_"
        x = x + 1
    elif bludiste [x][y+1] == "_":
        bludiste[x][y] = "_"
        y = y + 1

    bludiste[x][y] = "❤"
    print('právě probíhá: ' + str(kolo) + 'kolo')
    print(bludiste[0])
    print(bludiste[1])
    print(bludiste[2])
    print(bludiste[3])
    print(bludiste[4])
    print(bludiste[5])
    kolo = kolo + 1
    print(str(x), str(y))

