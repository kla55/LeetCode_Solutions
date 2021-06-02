class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        newlist = []
        calc = 0
        newlist.append(calc)
        for i in gain:
            calculation = calc + i
            newlist.append(calculation)
            calc = calculation
        newlist.sort()
        return newlist[-1]
