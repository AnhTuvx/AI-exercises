import os

def readfile(filename):
    filename = os.getcwd() + '\\input\\' + filename
    print(filename)
    if not os.path.isfile(filename):
        print("file is not found")
        return None
    
    with open(filename, "r") as f:
        n = int(f.readline().strip())
        adj = []
        for idx in range(n):
            line = list(map(int, f.readline().strip().split()))
            adj.append(line)
        return n, adj
    # networkx, matplot