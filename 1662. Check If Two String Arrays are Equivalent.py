class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        Statement = ""
        word_1 = [''.join(map(str,word1))]
        word_2 = [''.join(map(str,word2))]
        if word_1 == word_2:
            return True
        else:
            return False
        