from types import LambdaType

from utils.readfile import read_adj, read_h


def checkin(list, point):
    for i in range(len(list)):
        if list[i] == point:
            return True
    return False


def Cms(adj, start, stop):
    # Khoi tao cac gia tri
    OPEN = []  # tap cac dinh tiem nang
    CLOSE = []  # tap cac dinh da xet
    Tn = []  # tap cac dinh ke cua dinh dang xet
    Parent = [-1] * len(adj)  # khoi tao parent = -1 -1 .... n
    g = [float ('inf')] * len(adj)
    OPEN.append(start)
    g[start] = h[start][1] #hoac =0
    curr = start
    OPEN.append(curr)  # chen start vao cuoi OPEN

    while len(OPEN) > 0:  # OPEN con dinh de xet
        curr = OPEN.pop(0)  # Lay ra dau OPEN 1 dinh
        print(f"curr: {curr}")
        CLOSE.append(curr)
        Tn = []  # clear Tn
        if curr == stop:
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
        for neighbor in range(n):
            if adj[curr][neighbor] == 1 and checkin(CLOSE, neighbor) == False:
                if checkin(OPEN, neighbor) == False:
                    Tn.append(neighbor)
                    g[neighbor] = g[curr] + h[neighbor][1]
                    Parent[neighbor] = curr
                else:
                    g_tam = g[curr] + h[neighbor][1]
                    if g_tam  < g[neighbor]:
                        g[neighbor] = g_tam
                        Parent[neighbor] = curr
        print(f"Parent: {Parent}")
        print(f"Tn: {Tn}")


        OPEN = Tn + OPEN
        print(f"OPEN: {OPEN}")

        OPEN_sorted = sorted(OPEN, key=lambda x: g[x], reverse=False )
        OPEN = OPEN_sorted
        print(f"OPEN sorted: {OPEN}")
        print(f"g: {g}")

        Tn = []

    print("Goal Unreach!")


if __name__ == '__main__':
    n, adj = read_adj('input/CMS.adj')
    h = read_h('input/CMS.h')

    print(f"Number of nodes: {n}")
    print(f"Heutistic: ")
    print(f"Adjacency list: ")
    for i in range(n):
        print(f"Node {i}: {adj[i]}")

    Cms(adj, 0, 6)
