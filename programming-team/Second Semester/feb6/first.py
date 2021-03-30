from collections import deque
 
 
class Node:
    def __init__(self, x, y, dist=0):
 
        self.x = x
        self.y = y
        self.dist = dist
 
    def __hash__(self):
 
        return hash((self.x, self.y, self.dist))
 
    def __eq__(self, other):
 
        return (self.x, self.y) == (other.x, other.y)
 
 
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 

def valid(x, y, Nr, Nc):
	global not_valid
	if not_valid.get(str(x)+":"+str(y)) != None:
		return False
	return not (x < 0 or y < 0 or x >= Nr or y >= Nc)
 
 
def BFS(src, dest, Nr, Nc):
    visited = set()
    q = deque()
    q.append(src)
    while q:
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
        if x == dest.x and y == dest.y:
            return dist
 
        if (x,y) not in visited:
            visited.add((x,y))
            for i in range(8):
                x1 = x + row[i]
                y1 = y + col[i]
                if valid(x1, y1, Nr, Nc):
                    q.append(Node(x1, y1, dist + 1))
                    #print(x1,y1)
    return -1
 
 
if __name__ == '__main__':
	fin = input().split(" ")
	not_valid = {}
	target_x, target_y,x,y = -1,-1,-1,-1

	for i in range(int(fin[0])):
			line = input()
			c = 0
			for char in line:
				if char == "#":
					not_valid[str(i)+":"+str(c)] = 1
				elif char == "X":
					target_x = i
					target_y = c
				elif char == "K":
					x = i
					y = c
				c += 1
	Nr = int(fin[0])
	Nc = int(fin[1])
	src = Node(x, y)
	dest = Node(target_x, target_y)
	#print(not_valid,x,y,target_x,target_y)
	print(BFS(src, dest, Nr, Nc))