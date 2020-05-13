import sys


command_map = {}
def insert(output):
    with open("tmp.out", "r+b") as f:
        tmp = f.readline()
        c = list(tmp)
        print(c)
        ind = c.index(187)+1
        c[ind] = 34
        #after 16, 0,0
        c.insert(ind+4, 0)
        c.insert(ind+4, 0)
        c.insert(ind+4, 0) 
        c.insert(ind+4, 89)
        c.insert(ind+4, 187)
        print(c)
        c = bytes(c)
        # tmp = str(tmp)
        # tmp = tmp.replace('xbb\\x05', 'xbb\\x08')
        # c = bytes(tmp, encoding='bytes')
        # c = c[2:-2]

    with open(f"{output}.out", "w+b") as f:
        f.write(c)
        # reading
        # data = f.readline().hex()
        # data = ["".join(data[i:i+4]) for i in range(0, len(data), 4)]
        # data = [" ".join(data[i:i+8]) for i in range(0, len(data), 8)]
        # print("\n".join(data))
        # f.seek()
def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    insert(filename)
#chmod +x b.out 
#./hello.out ; echo $?
if __name__ == '__main__':
   main()
