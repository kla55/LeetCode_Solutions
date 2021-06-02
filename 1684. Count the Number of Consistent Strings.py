class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        distinct = set(allowed)
        for i in words:
            count = 0
            for j in i:
                if j in distinct:
                    count = count + 1
            if count == len(i):
                consistent = consistent + 1
        return consistent