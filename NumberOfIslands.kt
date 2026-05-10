class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        var count = 0
        val directions = listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)

        fun dfs(r: Int, c: Int) {
            grid[r][c] = '0'

            for ((dr, dc) in directions){
                if ((r + dr) in grid.indices && (c + dc) in grid[0].indices && grid[r + dr][c + dc] == '1') {
                    dfs(r + dr, c + dc)
                }
            }
        }

        for (r in grid.indices) {
            for (c in grid[r].indices) {
                if (grid[r][c] == '1') {
                    dfs(r, c)
                    count++
                }
            }
        }


        return count
        
    }
}