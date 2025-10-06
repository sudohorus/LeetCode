class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=strs[0]
        p_len=len(p)

        for s in strs[1:]:
            while p != s[0:p_len]:
                p_len -= 1
                if p_len == 0:
                    return ""

                p = p[0:p_len]
        return p