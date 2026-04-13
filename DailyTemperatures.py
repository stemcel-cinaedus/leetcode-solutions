class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = [0] * len(temperatures)
        stack = []
        stack.append((temperatures[len(temperatures) - 1], len(temperatures) - 1))
        i = len(temperatures) - 1
        while i >= 0:
            if temperatures[i] >= stack[len(stack) - 1][0]:
                while stack and temperatures[i] >= stack[len(stack) - 1][0]:
                    stack.pop()
                if stack:
                    a[i] = (stack[len(stack) - 1][1] - i)
                else:
                    a[i] = 0    
                stack.append((temperatures[i], i))
            else:
                a[i] = 1
                stack.append((temperatures[i], i))
            i -= 1
        return a
