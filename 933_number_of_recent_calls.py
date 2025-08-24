class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        start = -3000 + t
        end = t
        count = 0

        self.requests.append(t)
        self.requests = sorted(self.requests, reverse=True)
        
        for req in self.requests:
            if req >= start and req <= end:
                count += 1
            else:
                return count
        
        return count