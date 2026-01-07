

class Solution:

    def merge(self, nums_1: list[int], m: int, nums_2: list[int], n: int) -> None:
        # Last index of nums_1
        x, y = m-1, n-1
        for z in range(m + n - 1, -1, -1):
            if x < 0:
                nums_1[z] = nums_2[y]
                y -= 1
            elif y < 0:
                break
            elif nums_1[x] > nums_2[y]:
                nums_1[z] = nums_1[x]
                x -= 1
            else:
                nums_1[z] = nums_2[y]
                y -= 1



if __name__ == "__main__":
    solution = Solution()
    print(solution.merge(nums_1 = [1,2,3,0,0,0], m = 3, nums_2 = [2,5,6], n = 3))