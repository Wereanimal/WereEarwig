with open("b.out", "r+b") as f:
    tmp = f.readline()
    c = list(tmp)
    c[c.index(187)+1] = 74
    c = bytes(c)
    # tmp = str(tmp)
    # tmp = tmp.replace('xbb\\x05', 'xbb\\x08')
    # c = bytes(tmp, encoding='bytes')
    # c = c[2:-2]

with open("b.out", "w+b") as f:
    f.write(c)
    # reading
    # data = f.readline().hex()
    # data = ["".join(data[i:i+4]) for i in range(0, len(data), 4)]
    # data = [" ".join(data[i:i+8]) for i in range(0, len(data), 8)]
    # print("\n".join(data))
    # f.seek()