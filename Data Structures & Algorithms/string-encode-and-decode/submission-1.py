class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_text: str = ""
        for word in strs:
            encoded_text += f"{str(len(word))}##{word}"
        return encoded_text

    def decode(self, s: str) -> List[str]:
        ret_list: List[str] = []
        while True:
            (count,_,rest) = s.partition("##")
            if count == s:
                break
            word = rest[:int(count)]
            ret_list.append(word)
            s = rest[int(count):]
        return ret_list
