class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minAngle = (minutes/60) * 360
        hourAngle = (((hour % 12) * 30) + ((minutes/60) * 30))

        angleDiff = abs(hourAngle - minAngle)
        return min(angleDiff, 360 - angleDiff)
        