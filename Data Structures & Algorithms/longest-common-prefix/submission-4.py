class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret_str = ""
        for ind, char in enumerate(strs[0]):
            for i in range(1, len(strs)):
                if len(strs[i]) <= ind or strs[i][ind] != char:
                    return ret_str
            ret_str += char
        return ret_str