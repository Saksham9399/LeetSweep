class RecentCounter:

    def __init__(self):
        self._data = []
        

    def ping(self, t: int) -> int:
        counter = 0
        self._data.append(t)
        _range = (self._data[-1]-3000,self._data[-1])
        for data in self._data:
            if data >= _range[0] and data<= _range[1]:
                counter +=1
        
        return counter

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)