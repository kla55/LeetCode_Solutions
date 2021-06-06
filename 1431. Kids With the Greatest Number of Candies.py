class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_greatest = max(candies)
        lista = []
        for i in candies:
            test = i + extraCandies
            if test >= current_greatest:
                lista.append(True)
            else:
                lista.append(False)
        return lista