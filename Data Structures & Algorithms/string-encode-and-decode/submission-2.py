class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for i in strs:
            final_str+=i
            final_str+="``"
        print(final_str)
        return final_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        last_str = ""
        strings = ""
        for i in s:
            if last_str == '`' and i == '`':
                decoded_str.append(strings)
                strings = ""
                last_str = ""
                continue
            elif i == "`":
                last_str = i
                continue
            else:
                strings = strings + i
                last_str = i
        print(decoded_str)
        return decoded_str