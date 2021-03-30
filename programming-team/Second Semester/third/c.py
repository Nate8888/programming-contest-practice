class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    def isEmpty(self): 
        return len(self.queue) == 0
  
    def push(self, data): 
        self.queue.append(data) 
  
    def pop(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit()
	
    def top(self):
       return self.queue[0]

fin = input().split(" ")
amt_researchers = int(fin[0])
m = int(fin[1])

list_of_researchers = []

for i in range(amt_researchers):
	line = input().split(" ")
	research_obj = {'start':int(line[0]),'end':int(line[0])+int(line[1]) }
	list_of_researchers.append(research_obj)

#Sort by start_time.
list_of_researchers = sorted(list_of_researchers, key = lambda i: i['start'])
priority_q = PriorityQueue()

optimizations = 0

for i in range(1, amt_researchers):
	#while it's not empty and mycurrentstart is bigger than the ending+m on top of the priority_q

	while (not priority_q.isEmpty()) and (list_of_researchers[i]['start'] > priority_q.top() + m):
		priority_q.pop() #just pop bc we can't do anything about it
	
	if(priority_q.isEmpty() or priority_q.top() > list_of_researchers[i]['start']):
		#print("TOP OF StACK & Current_start-time: ",priority_q.top(),list_of_researchers[i]['start'])
		optimizations += 1
		priority_q.push(list_of_researchers[i]['end'])

	else:
		priority_q.pop()
		priority_q.push(list_of_researchers[i]['end'])

print(amt_researchers - optimizations)
