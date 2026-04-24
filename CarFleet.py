class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sorted_cars = []
        for pos, spd in sorted(zip(position, speed)):
            arrival = ((target - pos) / spd)
            sorted_cars.append([pos, arrival])
        i = len(sorted_cars) -1
        #This checks the positions from lowest to highest and just matches them with the speeds
        while i >= 0:
            if len(stack) > 0:
                if sorted_cars[i][1] > stack[-1]:
                    stack.append(sorted_cars[i][1])
            else:
                stack.append(sorted_cars[i][1])
            i -= 1
        return len(stack)


