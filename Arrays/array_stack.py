

class Solution:

    def build_array(self, target: list[int], n: int) -> list[str]:
        push = "Push"
        pop = "Pop"
        res: list[int] = list()
        stack: list[str] = list()
        for i in range(1, n+1):
            if len(target) == len(res):
                return stack
            stack.append(push)
            res.append(i)
            if i not in target:
                stack.append(pop)
                res.pop()
        return stack





if __name__ == "__main__":

    solution = Solution()
    print(solution.build_array(target = [1,3], n = 3))
    print(solution.build_array(target = [1,2], n = 4))
    print(solution.build_array(target = [2,3,4], n=4))
