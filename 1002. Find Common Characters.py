class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        for i in words:
            listc = []
            for j in i:
                if j in check:
                    listc.append(j)
                    check.remove(j)
            check = listc
        return check