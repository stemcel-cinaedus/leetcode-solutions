class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        pos = (0, 0)
        dx, dy, mdist = 0, 1, 0
        obs = {tuple(x) for x in obstacles}

        for c in commands:
            if c == -1:
                dx, dy = dy, -dx
            elif c == -2:
                dx, dy = -dy, dx
            else:
                for _ in range(c):
                    np = (pos[0] + dx, pos[1] + dy)
                    if np in obs:
                        break
                    else:
                        pos = np
                    if ((pos[0] ** 2) + (pos[1] ** 2)) > mdist:
                                mdist = ((pos[0] ** 2) + (pos[1] ** 2))
        return mdist

