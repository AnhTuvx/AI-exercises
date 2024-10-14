from utils.readfile_bfs import readfile
import os
import drawgraph

def checkin(list, point):
    for i in list:
        if i == point:
            return True
    return False

def Hill(adj, h, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
    n = len(adj)
    Parent = [-1] * n
    current = start
    OPEN.append(start)
    while len(OPEN) > 0:
        current = OPEN.pop(0)
        CLOSE.append(current)
        Tn = []
        if current == stop:
            print("Tim thay duong di")
            path = []  # duong di cua do thi
            idx = stop
            while idx != -1:
                path.append(idx)
                idx = Parent[idx]
            path.reverse()
            print(path)
            return
             
        else:
            for neighbor in range(n):
                if adj[current][neighbor] == 1 and checkin(OPEN, neighbor) == False and checkin(CLOSE, neighbor) == False:
                    Tn.append(neighbor)
                    Parent[neighbor] = current
            for i in range(len(Tn) -1):
                for j in range(i + 1, len(Tn)):
                    if(h[0][Tn[j]] < h[0][Tn[i]]):
                        temp = Tn[i]
                        Tn[i] = Tn[j]
                        Tn[j] = temp
            OPEN = Tn + OPEN
        print(f"{str(current):<4}{str(Tn):<20}{str(OPEN):<20}{str(CLOSE[len(CLOSE)-1]):<20}")
    else: print("Khong tim thay duong di")

n, adj = readfile('hill.txt')
k, h = readfile('hill_h.txt')
print(f"number = {n}")
for i in range(n):
    print(adj[i])
print(f"{'N' :<4}{'Tn' :<20}{'OPEN':<20}{'CLOSE':<20}")
Hill(adj, h, 0, 8)
# drawgraph.draw_graph_from_adjacency_matrix(adj_matrix=adj)