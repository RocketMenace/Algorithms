

class Solution:

    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(1, len(digits) + 1):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                return digits
        return [1] + digits



if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9]))
