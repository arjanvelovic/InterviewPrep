class MyStack:

    def __init__(self):
        self._queue = collections.deque()
        
    def push(self, x: int) -> None:
        q = self._queue
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self._queue.popleft()
        
    def top(self) -> int:
        return self._queue[0]
        
    def empty(self) -> bool:
        if len(self._queue) == 0:
            return True
        else:
            return False