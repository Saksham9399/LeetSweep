class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        points = [0] # n+1 points starting from 0
        latest = 0
        for idx,g in enumerate(gain):
            latest = gain[idx]+ points[-1]
            points.append(latest)
        return max(points)