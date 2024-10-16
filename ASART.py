from types import LambdaType

from utils.readfile import read_adj, read_h


def checkin(list, point):
    for i in range(len(list)):
        if list[i] == point:
            return True
    return False


def ASART(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    Parent = [-1] * len(adj)
    g = [float('inf')] * len(adj)
    f = [float('inf')] * len(adj)
    OPEN.append(start)
    g[start] = 0
    f[start] = h[start][1]

    while len(OPEN) > 0:  # OPEN con dinh de xet
        current = OPEN.pop(0)  # Lay ra dau OPEN 1 dinh
        print(f"curr: {current}")
        CLOSE.append(current)
        Tn = []  # clear Tn
        if current == stop:
            print("Goal reach!")
            # in ra duong di tu Stop - Start
            path = []
            idx = stop
            while idx != -1:
                path.append(idx)
                idx = Parent[idx]

            path.reverse()
            print(path)
            return

        # nguoc lai thi xet cac dinh ke
        for neighbor in range(len(adj)):
            if adj[current][neighbor] != 0:
                if checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == False:
                    Tn.append(neighbor)
                    g[neighbor] = g[current] + adj[current][neighbor]
                    f[neighbor] = g[current] + h[neighbor][1]
                    Parent[neighbor] = current

                    g_new = g[current] + adj[current][neighbor]
                    f_new = g_new + h[neighbor][1]
                    print(f"g_new({neighbor}):{g_new} , fnew = ({neighbor}):{f_new} ")

                    if f_new < g[current]:
                        g[current] = f_new
                        f[current] = f_new
                        print(f"cap nhat gia tri f({neighbor}), g({neighbor})  ")
                        Parent[neighbor] = current
        print(f"Tn:{Tn}")
        OPEN = Tn + OPEN
        print(f"OPEN:{OPEN}")

        OPEN_sorted = sorted(OPEN, key=lambda x:f[x],reverse=False)
        OPEN = OPEN_sorted
        print(f"OPEN_sorted:{OPEN}")
        print(f"g:{g}")
        print(f"g:{f}")
        print(f"Parent:{Parent}")
        Tn =[]
    print(f"khong tim thay duong di ")

if __name__ == '__main__':
    n, adj = read_adj('input/CMS.adj')
    h = read_h('input/CMS.h')

    print(f"Number of nodes: {n}")
    print(f"Heutistic: ")
    print(f"Adjacency list: ")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")

    ASART(adj, 0, 6)
