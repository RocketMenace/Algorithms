
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first_word = strs[0]
        for i in range(len(first_word)):
            current_char = first_word[i]
            for word in strs[1:]:
                if i >= len(word) or word[i] != current_char:
                    return first_word[:i]
        return first_word



if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
