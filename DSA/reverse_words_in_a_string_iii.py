class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        answer = []

        for word in words:
            st = list(word)
            i = 0
            j = len(st)-1

            while i < j:
                st[i], st[j] = st[j], st[i]
                i += 1
                j -= 1
        
            answer.append("".join(st))
        
        return " ".join(answer)