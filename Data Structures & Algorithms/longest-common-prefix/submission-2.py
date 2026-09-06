class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret_str = ""
        # ["abc", "", "abcd"]
        # 0, a
        for ind, char in enumerate(strs[0]):
            # i = 1
            for i in range(1, len(strs)):
                # comp_str = ""
                comp_str = strs[i]
                # 0 > 1
                if len(comp_str) <= ind or comp_str[ind] != char:
                    return ret_str
            ret_str += char
        return ret_str