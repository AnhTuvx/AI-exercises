import os


def read_adj(filename):
    if not os.path.exists(filename):
        print('File does not found')
        return None

    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        adj = []
        for i in range(n):
            Line = list(map(int, f.readline().strip().split()))
            adj.append(Line)
        return n, adj


def read_h(filename):
    if not os.path.exists(filename):
        print('File does not found')
        return None

    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        h = []
        for i in range(n):
            Line = list(map(int, f.readline().strip().split()))
            h.append(Line)
        return h