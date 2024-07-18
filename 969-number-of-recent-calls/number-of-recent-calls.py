from collections import deque

TIME_WINDOW = 3000
class RecentCounter:

    def __init__(self):
        self._data = deque()
        

    def ping(self, t: int) -> int:
        self._data.append(t)
        while self._data and self._data[0] < t-TIME_WINDOW:
            self._data.popleft()
        
        return len(self._data)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)