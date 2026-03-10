class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, n):
        self.queue.append(n)

    def pop(self):
        print(-1 if self.empty() else self.queue.pop(0))

    def size(self):
        print(len(self.queue))

    def empty(self):
        return (0 if len(self.queue) else 1)
    
    def front(self):
        print(-1 if self.empty() else self.queue[0])

    def back(self):
        print(-1 if self.empty() else self.queue[-1])


n = int(input())
q = Queue()

for _ in range(n):
    i = input().split()

    if i[0] == "push":
        q.push(i[1])
    elif i[0] == "pop":
        q.pop()
    elif i[0] == "size":
        q.size()
    elif i[0] == "empty":
        print(q.empty())
    elif i[0] == "front":
        q.front()
    else:
        q.back()