from utils.readfile_bfs import readfile
import os

def checkin(list, point):
    for i in list:
        if i == point:
            return True
    return False

def DFS(adj, start, stop):
    OPEN = []
    CLOSE = []
    Tn = []
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
                    OPEN = Tn + OPEN
                    Parent[neighbor] = current
        print(f"{str(current):<4}{str(Tn):<20}{str(OPEN):<20}{str(CLOSE):<20}")
        
    else: print("Khong tim thay duong di")
    
    
if __name__ == '__main__':
    
    n, adj = readfile('bfs.txt')
    print(f"number = {n}")
    for i in range(n):
        print(adj[i])
    print(f"{'N' :<4}{'Tn' :<20}{'OPEN':<20}{'CLOSE':<20}")
    DFS(adj, 0, 6)
    
    
    