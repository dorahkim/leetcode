# 317. Shortest Distance from All Buildings

class Solution:        
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        # key: (x, y), value: [# of building, total distance]
        land = {}
        building = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    building.append([r, c])
                elif grid[r][c] == 0:
                    land[(r, c)] = [0, 0]
        
        # breadth-first search
        for i in range(len(building)):
            q = [building[i]]
            dist = 1
            
            while len(q) > 0:
                newq = []
                for r, c in q:
                    if (r + 1, c) in land and land[(r + 1, c)][0] == i:
                        land[(r + 1, c)][0] += 1
                        land[(r + 1, c)][1] += dist
                        newq.append((r + 1, c))
                    if (r - 1, c) in land and land[(r - 1, c)][0] == i:
                        land[(r - 1, c)][0] += 1
                        land[(r - 1, c)][1] += dist
                        newq.append((r - 1, c))
                    if (r, c + 1) in land and land[(r, c + 1)][0] == i:
                        land[(r, c + 1)][0] += 1
                        land[(r, c + 1)][1] += dist
                        newq.append((r, c + 1))
                    if (r, c - 1) in land and land[(r, c - 1)][0] == i:
                        land[(r, c - 1)][0] += 1
                        land[(r, c - 1)][1] += dist
                        newq.append((r, c - 1))
                q = newq
                dist += 1
        
        # check the number of reachable buildings
        rtn = -1
        for key in land.keys():
            if land[key][0] == len(building):
                if rtn == -1:
                    rtn = land[key][1]
                else:
                    rtn = min(rtn, land[key][1])
        
        return rtn
