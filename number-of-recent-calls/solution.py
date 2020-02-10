# problem : https://leetcode.com/problems/number-of-recent-calls/submissions/
# for this problem i need to catch pings that made from t-3000
# psuedo algo :
# queue <- pings
# while queue[0] < t - 3000
# pop queue
# return length

import collections


class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)
